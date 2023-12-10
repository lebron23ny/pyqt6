import matplotlib.pyplot as plt

#add text

plt.text(0, 0, r'$\alpha > \beta$', fontsize=50, va='center')
plt.axis('off')
plt.gcf().set_size_inches(10, 5)
#hide axes
fig = plt.gca()

fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)


plt.savefig('filename.png')