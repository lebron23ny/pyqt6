#https://zeemarquez.github.io/posts/en/fem/index.html
import numpy as np
from math import *

import pygmsh
import gmsh

gmsh.initialize()
rect_width, rect_length  = 3.0, 10.0
resolution = 0.1
geom = pygmsh.geo.Geometry()
circle = geom.add_circle([5,1.5,0], radius=0.5, mesh_size=resolution*0.5, make_surface=False)

rect = geom.add_polygon(
    [
        [0.0, 0.0, 0],
        [0.0, rect_width, 0],
        [rect_length, rect_width, 0],
        [rect_length, 0.0, 0],
    ],
    mesh_size=resolution, holes=[circle]

)

mesh = geom.generate_mesh(dim=2)
geom.__exit__()