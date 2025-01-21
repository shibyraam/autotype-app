import sys
import time
import keyboard as kb
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel

class WishTyperApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the UI components
        self.initUI()

    def initUI(self):
        # Set the window title and geometry
        self.setWindowTitle('Keyboard Autotype System')
        self.setGeometry(300, 300, 300, 50)

        # Create a QVBoxLayout to hold the widgets
        layout = QVBoxLayout()
        
        # Create a label for instructions
        self.label = QLabel('Enter your wish and number of repetitions:', self)
        layout.addWidget(self.label)

        # Create an input field for the "wish"
        self.wish_input = QLineEdit(self)
        self.wish_input.setPlaceholderText('Type your wish here')
        layout.addWidget(self.wish_input)

        # Create an input field for the number of repetitions
        self.repetitions_input = QLineEdit(self)
        self.repetitions_input.setPlaceholderText('How many times?')
        layout.addWidget(self.repetitions_input)

        # Create a button to trigger the action
        self.button = QPushButton('Start Typing', self)
        self.button.clicked.connect(self.start_typing)
        layout.addWidget(self.button)
        
        # Creater name
        self.label = QLabel('Creater by RAAMSHIBY S', self)
        layout.addWidget(self.label)

        # Set the layout for the window
        self.setLayout(layout)

    def start_typing(self):
        # Get the user inputs
        shift = self.wish_input.text()
        try:
            x = int(self.repetitions_input.text())
        except ValueError:
            self.label.setText("Please enter a valid number for repetitions.")
            return
        
        # Validate the inputs
        if not shift or x <= 0:
            self.label.setText("Please enter a valid wish and a positive number.")
            return

        # Notify the user the process is starting
        self.label.setText(f"Typing your wish {x} times...")

        # Delay before starting typing (optional)
        time.sleep(3)

        # Type the wish 'x' times
        for i in range(x):
            kb.write(shift)
            time.sleep(0.05)
            kb.press_and_release('enter')

        # Notify the user that the process is finished
        self.label.setText("Finished typing your wish!")
        #self.label.setText("Creater by RAAMSHIBY S")

# Create the application
app = QApplication(sys.argv)
window = WishTyperApp()

# Show the window
window.show()

# Run the application
sys.exit(app.exec_())
