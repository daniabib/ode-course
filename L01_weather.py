import numpy as np
import matplotlib.pyplot as plt

DAYS: int = 50

A = np.array([[0.5, 0.5, 0.25], [0.25, 0., 0.25], [0.25, 0.5, 0.5]])

x_today = np.array([0, 1, 0]).T

weather = np.zeros((DAYS, 3))

# for k in range(50):
#     x_tomorrow = A @ x_today
#     print(x_tomorrow)
#     x_today = x_tomorrow

weather[0, :] = x_today
for k in range(DAYS):
    x_today = A @ x_today
    weather[k, :] = x_today
    print(x_today)

print(x_today)

plt.plot(weather)
plt.show()