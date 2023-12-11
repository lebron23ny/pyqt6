from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPalette
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QStyle,
    QToolButton,
    QVBoxLayout,
    QWidget,
    QPushButton, QFrame
)

class MyCustomTittleBar1(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        #self.setAutoFillBackground(True)
        #self.setBackgroundRole(QPalette.ColorRole.Highlight)
        self.initial_pos = None

        self.setFixedHeight(40)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(main_layout)
        frame = QFrame()
        frame.setObjectName('TittleBarFrame')
        frame.setStyleSheet(
            'border: 2px solid black;'
            #'background-color:red;'
        )

        main_layout.addWidget(frame)




        title_bar_layout = QHBoxLayout(self)
        title_bar_layout.setContentsMargins(5, 0, 8, 0)
        title_bar_layout.setSpacing(2)

        frame.setLayout(title_bar_layout)

        self.title = QLabel(f"{self.__class__.__name__}", self)

        self.title.setStyleSheet(
                'color: black;'
                'font-size:16pt;'
                'border: 2px solid black;'
                'background-color:red;'
                'font-weight: bold;'
                'padding-left:10px;'
        )

        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if title := parent.windowTitle():
            self.title.setText(title)


        self.title.setFixedHeight(30)

        title_bar_layout.addWidget(self.title)

        self.close_button = QPushButton(self)
        close_icon = self.style().standardIcon(
            QStyle.StandardPixmap.SP_TitleBarCloseButton
        )
        self.close_button.setIcon(close_icon)

        self.close_button.setFixedHeight(30)
        self.close_button.setFixedWidth(30)
        self.close_button.clicked.connect(self.window().close)

        self.close_button.setStyleSheet(
            'QPushButton'
            '{'
            'text-align: center;'
            'color:white;'
            'font-size:15pt;'
            'font-weight:bold;'
            'background-color:red;'
            'border: 2px solid black;'
            'border-radius:5px;'
            'width:230px;'
            'height:50px;'
            

            '}'
            'QPushButton:hover'
            '{'
            'background-color:blue;'
            '}'
            'QPushButton:pressed'
            '{'
            'background-color:green;'
            '}'


        )
        title_bar_layout.addWidget(self.close_button)



    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.initial_pos = event.position().toPoint()
        super().mousePressEvent(event)
        event.accept()

    def mouseMoveEvent(self, event):
        if self.initial_pos is not None:
            delta = event.position().toPoint() - self.initial_pos
            self.window().move(
                self.window().x() + delta.x(),
                self.window().y() + delta.y()
                                )
        super().mouseMoveEvent(event)
        event.accept()

    def mouseReleaseEvent(self, event):
        self.initial_pos = None
        super().mouseReleaseEvent(event)
        event.accept()
