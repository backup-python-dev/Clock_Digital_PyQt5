import style
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout, QLabel
from PyQt5.QtCore import QTimer, QTime, Qt


class Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(690, 280)
        self.setWindowTitle("Reloj digital")
        self.setStyleSheet(style.style)
        grid_layout = QGridLayout()

        self.lbl_hh = QLabel()
        self.lbl_hh.setAlignment(Qt.AlignCenter)
        self.lbl_hh.setObjectName("labelHour")

        self.lbl_mm = QLabel()
        self.lbl_mm.setAlignment(Qt.AlignCenter)
        self.lbl_mm.setObjectName("labelMinute")

        self.lbl_ss = QLabel()
        self.lbl_ss.setAlignment(Qt.AlignCenter)
        self.lbl_ss.setObjectName("labelSecond")

        self.point_1 = QLabel(":")
        self.point_1.setObjectName("labelEmty")
        self.point_1.setAlignment(Qt.AlignCenter)

        self.point_2 = QLabel(":")
        self.point_2.setAlignment(Qt.AlignCenter)
        self.point_2.setObjectName("labelEmty")

        self.type = QLabel()
        self.type.setAlignment(Qt.AlignCenter)
        self.type.setObjectName("labelEmty")

        grid_layout.addWidget(self.lbl_hh, 0, 0)
        grid_layout.addWidget(self.point_1, 0, 1)
        grid_layout.addWidget(self.lbl_mm, 0, 2)
        grid_layout.addWidget(self.point_2, 0, 3)
        grid_layout.addWidget(self.lbl_ss, 0, 4)
        grid_layout.addWidget(self.type, 2, 2)
        self.setLayout(grid_layout)

        #CREAMOS EL 'TIMER'
        timer = QTimer(self)
        timer.timeout.connect(self.displayTime)
        timer.start(1000)

    def displayTime(self):
        currentTime = QTime.currentTime()
        hours = currentTime.toString('hh')
        minutes = currentTime.toString('mm')
        seconds = currentTime.toString('ss')
        meridiem = currentTime.toString('ap')
        self.type.setText(meridiem.upper())
        self.lbl_hh.setText(hours)
        self.lbl_mm.setText(minutes)
        self.lbl_ss.setText(seconds)


#EJECUTAMOS APLICACIÓN.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = Clock()
    clock.show()
    sys.exit(app.exec_())
