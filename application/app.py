import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow

from services import capturer, search

class ScreenshotToSearch(QMainWindow):
    
    def __init__(self):
        super().__init__(None)
        self.capture()

    def capture(self):
        self.capturer = capturer.Capture(self)
        self.capturer.imageCaptured.connect(search.google_image)
        self.capturer.show()

def main():
    app = QApplication(sys.argv)

    app.setApplicationDisplayName("Screenshot to Search")
    app.setWindowIcon(QIcon("./assets/logo.ico"))

    sts = ScreenshotToSearch()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()