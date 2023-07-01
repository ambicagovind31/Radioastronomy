import matplotlib.pyplot as plt
import corner
from mcmc import samples
labels=['disp','amp','mu','sigma']
fig = corner.corner(samples,show_titles=True,labels=labels,plot_datapoints=True)
plt.show()