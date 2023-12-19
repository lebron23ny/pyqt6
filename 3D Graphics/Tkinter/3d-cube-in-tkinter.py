#https://billyeatcookies.github.io/2023-04-08/rendering-3d-in-tkinter
import math
import numpy as np
import tkinter as tk

vertices = [
    (100, 100, 100),
    (100, 100, -100),
    (100, -100, 100),
    (100, -100, -100),
    (-100, 100, 100),
    (-100, 100, -100),
    (-100, -100, 100),
    (-100, -100, -100)
]

edges = [
    (0, 1), (0, 2), (0, 4),
    (1, 3), (1, 5),
    (2, 3), (2, 6),
    (3, 7),
    (4, 5), (4, 6),
    (5, 7),
    (6, 7),
]


def rotate_x(theta):
    return [
        [1, 0, 0],
        [0, math.cos(theta), -math.sin(theta)],
        [0, math.sin(theta), math.cos(theta)],
    ]


def rotate_y(theta):
    return [
        [math.cos(theta), 0, math.sin(theta)],
        [0, 1, 0],
        [-math.sin(theta), 0, math.cos(theta)],
    ]


def rotate_z(theta):
    return [
        [math.cos(theta), -math.sin(theta), 0],
        [math.sin(theta), math.cos(theta), 0],
        [0, 0, 1],
    ]


def draw_mesh(vertices, edges):
    for edge in edges:
        x1, y1, z1 = vertices[edge[0]]
        x2, y2, z2 = vertices[edge[1]]
        canvas.create_line(x1 + 250, y1 + 250, x2 + 250, y2 + 250)

    for vertex in vertices:
        x, y, z = vertex
        r = 5
        canvas.create_oval(x - r + 250, y - r + 250, x + r + 250, y + r + 250, fill='white')


def animate():
    global vertices

    rotation_matrix = np.dot(rotate_x(0.01), np.dot(rotate_y(0.02), rotate_z(0.03)))
    vertices = [np.dot(rotation_matrix, vertex) for vertex in vertices]

    canvas.delete('all')
    draw_mesh(vertices, edges)

    root.after(10, animate)


root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

animate()
root.mainloop()