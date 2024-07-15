import numpy as np 
import matplotlib.pyplot as plt
from  ipywidgets import interact

n = 18
x_values = np.linspace(-2, 3, n)
y_values = x_values**2 - 1
plt.plot(x_values, y_values, 'r')
plt.legend([f"$y=x^2$ with {n} points"])
plt.show()

