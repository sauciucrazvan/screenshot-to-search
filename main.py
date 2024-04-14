import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QVBoxLayout,
    QGridLayout,
    QFrame,
    QPushButton,
)

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap, QRegion

from services import search, capturer

class ScreenRegionSelector(QMainWindow):
    
    def __init__(self,):
        super().__init__(None)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Screenshot To Search")
        self.setFixedSize(300, 200)

        frame = QFrame()
        frame.setContentsMargins(0, 0, 0, 0)
        lay = QVBoxLayout(frame)
        lay.setAlignment(Qt.AlignmentFlag.AlignTop)
        lay.setContentsMargins(5, 5, 5, 5)

        buttons_layout = QGridLayout()

        self.label = QLabel()
        self.btn_capture = QPushButton("📸")
        self.btn_capture.clicked.connect(self.capture)
        self.btn_close = QPushButton("❌")
        self.btn_close.clicked.connect(self.close)
        
        appLogo = QPixmap("assets/logo.png")
        self.label.setPixmap(appLogo)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        lay.addSpacing(20)
        lay.addWidget(self.label)
        lay.addSpacing(20)

        buttons_layout.addWidget(self.btn_capture, 0, 0)
        buttons_layout.addWidget(self.btn_close, 0, 1)
        buttons_layout.setHorizontalSpacing(10)

        lay.addLayout(buttons_layout)
        lay.addSpacing(20)

        self.setCentralWidget(frame)

    def capture(self):
        self.capturer = capturer.Capture(self)
        self.capturer.imageCaptured.connect(search.searchImage)
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
        background-color: #222222;
        padding: 10px;
        color: white;
        font-size: 24px;
        font-weight: bold;
        font-family: Arial;
        text-align: center;
    }
                      
    QPushButton::hover {
        background-color: #333333;
    }
    """)
    selector = ScreenRegionSelector()

    desktop = QApplication.desktop()
    desktop_rect = desktop.availableGeometry()
    selector.move(desktop_rect.width() - selector.width(), desktop_rect.height() - selector.height())

    selector.show()
    app.exit(app.exec_())
