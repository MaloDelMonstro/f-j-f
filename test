from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                             QLabel, QSpinBox, QGroupBox, QFileDialog)
from PyQt6.QtCore import Qt


class CircleGeneratorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Генератор Случайных Окружностей")
        self.setMinimumSize(400, 300)

        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        settings_group = QGroupBox("Параметры генерации")
        settings_layout = QVBoxLayout()

        count_layout = QHBoxLayout()
        count_label = QLabel("Количество окружностей:")
        self.spin_count = QSpinBox()
        self.spin_count.setRange(1, 1000)
        self.spin_count.setValue(50)
        count_layout.addWidget(count_label)
        count_layout.addWidget(self.spin_count)
        count_layout.addStretch()

        settings_layout.addLayout(count_layout)
        settings_group.setLayout(settings_layout)
        main_layout.addWidget(settings_group)

        actions_group = QGroupBox("Действия")
        actions_layout = QVBoxLayout()

        self.btn_choose_dir = QPushButton("📁 Выбрать папку для сохранения")
        self.btn_choose_dir.clicked.connect(self.choose_directory)
        actions_layout.addWidget(self.btn_choose_dir)

        self.lbl_path = QLabel("Папка не выбрана")
        self.lbl_path.setWordWrap(True)
        self.lbl_path.setStyleSheet("color: #888; font-style: italic;")
        actions_layout.addWidget(self.lbl_path)

        self.btn_generate = QPushButton("🎨 Сгенерировать и Сохранить")
        self.btn_generate.setEnabled(False)
        self.btn_generate.clicked.connect(self.on_generate_clicked)
        self.btn_generate.setStyleSheet("font-weight: bold; padding: 5px;")
        actions_layout.addWidget(self.btn_generate)

        actions_group.setLayout(actions_layout)
        main_layout.addWidget(actions_group)

        self.lbl_status = QLabel("Готов к работе")
        self.lbl_status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.lbl_status)

        self.setLayout(main_layout)

        self.target_directory = None

    def choose_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Выберите папку для сохранения")
        if directory:
            self.target_directory = directory
            self.lbl_path.setText(directory)
            self.lbl_path.setStyleSheet("color: #00ff41; font-weight: bold;")
            self.btn_generate.setEnabled(True)
            self.lbl_status.setText("Папка выбрана. Можно генерировать.")

    def on_generate_clicked(self):
        pass

    def get_count(self) -> int:
        return self.spin_count.value()

    def set_status(self, text: str):
        self.lbl_status.setText(text)
