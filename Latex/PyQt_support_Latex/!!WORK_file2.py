import sys
import matplotlib as mpl
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication, QMainWindow, QSizePolicy
from matplotlib.backends.backend_agg import FigureCanvasAgg
from PyQt6 import QtGui, QtCore
from matplotlib.figure import Figure
from _My_Library.My_Function.Pixmap_Latex import mathTex_to_QPixmap


# def mathTex_to_QPixmap(mathTex, font_size):
#
#     #---- set up a mpl figure instance ----
#
#     fig = Figure()
#
#     fig.patch.set_facecolor('none')
#
#     fig.set_canvas(FigureCanvasAgg(fig))
#     renderer = fig.canvas.get_renderer()
#
#     #---- plot the mathTex expression ----
#
#     axes = fig.add_axes([0, 0, 1, 1])
#     axes.axis('off')
#
#     axes.patch.set_facecolor('none')
#
#     text = axes.text(0, 0, mathTex, ha='left', va='bottom', fontweight='bold',
#                      fontsize=font_size, fontfamily='GOST 2.304 type A')
#
#     #---- fit figure size to text artist ----
#
#     fwidth, fheight = fig.get_size_inches()
#     fig_bbox = fig.get_window_extent(renderer)
#
#     text_bbox = text.get_window_extent(renderer)
#
#     tight_fwidth = text_bbox.width * fwidth / fig_bbox.width
#     tight_fheight = text_bbox.height * fheight / fig_bbox.height
#
#     fig.set_size_inches(tight_fwidth, tight_fheight)
#
#     #---- convert mpl figure to QPixmap ----
#
#     buf, size = fig.canvas.print_to_buffer()
#     qimage = QtGui.QImage.rgbSwapped(QtGui.QImage(buf, size[0], size[1],
#                                                   QtGui.QImage.Format.Format_ARGB32))
#     qpixmap = QPixmap(qimage)
#
#
#     return qpixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        widget = QWidget()
        self.setCentralWidget(widget)
        number = 5
        web_thickness = 5
        flange_thickness = 5

        formulaList = [r'$\sqrt{\beta}$', r'$\sqrt{\beta}$', 'Момент инерции сечения\n $I_{x}=5 см^{2}$', ' какая-то херня',
                       f'Толщина стенки: $t_{'w'}$ = {web_thickness}', f'Толщина полки: $t_{'f'} = {web_thickness} мм$']

        vlayout = QVBoxLayout()
        vlayout.setSpacing(0)
        i = 1
        for text in formulaList:

            pixmap = mathTex_to_QPixmap(text, 15)
            name = 'picture_'+str(i)+'.png'
            pixmap.save(name)
            i += 1
            label2 = QLabel()
            label2.setStyleSheet('background-color:red;'
                                 'font: bold;'
                                 'border: none;'
                                 'padding-left:10px;'
                                 'padding-right:100px;'
                                 'padding-top:1px')

            label2.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
            label2.setPixmap(pixmap)
            vlayout.addWidget(label2)


        label2 = QLabel('Конец')
        #label2.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        label2.setStyleSheet('background-color:red;'
                             'border: 2px solid black;'
                             'font-size:15pt;'
                             'padding-left:10px;'
                             'padding-top:1px;'
                             'font-family:GOST 2.304 type A')
        label2.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

        label3 = QLabel('Конец2')
        label3.setStyleSheet('background-color:red;'
                             'border: none;'
                             'font-size:15pt;'
                             'padding-left:10px;'
                             'padding-top:1px;'
                             'font-family:Bookman Old Style')
        label3.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        vlayout.addWidget(label2)
        vlayout.addWidget(label3)





        widget.setLayout(vlayout)




app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


