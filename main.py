# main.py

import sys  # sys is needed to pass command-line arguments to the PyQt5 application
from PyQt5.QtWidgets import QApplication  # QApplication is the base class for all PyQt applications
from time_display import TimeDisplay  # Import the TimeDisplay class from the time_display.py module

# Set up the application
app = QApplication(sys.argv)  # QApplication handles application-wide settings and manages the event loop

# Create the TimeDisplay window
window = TimeDisplay()  # Create an instance of the TimeDisplay class
window.show()  # Display the window on the screen

# Run the application's event loop
sys.exit(app.exec_())  # Start the event loop, which waits for user interactions such as clicks and keyboard inputs
