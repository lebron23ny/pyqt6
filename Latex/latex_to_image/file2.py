import matplotlib.pyplot as plt                                                 
import sympy
from matplotlib.figure import Figure

figure = Figure(figsize=(2, 2))
figure.clear()
latex_formula = r'$\alpha > \beta$'
w = 5
h = 1.25
# figure.set_size_inches(w,h)
figure.set_facecolor('white')
size = 55
ax = figure.add_subplot(111)
ax.text(0, 0, latex_formula, size=55, ha='center', va='center')
ax.axis('off')
figure.savefig('filename3.png')