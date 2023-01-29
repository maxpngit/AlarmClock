from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QDialog, QPushButton
from PyQt5.QtWidgets import QLabel
from dbwork import AlarmData


# Диалоговое окно при срабатывании будильника:
# выключили один будильник - ждём следующего
# (если, конечно, он был установлен)
class WakeUp(QDialog):
    def __init__(self, *args):
        super().__init__()
        self.resize(400, 300)
        self.setWindowTitle('Выключи меня')
        self.setWindowIcon(QIcon('images/alarm_off.png'))
        self.timelab = QLabel(self)
        self.timelab.setGeometry(20, 30, 360, 60)
        self.timelab.setFont(QFont("Times", 50, QFont.Bold))
        self.timelab.setAlignment(Qt.AlignCenter)
        self.namelab = QLabel(self)
        self.namelab.setGeometry(20, 110, 360, 60)
        self.namelab.setFont(QFont("Times", 20, QFont.Bold))
        self.namelab.setWordWrap(True)
        self.namelab.setAlignment(Qt.AlignCenter)
        self.upbutton = QPushButton('Я проснулся', self)
        self.upbutton.setGeometry(15, 190, 370, 100)
        self.upbutton.setFont(QFont("Times", 25, QFont.Bold))
        self.db = AlarmData()  # подключился
        time = args[1]
        name = self.db.get_alarmname(time)
        self.timelab.setText(time)
        self.namelab.setText(name[0])
        self.upbutton.clicked.connect(self.wake)

    def wake(self):
        self.close()
