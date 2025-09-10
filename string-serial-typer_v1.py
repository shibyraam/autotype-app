import sys
import time
import string
import keyboard as kb
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QHBoxLayout, QMessageBox
)
from PyQt5.QtCore import QTimer


class SerialTyper(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Serial Number / Alphabet Typer")
        self.setGeometry(200, 200, 400, 150)

        layout = QVBoxLayout()

        # Mode selection
        self.label_mode = QLabel("Choose Mode:")
        self.radio_num = QRadioButton("Serial Number Typer")
        self.radio_alpha = QRadioButton("Alphabet with Ref No. Typer")
        layout.addWidget(self.label_mode)
        layout_h = QHBoxLayout()
        layout_h.addWidget(self.radio_num)
        layout_h.addWidget(self.radio_alpha)
        layout.addLayout(layout_h)

        # Inputs
        self.input1 = QLineEdit()
        self.input1.setPlaceholderText("Start Serial Number (OR) Count for Alphabet mode)")
        layout.addWidget(self.input1)

        self.input2 = QLineEdit()
        self.input2.setPlaceholderText("How many rolls (OR) Supplier Ref No. (Alphabet mode)")
        layout.addWidget(self.input2)

        # Start button
        self.btn_start = QPushButton("Start Typing")
        self.btn_start.clicked.connect(self.start_typing)
        layout.addWidget(self.btn_start)

        self.setLayout(layout)

    def start_typing(self):
        if self.radio_num.isChecked():
            try:
                start_num = int(self.input1.text())
                count = int(self.input2.text())
            except ValueError:
                QMessageBox.warning(self, "Error", "Enter valid numbers!")
                return

            QMessageBox.information(self, "Info", "Switch to Excel/target app. Typing starts in 3 seconds...")
            QTimer.singleShot(3000, lambda: self.type_numbers(start_num, count))

        elif self.radio_alpha.isChecked():
            try:
                count = int(self.input1.text())
            except ValueError:
                QMessageBox.warning(self, "Error", "Enter valid alphabet count!")
                return
            ref = self.input2.text().strip()

            if not ref:
                QMessageBox.warning(self, "Error", "Enter supplier reference!")
                return

            if count > 26:
                QMessageBox.warning(self, "Warning", "Only 26 letters A–Z available! Limiting to 26.")
                count = 26

            QMessageBox.information(self, "Info", "Switch to Excel/target app. Typing starts in 3 seconds...")
            QTimer.singleShot(3000, lambda: self.type_alphabets(count, ref))

        else:
            QMessageBox.warning(self, "Error", "Select a mode!")

    def type_numbers(self, start, count):
        for i in range(start, start + count):
            kb.write(str(i))
            kb.press_and_release("down")
            time.sleep(0.3)

    def type_alphabets(self, count, ref):
        for i in range(count):
            serial = f"{string.ascii_uppercase[i]}-{ref}"
            kb.write(serial)
            kb.press_and_release("down")
            time.sleep(0.2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SerialTyper()
    window.show()
    sys.exit(app.exec_())
