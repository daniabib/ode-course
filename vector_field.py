import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

GRID_DEFINITION = 40

THETA_0 = np.pi / 3
THETA_DOT_0 = 0

g = 9.8
L = 2
mu = 0.1

theta = sym.Symbol('t')


def get_theta_double_dot(theta, theta_dot):
    return -mu * theta_dot - (g / L) * np.sin(theta)


def theta_derivs_over_time(time, theta=THETA_0, theta_dot=THETA_DOT_0, delta_t=0.01):
    thetas = []
    theta_dots = []
    theta_double_dots = []
    # for _ in np.arange(0, time, delta_t):
    for _ in np.linspace(0, 10, GRID_DEFINITION**2):
        theta_double_dot = get_theta_double_dot(theta, theta_dot)
        theta += theta_dot * delta_t
        theta_dot += theta_double_dot * delta_t
        thetas.append(theta)
        theta_dots.append(theta_dot)
        theta_double_dots.append(theta_double_dot)
    return thetas, theta_dots, theta_double_dots

def get_output_vector(theta, theta_dot, delta_t=0.01):
    theta_double_dot = get_theta_double_dot(theta, theta_dot)
    return 

thetas, theta_dots, theta_double_dots = theta_derivs_over_time(
    10, THETA_0, THETA_DOT_0)

# plt.plot(thetas, theta_dots)
# plt.show()

xs = np.radians(np.linspace(-330, 330, GRID_DEFINITION))
ys = np.linspace(-4.5, 4.5, GRID_DEFINITION)



x, y = np.meshgrid(xs, ys)


v = -mu * y - (g / L) * np.sin(x)

skip = (slice(None, None, 3), slice(None, None, 3))


fig, ax = plt.subplots()
im = ax.imshow(v, extent=[x.min(), x.max(), y.min(), y.max()])
ax.quiver(x[skip], y[skip], y[skip], v[skip], v[skip])


fig.colorbar(im)
ax.set(aspect=1, title='Quiver Plot')
plt.show()
