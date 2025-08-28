import sys
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTextEdit, QLabel, QFileDialog, QLineEdit, QMessageBox, QGroupBox
)
from PySide6.QtGui import QGuiApplication
from PySide6.QtGui import QFont
from PySide6.QtCore import QRect
from caesar import caesar_encrypt, caesar_decrypt, caesar_bruteforce

class CaesarGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Caesar Cipher Tool")
        self.setGeometry(300, 200, 700, 500)
        self.center_on_screen()

    def center_on_screen(self):
        screen_geometry: QRect = QGuiApplication.primaryScreen().availableGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)    


        #Main layout
        layout = QVBoxLayout()

        #Title
        title = QLabel("Caesar Cipher Encryption Tool")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        layout.addWidget(title)

        #Input Section
        input_group = QGroupBox("Input Text")
        input_group.setStyleSheet("QGroupBox { font: bold 12pt 'Arial'; }")
        input_layout = QVBoxLayout()
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Enter text here...")
        input_layout.addWidget(self.input_text)
        input_group.setLayout(input_layout)
        layout.addWidget(input_group)

        #Shift section
        shift_group = QGroupBox("Shift")
        shift_group.setStyleSheet("QGroupBox { font: bold 12pt 'Arial'; }")
        shift_layout = QHBoxLayout()
        self.shift_input = QLineEdit("3")
        self.shift_input.setFixedWidth(60)
        shift_layout.addWidget(QLabel("Shift By: "))
        shift_layout.addWidget(self.shift_input)
        shift_layout.addStretch()
        shift_group.setLayout(shift_layout)
        layout.addWidget(shift_group)

        # Buttons Section
        btn_group = QGroupBox("Actions")
        btn_group.setStyleSheet("QGroupBox { font: bold 12pt 'Arial'; }")
        btn_layout = QHBoxLayout()
        self.encrypt_btn = QPushButton("Encrypt")
        self.decrypt_btn = QPushButton("Decrypt")
        self.bruteforce_btn = QPushButton("Bruteforce")
        self.load_btn = QPushButton("Load File")
        self.save_btn = QPushButton("Save File")
        for btn in [self.encrypt_btn, self.decrypt_btn, self.bruteforce_btn, self.load_btn, self.save_btn]:
            btn.setMinimumHeight(35)
            btn_layout.addWidget(btn)
        btn_group.setLayout(btn_layout)
        layout.addWidget(btn_group)

       # Output Section
        output_group = QGroupBox("Output")
        output_group.setStyleSheet("QGroupBox { font: bold 12pt 'Arial'; }")
        output_layout = QVBoxLayout()
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setPlaceholderText("Your encrypted/decrypted text will appear here...")
        output_layout.addWidget(self.output_text)
        output_group.setLayout(output_layout)
        layout.addWidget(output_group)

        self.setLayout(layout)

        # Connect buttons
        self.encrypt_btn.clicked.connect(self.encrypt_text)
        self.decrypt_btn.clicked.connect(self.decrypt_text)
        self.bruteforce_btn.clicked.connect(self.bruteforce_text)
        self.load_btn.clicked.connect(self.load_file)
        self.save_btn.clicked.connect(self.save_file)

    def get_shift(self) -> int:
        try:
            value = int(self.shift_input.text())
            if 1 <= value <= 26:
                return value
            else:
                QMessageBox.warning(self,"Invalid Shift", "Shift must be between 1 and 26")
                self.shift_input.setText("3")
                return 3
        except ValueError:
            QMessageBox.warning(self, "Error", "Shift must be an integer")
            self.shift_input.setText("3")
            return 3

    def encrypt_text(self):
        shift = self.get_shift()
        text = self.input_text.toPlainText()
        result = caesar_encrypt(text, shift)
        self.output_text.setPlainText(result)

    def decrypt_text(self):
        shift = self.get_shift()
        text = self.input_text.toPlainText()
        result = caesar_decrypt(text, shift)
        self.output_text.setPlainText(result)

    def bruteforce_text(self):
        text = self.input_text.toPlainText()
        results = caesar_bruteforce(text)
        formatted = "\n".join([f"Shift {s:2}: {t}" for s, t in results.items()])
        self.output_text.setPlainText(formatted)

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Text File", "", "Text Files (*.txt)")
        if file_path:
            content = Path(file_path).read_text(encoding="utf-8")
            self.input_text.setPlainText(content)

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Output File", "", "Text Files (*.txt)")
        if file_path:
            Path(file_path).write_text(self.output_text.toPlainText(), encoding="utf-8")
            QMessageBox.information(self, "Saved", f"✅ Output saved to {file_path}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CaesarGUI()
    window.show()
    sys.exit(app.exec())