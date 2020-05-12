from PySide2 import QtWidgets, QtGui, QtCore, QtMultimedia
import os
import sys
import phonon

# 設定程式
app = QtWidgets.QApplication()

# 設定player套件
player = QtMultimedia.QMediaPlayer()

# 設定畫布
my_widght = QtWidgets.QWidget()
my_widght.show()
my_widght.setWindowTitle("GGBOX")
my_widght.setGeometry(100, 50, 720, 480)

# 設定ICON
my_button_icon_play = QtGui.QIcon("./play.jpg")
my_button_icon_stop = QtGui.QIcon("./stop.jpg")
my_button_icon_pause = QtGui.QIcon("./pause.jpg")
my_button_icon_next = QtGui.QIcon("./next_song.jpg")
my_button_icon_last = QtGui.QIcon("./last_song.jpg")
my_icon = QtGui.QIcon("./youtube.png") 
my_widght.setWindowIcon(my_icon)

# 放入圖片
my_pixmap = QtGui.QPixmap("./1.jpg")
my_label = QtWidgets.QLabel()
my_label.setParent(my_widght)
my_label.setPixmap(my_pixmap.scaled(720,480))
my_label.show()

# 找到音樂的檔案,用迴圈放進清單
a = os.listdir("C:/Users/PC/Desktop/1090401/music")
my_list = QtWidgets.QListWidget()
my_list.setParent(my_widght)
my_list.setGeometry(75, 45, 550, 360)
for i, b in enumerate(a):
    my_list.addItem(f"{b}")
# 設定字體
my_font = QtGui.QFont()
my_font.setPointSize(16)
my_label.setFont(my_font)
my_list.show()
# 播放器時間設定
# time = QtCore.QTimer()
# time.setInterval(1000)
# time.connect(time.check_music)

def play_music():
    x = my_list.selectedItems()
    media = QtCore.QUrl.fromLocalFile(f"./music/{x[0].text()}")
    content = QtMultimedia.QMediaContent(media)
    player.setMedia(content)
    player.play()

# 播放|暫停
count = 1
def play_and_end_music():
    global count
    if count%2 == 1:
        player.pause()
    else:
        player.play()
    count += 1
# 下一首
time = QtCore.QTimer()
time.setInterval(1000)
def next_music(self):
    player_status = self.player.mediaStatus()
    player_duration = self.player.duration()
    print("音樂時間: ", player_duration)
    print("播放狀態: ", player_status)
    if player_status == 7:
        self.next_music()
    if player_status > 0:
        self.duration = player_duration

# 播放按鈕
my_button = QtWidgets.QPushButton("")
my_button.setParent(my_widght)
my_button.setIcon(my_button_icon_play)
my_button.setIconSize(QtCore.QSize(50,35))
my_button.setGeometry(170, 420, 40, 40)
my_button.clicked.connect(play_music)
my_button.show()

# 暫停按鈕
my_button = QtWidgets.QPushButton("")
my_button.setParent(my_widght)
my_button.setIcon(my_button_icon_pause)
my_button.setIconSize(QtCore.QSize(50,35))
my_button.setGeometry(320, 420, 40, 40)
my_button.clicked.connect(play_and_end_music)
my_button.show()

# 下一首按鈕
my_button = QtWidgets.QPushButton("")
my_button.setParent(my_widght)
my_button.setIcon(my_button_icon_next)
my_button.setIconSize(QtCore.QSize(50, 35))
my_button.setGeometry(230,420,40,40)
my_button.clicked.connect(next_music)
my_button.show()

sys.exit(app.exec_())









# # 設置播放進度條
# schedule_row = QtWidgets.QProgressBar()
# schedule_row.setValue(49)
# schedule_row.setFixedHeight(3) # 進度條高度
# schedule_row.setTextVisible(False)      # 不要顯示進度條的文字

# # 播放控制用套件
# schedule_control = QtWidgets.QWidget()
# schedule_control_a =QtWidgets.QGridLayout()  # 播放控制套件網格布局
# schedule_control.setLayout(schedule_control_a)

# quick_button = QtWidgets.QPushButton(qtawesome.icon("./quick_button.jpg",color="#F76677",""))
# back_button = QtWidgets.QPushButton(qtawesome.icon("./back_button.jpg",color="#F76677",""))
# back_button.setIconSize(QtCore.QSize(30,30))
# quick_button.setIconSize(QtCore.QSize(30,30))

# schedule_control_a.addWidget(quick_button,0,0)
# schedule_control_a.addWidget(back_button,0,0)
# schedule_control_a.setAlignment(QtCore.Qt.AlignCenter) # 設置布局內部居中顯示
