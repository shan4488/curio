import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt
import interface

class LoadingGif(object):

    def mainUI(self, FrontWindow):
        FrontWindow.setObjectName("SJEC")
        FrontWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(FrontWindow)
        self.centralwidget.setObjectName("main-widget")

        # Label Create
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.label.setMinimumSize(QtCore.QSize(800, 480))
        self.label.setMaximumSize(QtCore.QSize(800, 480))
        self.label.setObjectName("lb1")
        FrontWindow.setCentralWidget(self.centralwidget)

        # Loading the GIF
        self.movie = QMovie("sjec_gif.gif")
        self.label.setMovie(self.movie)

        # Start Animation
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.startAnimation)
        self.timer.start(50) # 50 ms

    def startAnimation(self):
        self.movie.start()

    # Stop Animation(According to need)
    # def stopAnimation(self):
    #     self.movie.stop()

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
demo = LoadingGif()
demo.mainUI(window)
window.show()
sys.exit(app.exec_())

