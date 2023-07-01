import numpy as np
import matplotlib.pyplot as plt
import emcee
import scipy.stats as stats
from astropy.io import ascii 

def model(parameters, x):
    disp,amp,mu,sigma=parameters
    return disp+amp*stats.norm.pdf(x,mu,sigma)

def likelihood(parameters,x,y,yerr):
    return -0.5 * np.sum(((y - model(parameters, x))/yerr) ** 2)

def priors(parameters):
    disp,amp,mu,sigma=parameters
    if 0.0<disp<100.0 and 0.0<amp<100.0 and 20.8<mu<21.2 and 0.0<sigma<1.0:
        return 0.0
    return -np.inf

def probability(parameters,x,y,yerr):
    lp=priors(parameters)
    if not np.isfinite(lp):
        return -np.inf
    return likelihood(parameters,x,y,yerr)

def main(p0,nwalkers,steps,ndim,probability,data):
    sampler= emcee.EnsembleSampler(nwalkers, ndim, probability, args=data)
    print("Running burn-in...")
    p0, _, _ = sampler.run_mcmc(p0, 100)
    sampler.reset()
    print("Running production...")
    pos, prob, state = sampler.run_mcmc(p0, steps)
    return sampler, pos, prob, state

def plot(sampler,wvl,bri):
    plt.ion()
    plt.plot(wvl,bri,label='Spectrum of 21-cm line')
    samples = sampler.flatchain
    for theta in samples[np.random.randint(len(samples), size=100)]:
        plt.plot(wvl, model(theta, wvl), color="r")
    plt.xlabel('Wavelength')
    plt.ylabel('Brightness')
    plt.legend()
    plt.show(block=True)

file_data=ascii.read('/home/ambica/Downloads/galaxy_21cm_spectrum/spectrum_d_0.69_kpc.txt')
yerr=0.05*np.mean(file_data["wavelngth (cm)"])
wvl=file_data["wavelngth (cm)"]
bri=file_data['brightness']
data=(wvl,bri,yerr)
nwalkers=500
niter=1000
initial=np.array([0,1,21,0.1])
ndim=len(initial)
p0 = [np.array(initial) + 1e-7 * np.random.randn(ndim) for i in range(nwalkers)]
sampler, pos, prob, state = main(p0,nwalkers,niter,ndim,probability,data)
#plot(sampler,wvl,bri)

samples=sampler.flatchain
best_parameters=samples[np.argmax(sampler.flatlnprobability)]
best_fit_model=model(best_parameters,wvl)
#plt.plot(wvl,bri,label='21-cm spectral line')
#plt.plot(wvl,best_fit_model,'--',label='Highest Likelihood Model')
#plt.legend()
#plt.show()
print('Best parameters',best_parameters)



#Output: [5.37206491e+00 1.04274420e+01 2.10024518e+01 7.00450472e-04]