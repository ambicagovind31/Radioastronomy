import scipy.stats as stats
from astropy.io import ascii
from scipy.optimize import curve_fit
from mcmc import best_fit_model
import matplotlib.pyplot as plt

def gaussian(x,disp, amp, mu,sigma):
    return disp+amp*stats.norm.pdf(x,mu,sigma)

data=ascii.read('/home/ambica/Downloads/galaxy_21cm_spectrum/spectrum_d_0.69_kpc.txt')
popts, pcovs=curve_fit(gaussian, data["wavelngth (cm)"],data['brightness'],p0=(0,3000,21,1))
model= best_fit_model
plt.plot(data["wavelngth (cm)"],model,'--',label='Highest Likelihood Model')
plt.plot(data["wavelngth (cm)"],data['brightness'],label='21-cm spectral line(data)')
plt.plot(data["wavelngth (cm)"],gaussian(data["wavelngth (cm)"],popts[0],popts[1],popts[2],popts[3]),color='black',label='Scipy curvefit')
plt.legend()
plt.show()


