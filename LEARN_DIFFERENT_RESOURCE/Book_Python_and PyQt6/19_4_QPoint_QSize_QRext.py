from PyQt6.QtCore import QPoint, QSize, QRect, QRectF

point = QPoint(10, 10)

x = point.x()
y = point.y()

print(x, y)
print()
size = QSize()
size2 = QSize(10, 50)
print(size)
print(size2)

size.setHeight(10)
print(size)
print()

rect1 = QRect()
print(rect1.height())
print(rect1)
rect1.setLeft(10)
rect1.setTop(55)
print(rect1)

rect1.setTopLeft(QPoint(10, 50))
rect1.setBottomRight(QPoint(0, 120))
print(rect1)
rect1.setWidth(100)
rect1.setHeight(50)
print(rect1)

rect1.setCoords(12, 50, 92, 60)
print(rect1)


