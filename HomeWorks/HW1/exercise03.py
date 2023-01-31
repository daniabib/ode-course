import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
from sympy.utilities.lambdify import lambdify

def f(x):
    x = sy.symbols('x')
    return sy.sin(x)/x

def g(x):
    return sy.exp(x)

def taylor_expansion(f, a=1, n=3):
    x = sy.symbols('x')
    func = f(x)
    result = func.subs(x, a)
    for i in range(1, n):
        result += sy.diff(func, x, i).subs(x, a) * ((x - a)**i)/(sy.factorial(i))
    sy.pretty_print(result)
    return lambdify(x, result)

x = np.linspace(-9.4, 9.4, 200)

func_to_plot = taylor_expansion(f, n=10)

plt.plot(x, np.sin(x), 'k', label='Analytic')
plt.plot(x, [func_to_plot(i) for i in x])
plt.legend()
plt.show()

taylor_expansion(g, n=6)
