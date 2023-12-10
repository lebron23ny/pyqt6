
from PyQt6.QtGui import QPixmap
from matplotlib.backends.backend_agg import FigureCanvasAgg
from PyQt6 import QtGui
from matplotlib.figure import Figure

def mathTex_to_QPixmap(mathTex, font_size):

    #---- set up a mpl figure instance ----

    fig = Figure()

    fig.patch.set_facecolor('none')

    fig.set_canvas(FigureCanvasAgg(fig))
    renderer = fig.canvas.get_renderer()

    #---- plot the mathTex expression ----

    axes = fig.add_axes([0, 0, 1, 1])
    axes.axis('off')

    axes.patch.set_facecolor('none')

    text = axes.text(0, 0, mathTex, ha='left', va='bottom', fontsize=font_size, fontfamily='GOST 2.304 type A')

    #---- fit figure size to text artist ----

    fwidth, fheight = fig.get_size_inches()
    fig_bbox = fig.get_window_extent(renderer)

    text_bbox = text.get_window_extent(renderer)

    tight_fwidth = text_bbox.width * fwidth / fig_bbox.width
    tight_fheight = text_bbox.height * fheight / fig_bbox.height

    fig.set_size_inches(tight_fwidth, tight_fheight)

    #---- convert mpl figure to QPixmap ----

    buf, size = fig.canvas.print_to_buffer()
    qimage = QtGui.QImage.rgbSwapped(QtGui.QImage(buf, size[0], size[1],
                                                  QtGui.QImage.Format.Format_ARGB32))
    qpixmap = QPixmap(qimage)


    return qpixmap