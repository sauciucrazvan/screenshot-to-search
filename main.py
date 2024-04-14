import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from services import search, capturer

class Application(QMainWindow):
    
    def __init__(self):
        super().__init__(None)
        self.capture()

    def capture(self):
        self.capturer = capturer.Capture(self)
        self.capturer.imageCaptured.connect(search.google_image)
        self.capturer.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)    
    application = Application()
    app.exec_()
