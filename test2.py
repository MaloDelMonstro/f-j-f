import sys
import os
import random

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import QThread, pyqtSignal, Qt
from PyQt6.QtGui import QImage, QPainter, QColor

from test import CircleGeneratorUI


class ImageGeneratorWorker(QThread):
    finished = pyqtSignal(str)
    error = pyqtSignal(str)
    progress = pyqtSignal(int)

    def __init__(self, output_dir: str, count: int):
        super().__init__()
        self.output_dir = output_dir
        self.count = count

    def run(self):
        try:

            width, height = 1920, 1080
            image = QImage(width, height, QImage.Format.Format_RGB32)
            image.fill(QColor(0, 0, 0))

            painter = QPainter(image)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)

            for i in range(self.count):
                radius = random.randint(10, 100)

                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                color = QColor(r, g, b)

                x = random.randint(radius, width - radius)
                y = random.randint(radius, height - radius)

                painter.setBrush(color)
                painter.setPen(Qt.PenStyle.NoPen)

                painter.drawEllipse(x, y, radius, radius)

                self.progress.emit(int((i / self.count) * 100))

            painter.end()

            filename = f"random_circles_{self.count}.png"
            filepath = os.path.join(self.output_dir, filename)

            if image.save(filepath):
                self.finished.emit(filepath)
            else:
                raise IOError("Не удалось сохранить изображение")

        except Exception as e:
            self.error.emit(str(e))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = CircleGeneratorUI()
        self.setCentralWidget(self.ui)

        self.ui.btn_generate.clicked.connect(self.start_generation)

        self.worker = None

    def start_generation(self):
        if not self.ui.target_directory:
            QMessageBox.warning(self, "Ошибка", "Сначала выберите папку!")
            return

        count = self.ui.get_count()
        self.ui.set_status(f"Генерация {count} окружностей...")
        self.ui.btn_generate.setEnabled(False)

        self.worker = ImageGeneratorWorker(self.ui.target_directory, count)
        self.worker.finished.connect(self.on_generation_finished)
        self.worker.error.connect(self.on_generation_error)
        self.worker.start()

    def on_generation_finished(self, filepath):
        self.ui.set_status(f"Готово! Файл сохранен: {os.path.basename(filepath)}")
        self.ui.btn_generate.setEnabled(True)
        QMessageBox.information(self, "Успех", f"Изображение успешно создано:\n{filepath}")

    def on_generation_error(self, error_msg):
        self.ui.set_status("Ошибка генерации")
        self.ui.btn_generate.setEnabled(True)
        QMessageBox.critical(self, "Ошибка", f"Произошла ошибка:\n{error_msg}")


def main():
    app = QApplication(sys.argv)

    font = app.font()
    font.setPointSize(10)
    app.setFont(font)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()