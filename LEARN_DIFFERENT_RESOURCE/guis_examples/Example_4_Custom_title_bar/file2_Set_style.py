from PyQt6.QtCore import QSize, Qt, QEvent
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QFrame, QPushButton
)


from My_custom_widget import CustomTittleBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Custom Title Bar')
        self.resize(400, 200)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet("background-color: gray; border-radius: 20px;")

        central_widget = QWidget()

        central_widget.setObjectName('Container')
        central_widget.setStyleSheet("""#Container {
                    background: qlineargradient(x1:0 y1:0, x2:1 y2:1, stop:0 #051c2a stop:1 #44315f);
                    border-radius: 25px;
                }""")
        self.title_bar = CustomTittleBar(self)

        work_space_layout = QVBoxLayout()
        work_space_layout.setContentsMargins(11, 11, 11, 11)

        centra_widget_layout = QVBoxLayout()
        centra_widget_layout.setContentsMargins(0, 0, 0, 0)
        centra_widget_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        centra_widget_layout.addWidget(self.title_bar)
        centra_widget_layout.addLayout(work_space_layout)

        button = QPushButton('Кнопка')
        centra_widget_layout.addWidget(button)

        central_widget.setLayout(centra_widget_layout)
        self.setCentralWidget(central_widget)

    def changeEvent(self, event): #Событие происходит когда нажимают кнопку управления или программно делают окно
        #minimized, maximized or full-screen
        if event.type() == QEvent.Type.WindowStateChange:
            self.title_bar.window_state_changed(self.windowState())
        super().changeEvent(event)
        event.accept()








if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
