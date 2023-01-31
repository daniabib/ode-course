import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-8, 8, 1000)

# a)
real = np.cos(t)
im = np.sin(t)

plt.plot(t, real, label="real part")
plt.plot(t, im, label="imaginary part")
plt.xlabel("t")
plt.ylabel("y")
plt.title("Exercise 3-a")
plt.legend()
plt.show()

# b)
real = np.exp(-t) * np.cos(t)
im = - np.exp(-t) * np.sin(t)

plt.plot(t, real, label="real part")
plt.plot(t, im, label="imaginary part")
plt.xlabel("t")
plt.ylabel("y")
plt.title("Exercise 3-b")
plt.legend()
plt.show()

# c)
real = np.e * np.cos(t)
im = -np.e * np.sin(t)

plt.plot(t, real, label="real part")
plt.plot(t, im, label="imaginary part")
plt.xlabel("t")
plt.ylabel("y")
plt.title("Exercise 3-c")
plt.legend()
plt.show()

# d)
real = np.exp(-0.2*t) * np.cos(9.42478 * t)
im = -np.exp(-0.2*t) * np.sin(9.42478 * t)

plt.plot(t, real, label="real part")
plt.plot(t, im, label="imaginary part")
plt.xlabel("t")
plt.ylabel("y")
plt.title("Exercise 3-d")
plt.legend()
plt.show()