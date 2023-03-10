import numpy as np
import matplotlib.pyplot as plt

THETA_0 = np.pi / 3
THETA_DOT_0 = 0

g = 9.8
L = 2
mu = 0.1


def get_theta_double_dot(theta, theta_dot):
    return -mu * theta_dot - (g / L) * np.sin(theta)


def theta(t, theta=THETA_0, theta_dot=THETA_DOT_0, delta_t=0.01):
    for time in np.arange(0, t, delta_t):
        theta_double_dot = get_theta_double_dot(theta, theta_dot)
        theta += theta_dot * delta_t
        theta_dot += theta_double_dot * delta_t
    return theta


print(theta(10, THETA_0, THETA_DOT_0))

x, y = np.meshgrid(np.linspace(-5, 5, 10), np.linspace(-5, 5, 10))

plt.quiver(x, y, 1, -1)
plt.show()

