from PyQt5.QtWidgets import QMessageBox, QDialog
from dbwork import AlarmData
from uiforms.editor import Ui_Editor
from misc import *


# Диалог редактирования существующего будильника
# Возможны: смена названия и мелодии (время не меняется)
class Reader(QDialog, Ui_Editor):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)

        self.db = AlarmData()  # подключился к DB

        self.time = args[1]
        self.label.setText(self.label.text() + " " + str(self.time))
        curname = self.db.get_alarmname(args[1])
        self.NameLine.setText(curname[0] + '2')
        res = self.db.get_music()

        for item in res:
            self.MusicList.addItem(f'{item[0]}')

        self.Save.clicked.connect(self.save)
        self.MusicList.itemClicked.connect(self.musicClick)

        self.name_exist = False
        self.music_click = False

    def save(self):
        names = self.db.get_alarmnames()
        self.newname = remove_illegal(self.NameLine.text())
        self.NameLine.setText(self.newname)
        for index in names:
            if self.newname == index[0]:
                self.name_exist = True

        if self.music_click == True:
            self.newmusic = self.musicnum
            if self.name_exist == False:
                self.result = self.db.update(self.time, self.newname, self.newmusic)
                if self.result:
                    QMessageBox.about(self, "Всё хорошо", "Данные записались!")
                    self.close()
                else:
                    QMessageBox.about(self, "Всё плохо", "Данные не записались!")
            else:
                QMessageBox.about(self, "Ошибка!", "У вас уже есть будильник с таким именем!")
        else:
            QMessageBox.about(self, "Ошибка!", "Выберите песню!")

    def musicClick(self, item):
        self.music_click = True
        self.musicname = item.text()
        self.musicnum = 0

        for i in range(0, self.MusicList.count()):
            if self.musicname == self.MusicList.item(i).text():
                self.musicnum = i + 1
