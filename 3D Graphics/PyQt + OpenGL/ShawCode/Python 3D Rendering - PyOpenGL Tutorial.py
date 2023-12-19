#https://www.youtube.com/watch?v=eHw6zKUw3uU&t=286s
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys




def draw():
    xrot = 45
    yrot = 45
    ambient = (1.0, 1.0, 1.0, 1)  # Первые три числа - цвет в формате RGB, а последнее - яркость
    greencolor = (0.2, 0.8, 0.0, 0.8)  # Зеленый цвет для иголок
    treecolor = (0.9, 0.6, 0.3, 0.8)  # Коричневый цвет для ствола
    lightpos = (1.0, 1.0, 1.0)

    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(xrot, 1, 0, 0)
    glRotatef(yrot, 0, 1, 0)



    glutWireCube(0.7)
    glFlush()





glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow("Cube")
glutDisplayFunc(draw)

glutMainLoop()
