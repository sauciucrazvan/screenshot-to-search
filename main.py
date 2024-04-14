import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QVBoxLayout,
    QFrame,
    QPushButton,
)

from PyQt5.QtCore import Qt

from search import *
from capturer import Capture

class ScreenRegionSelector(QMainWindow):
    
    def __init__(self,):
        super().__init__(None)
        self.m_width = 300
        self.m_height = 100

        self.setWindowTitle("Screenshot To Search")
        self.setMinimumSize(self.m_width, self.m_height)

        frame = QFrame()
        frame.setContentsMargins(0, 0, 0, 0)
        lay = QVBoxLayout(frame)
        lay.setAlignment(Qt.AlignmentFlag.AlignTop)
        lay.setContentsMargins(5, 5, 5, 5)

        self.label = QLabel()
        self.btn_capture = QPushButton("Capture")
        self.btn_capture.clicked.connect(self.capture)

        lay.addWidget(self.label)
        lay.addWidget(self.btn_capture)

        self.setCentralWidget(frame)

    def capture(self):
        self.capturer = Capture(self)
        self.capturer.imageCaptured.connect(searchImage)
        self.capturer.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)    
    app.setStyleSheet("""
    QFrame {
        background-color: #121212;
        padding-right: 20px;
        padding-left: 20px;
    }
                      
    QPushButton {
        border-radius: 12px;
        background-color: #00A170;
        padding: 10px;
        color: white;
        font-weight: bold;
        font-family: Arial;
        font-size: 12px;
    }
                      
    QPushButton::hover {
        background-color: #008059
    }
    """)
    selector = ScreenRegionSelector()

    desktop = QApplication.desktop()
    desktop_rect = desktop.availableGeometry()
    selector.move(desktop_rect.width() - selector.width(), desktop_rect.height() - selector.height())

    selector.show()
    app.exit(app.exec_())