import matplotlib.pyplot as plt
import numpy as np

# Boltzmann constant
k = 1.38e-23

# Plot the entropy as a function of temperature
T = np.linspace(0, 400, 100)
S = k * np.log(T)
plt.plot(T, S)
plt.xlabel('Temperature (K)')
plt.ylabel('Entropy (J/K)')
plt.show()
