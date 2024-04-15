import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal

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
        super().__init__(None)
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
        sys.exit()

def main():
    app = QApplication(sys.argv)

    app.setApplicationDisplayName("Screenshot to Search")
    app.setWindowIcon(QIcon("./assets/logo.ico"))

    sts = ScreenshotToSearch()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
