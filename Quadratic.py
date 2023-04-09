import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(y, x):
    return x**2

y0 = 1
x = np.linspace(0, 5, 101)
sol = odeint(f, y0, x)

plt.plot(x, sol)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
