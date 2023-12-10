import matplotlib.pyplot as plt


def renderLaTeX(a, path, usetex=True, dpi=500, fontsize=20):
    acopy = a
    plt.figure(figsize=(0.3, 0.3))
    if usetex:  # Use real Latex rendering
        try:
            a = '$\\displaystyle ' + a.strip('$') + ' $'
            plt.text(-0.3, 0.9, a, fontsize=fontsize, usetex=usetex)  #
        except:
            usetex = False

    if not usetex:
        a = acopy
        a = a.strip('$')
        a = '\n'.join([' $ ' + _ + ' $ ' for _ in a.split('\\\\')])
        plt.text(-0.3, 0.9, a, fontsize=fontsize, usetex=usetex)

    plt.ylim(0, 1)
    plt.xlim(0, 6)
    plt.axis('off')  # Hidden coordinate system
    plt.savefig(path, dpi=dpi, bbox_inches='tight')
    plt.close()


renderLaTeX(r'c:\ |z|=1 \\ \frac{1}{2\pi i}\int_c \frac{f(z)}{z-z_0}dz = Res_{z=z_0}f(z)', 'Formula.png', usetex=True)