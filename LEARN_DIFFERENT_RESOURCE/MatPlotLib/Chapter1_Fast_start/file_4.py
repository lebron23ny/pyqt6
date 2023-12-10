import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 10, 50)
y1 = x

y2 = [i**2 for i in x]


plt.figure()

plt.subplot(2, 1, 1)
plt.plot(x, y1)
plt.title("Зависимости: y1 = x, y2 = x^2")
plt.ylabel('y1', fontsize=14)
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(x, y2)
plt.xlabel('x', fontsize=14)
plt.ylabel('y2', fontsize=14)
plt.grid(True)

plt.show()