

import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
AutoMinorLocator)
import numpy as np


x = np.linspace(0, 10, 10)
y1 = 4*x
y2 = [i**2 for i in x]
fig, ax = plt.subplots(figsize=(8, 6))
#ax.set_title('Графики зависимостей: y1=4*x, y2=x^2', fontsize=16, fontfamily='GOST 2.304 type A')
ax.set_title('Графики зависимостей $y_{1}=4x, y_{2}=x^{2}$', fontsize=16, fontfamily='GOST 2.304 type A',
             fontweight='bold')
ax.set_xlabel('x', fontsize=14, fontfamily='GOST 2.304 type A')
ax.set_ylabel('y1, y2', fontsize=14, fontfamily='GOST 2.304 type A')
ax.grid(which='major', linewidth=1.2)
ax.grid(which='minor', linestyle='-', color='gray', linewidth=0.5)
ax.scatter(x, y1, c='red',linestyle='-', label='y1 = 4*x')
ax.plot(x, y2, label='y2 = x^2')
#ax.legend()
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(which='major', length=10, width=2)
ax.tick_params(which='minor', length=5, width=1)
plt.text(5, 5, 'Графики зависимостей \n $y_{1}=4x$ \n $y_{2}=x^{2}$', fontsize=16, fontfamily='GOST 2.304 type A')
plt.text(5, 0, 'Графики зависимостей жирный', fontsize=16, weight='bold',
         fontfamily='GOST 2.304 type A')
plt.show()