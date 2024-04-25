import sys

from PyQt5.QtGui import QIcon, QPixmap, QKeyEvent
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QGridLayout
from PyQt5.QtCore import QThread, pyqtSignal, Qt

from services import capturer, search

class GoogleSearchThread(QThread):
    searchFinished = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        search.google_image()
        self.searchFinished.emit()

class ScreenshotToSearch(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setWindowTitle("Screenshot to Search")
        self.setWindowIcon(QIcon("../assets/logo.ico"))
        self.setStyleSheet("background-color: #121212; color: white; font-size: 16px; border-radius: 25px; padding: 16px;")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QGridLayout(central_widget)

        logo_label = QLabel()
        logo_pixmap = QPixmap("../assets/logo.png")
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo_label, 0, 0, 1, 2)

        self.label = QLabel("Please wait while we do our magic... :)")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label, 1, 0, 1, 2)

        self.capture()

    def capture(self):
        self.capturer = capturer.Capture(self)
        self.capturer.show()

        self.search_thread = GoogleSearchThread()
        self.capturer.imageCaptured.connect(self.start_search_thread)
    
    def start_search_thread(self):
        self.search_thread.start()
        self.search_thread.searchFinished.connect(self.close_application)

    def close_application(self):
        QApplication.quit()

def main():
    app = QApplication(sys.argv)

    ScreenshotToSearch()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()
