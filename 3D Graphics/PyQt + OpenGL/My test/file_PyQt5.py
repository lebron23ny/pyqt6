
from PyQt5.QtOpenGL import QGLWidget
from PyQt5.QtGui import QColor, QOpenGLContext
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
import sys
from PyQt6.QtOpenGL import QOpenGLWindow, QOpenGLFunctions_2_1
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL import GL as gl
from OpenGL.GL import *
from OpenGL.GLU import *


class MainWindow(QWidget):
        def __init__(self):
            super().__init__()

            layout = QVBoxLayout()
            self.setLayout(layout)
            self.gl_widget = GLWidget()
            self.button = QPushButton('Кнопка')

            layout.addWidget(self.gl_widget)
            layout.addWidget(self.button)


            self.gl_widget.setMinimumSize(300, 400)


class GLWidget(QGLWidget):
    def __init__(self):
        super().__init__()


    def initializeGL(self):
        self.qglClearColor(QColor(200, 0, 0))
        gl.glEnable(gl.GL_DEPTH_TEST)
        #self.init_cube()

    def paintGL(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)



    def init_cube(self):
        self.verticies = (
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, -1, 1),
            (-1, 1, 1)
        )
        edges = (
            (0, 1),
            (0, 3),
            (0, 4),
            (2, 1),
            (2, 3),
            (2, 7),
            (6, 3),
            (6, 4),
            (6, 7),
            (5, 1),
            (5, 4),
            (5, 7)
        )
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(self.verticies[self.vertex])
        glEnd()


app = QApplication(sys.argv)
wind = MainWindow()
wind.show()
app.exec()