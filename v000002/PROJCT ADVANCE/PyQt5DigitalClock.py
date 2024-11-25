from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase
import sys

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.startClock()

    def initUI(self):
        # Set up the main window
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)
        self.setStyleSheet("background-color: black;")

        # Create and configure the time label
        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignCenter)
        
        self.time_label.setStyleSheet("font-size: 150px; color: #26ff00;")
        font_id = QFontDatabase.addApplicationFont("v000002/PROJCT ADVANCE/DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)

        self.time_label.setFont(my_font)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.time_label)
        self.setLayout(layout)

    def startClock(self):
        # Create a timer to update the clock every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)  # Update every second
        self.updateTime()  # Initialize the time display

    def updateTime(self):
        # Get the current time and update the label
        current_time = QTime.currentTime()
        self.time_label.setText(current_time.toString("hh:mm:ss"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())