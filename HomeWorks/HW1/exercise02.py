import numpy as np
import matplotlib.pyplot as plt

URANIUM_HALF_LIFE = 4.468e9

uranium_lamb = np.log(0.5)/URANIUM_HALF_LIFE

print(uranium_lamb)

t = np.linspace(0, 5, 100)

k = 2  # Initial condition x(0)

lambdas = [-5, -1, 0, 0.01, 0.1, uranium_lamb]


def radioactive_decay(t, k, lamb):
    return np.exp(lamb * t) * k


fig = plt.figure()
fig.show()
ax = fig.add_subplot(111)

for l in lambdas:
    ax.plot(t, radioactive_decay(t, k, l), label=f"lambda = {l}")

plt.legend(loc=2)
plt.show()

