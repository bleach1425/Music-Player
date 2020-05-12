from PySide2 import QtWidgets, QtGui, QtCore, QtMultimedia
import os


class Music_Plyer(QtWidgets.QWidget):
    def __init__(self, widght , icon , label, list, font, button, a):
        super().__init__(self)
        self.widght = QtWidgets.QWidget()
        self.widght.show()
        self.setWindowTitle("GGBOX")
        self.setGeometry(100, 50, 720, 480)

        self.icon_play = QtGui.QIcon("./play.jpg")
        self.icon_stop = QtGui.QIcon("./stop.jpg")
        self.icon_pause = QtGui.QIcon("./pause.jpg")
        self.icon = QtGui.QIcon("./youtube.png")
        self.setWindowIcon(self.icon)

        self.pixmap = QtGui.QPixmap("./1.jpg")
        self.label = QtWidgets.QLabel()
        self.setParent(self.widght)
        self.setPixmap(self.pixmap.scaled(720, 480))
        self.show()

        self.a = os.listdir("C:/Users/PC/Desktop/1090401/music")
        self.list = QtWidgets.QListWidget()
        self.flist.setParent(self.widght)
        self.list.setGeometry(75, 45, 550, 360)
        for b in a:
            self.list.addItem(f"{b}")

        self.font = QtGui.QFont()
        self.font.setPointSize(16)
        self.label.setFont(self.font)
        self.list.show()

        # 播放按鈕
        self.button = QtWidgets.QPushButton("")
        self.button.setParent(self.widght)
        self.button.setIcon(self.icon_play)
        self.button.setIconSize(QtCore.QSize(50, 35))
        self.utton.setGeometry(170, 420, 40, 40)
        self.button.clicked.connect(play_music)
        self.button.show()

        # 暫停按鈕
        my_button = QtWidgets.QPushButton("")
        my_button.setParent(self.widght)
        my_button.setIcon(self.button_icon_pause)
        my_button.setIconSize(QtCore.QSize(50, 35))
        my_button.setGeometry(320, 420, 40, 40)
        my_button.clicked.connect(play_and_end_music)
        my_button.show()

player = QtMultimedia.QMediaPlayer()
a = os.listdir("C:/Users/PC/Desktop/1090401/music")


def play_music(Music_Player):
    x = self.list.selectedItems()
    media = QtCore.QUrl.fromLocalFile(f"./music/{x[0].text()}")
    content = QtMultimedia.QMediaContent(media)
    player.setMedia(content)
    player.play()


# # 停止
# def end_music(play_music):
#     player.stop()

# 播放|暫停
count = 1


def play_and_end_music(play_music):
    global count
    if count % 2 == 1:
        player.pause()
    else:
        player.play()
    count += 1
