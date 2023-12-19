#https://www.youtube.com/watch?v=W3-SMvMa8D4
from PyQt6.QtGui import QColor
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from PyQt6.QtOpenGL import QOpenGLWindow
from PyQt6.QtOpenGL import QOpenGLFunctions_2_1


class MyOPenGLWidget(QOpenGLWidget, QOpenGLFunctions_2_1):
    def __init__(self, parent=None):
        super().__init__()


    def initializeGL(self):
        self.initializeOpenGLFunctions()
        self.glClearColor(0, 0, 0, 0)




    def paintGL(self):
        pass

    def resizeGL(self, w, h):
        pass
