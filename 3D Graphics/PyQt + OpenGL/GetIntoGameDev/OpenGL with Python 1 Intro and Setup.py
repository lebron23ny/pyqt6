#https://www.youtube.com/watch?v=mOTE_62i5ag&list=PLn3eTxaOtL2PDnEVNwOgZFm5xYPr4dUoR&index=2
import pygame as pg
from OpenGL.GL import *
import numpy as np
import ctypes

from OpenGL.GL.shaders import compileShader, compileProgram

class Triangle:
    def __init__(self):


        #x, y, z, r, g, b
        self.vertices = (
            -0.5, -0.5, 0.0, 1.0, 0.0, 0,
            0.5, -0.5, 0.0, 0.0, 1, 0,
            0.0, 0.5, 0.0, 0.0, 0, 1,
        )

        self.vertices = np.array(self.vertices, dtype=np.float32)

        self.vertex_count = 3

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)
        glEnableVertexArrayAttrib(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
        glEnableVertexArrayAttrib(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))


    def destroy(self):

        glDeleteVertexArrays(1, (self.vao, ))
        glDeleteBuffers(1, (self.vbo, ))





class App:
    def __init__(self):
        pg.init()
        pg.display.set_mode((640, 480), pg.OPENGL | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        #initialize opengl
        glClearColor(1, 0.2, 0.2, 1)
        self.shader = self.createShader("Shaders/vertex.txt", "Shaders/fragment.txt")
        glUseProgram(self.shader)
        self.triangle = Triangle()
        self.mainLoop()


    def createShader(self, vertexFilePath, fragmentFilePath):
        with open(vertexFilePath, 'r') as f:
            vertex_scr = f.readlines()
        with open(fragmentFilePath, 'r') as f:
            fragment_scr = f.readlines()

        shader = compileProgram(
            compileShader(vertex_scr, GL_VERTEX_SHADER),
            compileShader(fragment_scr, GL_FRAGMENT_SHADER)
        )

        return shader

    def mainLoop(self):
        running = True
        while (running):
            #check event
            for event in pg.event.get():
                if (event.type == pg.WINDOWCLOSE):
                    running = False
            #refresh screen
            glClear(GL_COLOR_BUFFER_BIT)

            glUseProgram(self.shader)
            glBindVertexArray(self.triangle.vao)
            glDrawArrays(GL_TRIANGLES, 0, self.triangle.vertex_count)

            pg.display.flip()
            #timing
            self.clock.tick(60)

        self.quit()


    def quit(self):

        self.triangle.destroy()
        glDeleteProgram(self.shader)
        pg.quit()





if __name__ == '__main__':
    app = App()



