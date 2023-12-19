#https://www.pythonguis.com/tutorials/pyqt6-qml-qtquick-python-application/
import sys
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from time import strftime, localtime
from PyQt6.QtCore import QTimer, QObject, pyqtSignal
from PySide6.QtCore import Signal

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)

engine.load('main.qml')

class Backend(QObject):

    updated = pyqtSignal(str, arguments=['time'])

    hms = pyqtSignal(int, int, int, arguments=['hours, minutes', 'seconds'])

    def __init__(self):
        super().__init__()

        # Define timer.
        self.timer = QTimer()
        self.timer.setInterval(100)  # msecs 100 = 1/10th sec
        self.timer.timeout.connect(self.update_time)
        self.timer.start()

    def update_time(self):
        # Pass the current time to QML.
        local_time = localtime()
        curr_time = strftime("%H:%M:%S", local_time)
        self.updated.emit(curr_time)
        self.hms.emit(local_time.tm_hour, local_time.tm_min, local_time.tm_sec)


# Define our backend object, which we pass to QML.
backend = Backend()

engine.rootObjects()[0].setProperty('backend', backend)

# Initial call to trigger first update. Must be after the setProperty to connect signals.
backend.update_time()

sys.exit(app.exec())