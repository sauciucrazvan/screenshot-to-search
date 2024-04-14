import tempfile

from PyQt5.QtCore import Qt, QPoint, QRect, pyqtSignal
from PyQt5.QtWidgets import QWidget, QRubberBand, QApplication
from PyQt5.QtGui import QMouseEvent, QKeyEvent

class Capture(QWidget):
    imageCaptured = pyqtSignal(str)

    def __init__(self, main_window):
        super().__init__()
        self.main = main_window
        self.main.hide()
        
        self.setMouseTracking(True)
        desk_size = QApplication.desktop()
        self.setGeometry(0, 0, desk_size.width(), desk_size.height())
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowOpacity(0.15)

        self.rubber_band = QRubberBand(QRubberBand.Rectangle, self)
        self.origin = QPoint()

        QApplication.setOverrideCursor(Qt.CrossCursor)

    def mousePressEvent(self, event: QMouseEvent | None) -> None:
        if event.button() == Qt.LeftButton:
            self.origin = event.pos()
            self.rubber_band.setGeometry(QRect(self.origin, event.pos()).normalized())
            self.rubber_band.show() 

            screen = QApplication.primaryScreen()
            rect = QApplication.desktop().rect()
            self.imgmap = screen.grabWindow(QApplication.desktop().winId(), rect.x(), rect.y(), rect.width(), rect.height())

    def mouseMoveEvent(self, event: QMouseEvent | None) -> None:
        if not self.origin.isNull():
            self.rubber_band.setGeometry(QRect(self.origin, event.pos()).normalized())

    def mouseReleaseEvent(self, event: QMouseEvent | None) -> None:
        if event.button() == Qt.LeftButton:
            self.rubber_band.hide()
            
            rect = self.rubber_band.geometry()
            self.imgmap = self.imgmap.copy(rect)
            QApplication.restoreOverrideCursor()

            image_path = f"{tempfile.gettempdir()}/screenshot.png"
            self.imgmap.save(image_path)
            self.imageCaptured.emit(image_path)

            self.main.show()
            self.close()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Escape:
            QApplication.restoreOverrideCursor()
            self.main.show()
            self.close()