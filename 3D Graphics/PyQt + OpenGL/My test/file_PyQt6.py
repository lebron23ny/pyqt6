#https://www.youtube.com/watch?v=CcYPs6Sbdsg
from PyQt5.QtOpenGL import QGLWidget
from PyQt6.QtGui import QColor, QOpenGLContext
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
import sys
from PyQt6.QtOpenGL import QOpenGLWindow, QOpenGLFunctions_2_1
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL import GL as gl


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


class GLWidget(QOpenGLWidget):

        def __init__(self):
            super().__init__()


        def initializeGL(self):
            gl.glClearColor(255, 0, 0, 1)

        def paintGL(self):
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)


app = QApplication(sys.argv)
wind = MainWindow()
wind.show()
app.exec()