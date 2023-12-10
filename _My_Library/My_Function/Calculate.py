
def isNumberValue(text):
    """

    :param text:
    :return: True if text is number (float, int)
    """
    try:
        float(text)
        res = True
    except:
        print("Not a float")
        res = False
    return res

def linInter2D(x1, y1, x2, y2, x):
    """

    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :param x:
    :return:Returns the interpolated value Y corresponding X between (x1, y1) and (x2, y2)
    :rtype: float
    """
    y = y1 + (x - x1) * (y2 - y1) / (x2 - x1)
    return y


def linInterp3D(x1, y1, x2, y2, z11, z21, z12, z22, x, y):
    """

    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :param z11:
    :param z21:
    :param z12:
    :param z22:
    :param x:
    :param y:
    :return: Returns the interpolated value Z corresponding to the point(x,y) between points
    (x1, y1, z11), (x1, y2, z12), (x2, y1, z21) and (x2, y2, z22)
    :rtype: float
    """
    z1 = z11 + (z12 - z11) * (y - y1) / (y2 - y1)
    z2 = z21 + (z22 - z21) * (y - y1) / (y2 - y1)
    z = z1 + (z2 - z1) * (x - x1) / (x2 - x1)
    return z



def findZ(listX, listY, listZ, x, y):
    """

    :param listX:
    :param listY:
    :param listZ:
    :param x:
    :param y:
    :return: returns the interpolated z value corresponding to x and y
    :rtype: float
    """
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    z11 = 0
    z21 = 0
    z12 = 0
    z22 = 0

    x1i = 0
    y1i = 0
    x2i = 0
    y2i = 0

    x_inside_range = False
    y_inside_range = False

    for i in range(len(listX) - 1):
        if x == listX[i]:
            x1 = x2 = listX[i]
            x1i = x2i = i
            x_inside_range = True
            break
        elif (x > listX[i]) and (x < listX[i + 1]):
            x1 = listX[i]
            x1i = i
            x2 = listX[i + 1]
            x2i = i + 1
            x_inside_range = True
            break
        elif x == listX[i + 1]:
            x1 = x2 = listX[i + 1]
            x1i = x2i = i + 1
            x_inside_range = True
            break
    if not x_inside_range:
        return None

    for i in range(len(listY) - 1):
        if y == listY[i]:
            y1 = y2 = listY[i]
            y1i = y2i = i
            y_inside_range = True
            break
        elif (y > listY[i]) and (y < listY[i + 1]):
            y1 = listY[i]
            y1i = i
            y2 = listY[i + 1]
            y2i = i + 1
            y_inside_range = True
            break
        elif y == listY[i + 1]:
            y1 = y2 = listY[i + 1]
            y1i = y2i = i + 1
            y_inside_range = True

    if not y_inside_range:
        return None

    z11 = listZ[y1i][x1i]
    z21 = listZ[y1i][x2i]
    z12 = listZ[y2i][x1i]
    z22 = listZ[y2i][x2i]

    if (x1 == x2) and (y1 == y2):
        return listZ[y1i][x1i]
    elif (x1 == x2) and (y1 != y2):
        return linInter2D(y1, z11, y2, z12, y)
    elif (x1 != x2) and (y1 == y2):
        return linInter2D(x1, z11, x2, z21, x)
    else:
        return linInterp3D(x1, y1, x2, y2, z11, z21, z12, z22, x, y)



listX = [0.1, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 8, 9, 10, 12, 14, 17, 20]
listY = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]

listZ = [
    [967, 922, 850, 782, 722, 669, 620, 577, 538, 469, 417, 370, 337, 307, 280, 260, 237, 222, 210, 183, 164, 150, 125,
     106, 90, 77],
    [925, 854, 778, 711, 653, 600, 563, 520, 484, 427, 382, 341, 307, 283, 259, 240, 225, 209, 196, 175, 157, 142, 121,
     103, 86, 74],
    [875, 804, 716, 647, 593, 548, 507, 470, 439, 388, 347, 312, 283, 262, 240, 223, 207, 195, 182, 163, 148, 134, 114,
     99, 82, 70],
    [813, 742, 653, 587, 536, 496, 457, 425, 397, 352, 315, 286, 260, 240, 222, 206, 193, 182, 170, 153, 138, 125, 107,
     94, 79, 67],
    [742, 672, 587, 526, 480, 442, 410, 383, 357, 317, 287, 262, 238, 220, 204, 190, 178, 168, 158, 144, 130, 118, 101,
     90, 76, 65],
    [667, 597, 520, 465, 425, 395, 365, 342, 320, 287, 260, 238, 217, 202, 187, 175, 166, 156, 147, 135, 123, 112, 97,
     86, 73, 63],
    [587, 522, 455, 408, 375, 350, 325, 303, 287, 258, 233, 216, 198, 183, 172, 162, 153, 145, 137, 125, 115, 106, 92,
     82, 69, 60],
    [505, 447, 394, 356, 330, 309, 289, 270, 256, 232, 212, 197, 181, 168, 158, 149, 140, 135, 127, 118, 108, 98, 88,
     78, 66, 57],
    [418, 382, 342, 310, 288, 272, 257, 242, 229, 208, 192, 178, 165, 155, 146, 137, 130, 125, 118, 110, 101, 93, 83,
     75, 64, 55],
    [354, 326, 295, 273, 253, 239, 225, 215, 205, 188, 175, 162, 150, 143, 135, 126, 120, 117, 111, 103, 95, 88, 79, 72,
     62, 53],
    [302, 280, 256, 240, 224, 212, 200, 192, 184, 170, 158, 148, 138, 132, 124, 117, 112, 108, 104, 95, 89, 84, 75, 69,
     60, 51]
]




