#https://www.youtube.com/watch?v=lFFYmP528Mw

import ctypes
import sys

import numpy as np

from OpenGL.GL import *
from OpenGL.GL.shaders import compileShader, compileProgram

from PyQt6.QtGui import QSurfaceFormat
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication
from PyQt6.QtOpenGL import QOpenGLWindow, QOpenGLVersionProfile

vertex_scr = '''
#version 330 core

layout (location=0) in vec3 vertexPos;
layout (location=1) in vec3 vertexColor;

out vec3 fragmentColor;

void main()
{
    gl_Position = vec4(vertexPos, 1.0);
    fragmentColor = vertexColor;
}
'''

fragment_scr = '''
#version 330 core

in vec3 fragmentColor;

out vec4 color;

void_main()
{
    color = vec4(fragmentColor, 1.0);
}
'''

class GLWindow(QOpenGLWindow):
    def initializeGL(self):
        self.fmt = QOpenGLVersionProfile()
        self.fmt.setVersion(3, 3)
        self.fmt.setProfile(QSurfaceFormat.QOpneGLContextProfile.CornerProfile)


        #print(f'running {glGetString(GL_Version)}')

        self.shader = compileProgram(compileShader(vertex_scr, GL_VERTEX_SHADER),
                                     compileShader(fragment_scr, GL_FRAGMENT_SHADER))
        glUseProgram(self.shader)

        self.vertices = (
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
            0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
            0.0, 0.5, 0.0, 0.0, 0.0, 1.0
        )
        self.vertices = np.array(self.vertices, dtype=np.float32)

        self.vbo = glGenBuffers(1)
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        glBindBuffer(GL_ARRAY_BUFFER, self.vao)

        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))


    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glUseProgram(self.shader)
        glBindVertexArray(self.vao)
        glDrawArrays(GL_TRIANGLES, 0, 6)



app = QApplication(sys.argv)
window = GLWindow()
window.resize(QSize(800, 600))
window.show()
app.exec()

