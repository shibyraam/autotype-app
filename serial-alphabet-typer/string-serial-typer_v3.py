import sys
import time
import keyboard as kb
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QHBoxLayout, QMessageBox
)
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon


class SerialTyper(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon("img.ico"))  # use your .ico file
        self.setWindowTitle("Serial Number / Alphabet Typer")
        self.setGeometry(200, 200, 220, 100)

        layout = QVBoxLayout()

        # Mode selection
        self.label_creater = QLabel("Created by *** RAAM SHIBY ***")
        self.label_mode = QLabel("Choose the mode:")
        self.radio_num = QRadioButton("Serial Number Typer")
        self.radio_alpha_ref = QRadioButton("Alphabet with Ref No. Typer")
        self.radio_alpha_only = QRadioButton("Alphabet Only Typer")
        layout.addWidget(self.label_mode)
        layout_h = QHBoxLayout()
        layout_h.addWidget(self.radio_num)
        layout_h.addWidget(self.radio_alpha_ref)
        layout_h.addWidget(self.radio_alpha_only)
        layout.addLayout(layout_h)

        # Inputs
        self.input1 = QLineEdit()
        self.input1.setPlaceholderText("Start Serial Number (OR) Supplier Ref No. (Alphabet mode)")
        layout.addWidget(self.input1)

        self.input2 = QLineEdit()
        self.input2.setPlaceholderText("How many numbers/alphabets to type")
        layout.addWidget(self.input2)

        # Delay input
        self.input_delay = QLineEdit()
        self.input_delay.setPlaceholderText("Typing delay in seconds (default 0.2)")
        #layout.addWidget(self.input_delay)

        # Start button
        self.btn_start = QPushButton("Start Typing")
        self.btn_start.clicked.connect(self.start_typing)
        layout.addWidget(self.btn_start)

        layout.addWidget(self.label_creater)

        self.setLayout(layout)

    def start_typing(self):
        try:
            delay = float(self.input_delay.text() or 0.2)
        except ValueError:
            QMessageBox.warning(self, "Error", "Enter a valid delay (e.g., 0.2)")
            return

        key = "down"  # fixed to only down

        if self.radio_num.isChecked():
            try:
                start_num = int(self.input1.text())
                count = int(self.input2.text())
            except ValueError:
                QMessageBox.warning(self, "Error", "Enter valid numbers!")
                return

            QMessageBox.information(self, "Info", "Switch to Excel/target app. Typing starts in 3 seconds...")
            QTimer.singleShot(3000, lambda: self.type_numbers(start_num, count, delay, key))

        elif self.radio_alpha_ref.isChecked():
            try:
                count = int(self.input2.text())
            except ValueError:
                QMessageBox.warning(self, "Error", "Enter valid alphabet count!")
                return
            ref = self.input1.text().strip()

            if not ref:
                QMessageBox.warning(self, "Error", "Enter supplier reference!")
                return

            QMessageBox.information(self, "Info", "Switch to Excel/target app. Typing starts in 3 seconds...")
            QTimer.singleShot(3000, lambda: self.type_alphabets_with_ref(count, ref, delay, key))

        elif self.radio_alpha_only.isChecked():
            try:
                count = int(self.input2.text())
            except ValueError:
                QMessageBox.warning(self, "Error", "Enter valid alphabet count!")
                return

            QMessageBox.information(self, "Info", "Switch to Excel/target app. Typing starts in 3 seconds...")
            QTimer.singleShot(3000, lambda: self.type_alphabets_only(count, delay, key))

        else:
            QMessageBox.warning(self, "Error", "Select a mode!")

    def type_numbers(self, start, count, delay, key):
        for i in range(start, start + count):
            kb.write(str(i))
            kb.press_and_release(key)
            time.sleep(delay)

    def type_alphabets_with_ref(self, count, ref, delay, key):
        series = self.generate_alphabet_series(count)
        for s in series:
            serial = f"{s}-{ref}"
            kb.write(serial)
            kb.press_and_release(key)
            time.sleep(delay)

    def type_alphabets_only(self, count, delay, key):
        series = self.generate_alphabet_series(count)
        for s in series:
            kb.write(s)
            kb.press_and_release(key)
            time.sleep(delay)

    def generate_alphabet_series(self, limit):
        """Generates A, B, ..., Z, AA, AB ... up to given limit"""
        series = []
        for i in range(limit):
            s = ""
            n = i
            while True:
                s = chr(65 + (n % 26)) + s
                n = n // 26 - 1
                if n < 0:
                    break
            series.append(s)
        return series


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SerialTyper()
    window.show()
    sys.exit(app.exec_())
