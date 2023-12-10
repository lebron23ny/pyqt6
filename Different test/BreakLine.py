
from PyQt6.QtWidgets import QFrame
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QCursor

class BreakLineV(QFrame):
    def __init__(self):
        super().__init__()
        #self.setMouseTracking(True)
        self.setFixedWidth(25)
        self.setStyleSheet('background-color:gray')





class BreakLineH(QFrame):
    def __init__(self, layout_widget):
        super().__init__()
        #self.setMouseTracking(True)
        self.setFixedHeight(5)
        self.setStyleSheet('background-color:gray')
        self.initial_pos = None
        self.layout_widget = layout_widget


    def mousePressEvent(self, event):
        self.setCursor(QCursor(Qt.CursorShape.SizeVerCursor))
        if event.button() == Qt.MouseButton.LeftButton:
            self.initial_pos = event.position().toPoint()
        super().mousePressEvent(event)
        event.accept()

    def mouseMoveEvent(self, event):

        #self.setCursor(QCursor(Qt.CursorShape.SizeVerCursor))
        self.setCursor(QCursor(Qt.CursorShape.SplitVCursor))



        if self.initial_pos is not None:
            index = self.layout_widget.indexOf(self)
            widget_top = self.layout_widget.itemAt(index - 1).widget()
            widget_bottom = self.layout_widget.itemAt(index + 1).widget()

            height_window = self.window().height()
            width_window = self.window().width()

            height_top_widget = widget_top.height()
            height_bottom_widget = widget_bottom.height()
            delta = event.position().toPoint() - self.initial_pos
            delta_x = delta.x()
            delta_y = delta.y()
            height_top_widget_new = height_top_widget + delta_y
            height_bottom_widget_new = height_bottom_widget - delta_y

            if (height_top_widget_new <= 5) or (height_bottom_widget_new <= 5):
                return


            widget_bottom.setFixedHeight(height_bottom_widget_new)
            widget_top.setFixedHeight(height_top_widget_new)

            # widget_bottom.setMinimumHeight(height_bottom_widget_new)
            # widget_top.setMinimumHeight(height_top_widget_new)

            # widget_bottom.resize(width_bottom_widget, height_bottom_widget_new )
            # widget_top.resize(width_top_widget, height_top_widget_new)
            #
            self.window().resize(QSize(width_window, height_window))
            print(delta_y)


            # self.window().move(
            #     self.x(),
            #     self.y() + delta.y()
            #                     )
        self.mouseMoveEvent(event)
        event.accept()

    def mouseReleaseEvent(self, event):
        self.setCursor(QCursor(Qt.CursorShape.SplitVCursor))
        self.initial_pos = None
        super().mouseReleaseEvent(event)
        event.accept()
