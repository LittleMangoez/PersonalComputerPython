# time_display.py

from PyQt5.QtWidgets import QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSpacerItem, QSizePolicy
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
import math

class TimeDisplay(QMainWindow):
    """
    A PyQt5 QMainWindow that displays the current time in both digital and analog formats.
    Allows toggling between these formats.
    """

    def __init__(self):
        super().__init__()
        self.initUI()
        self.mode = 'digital'  # Default mode is digital

    def initUI(self):
        """
        Sets up the user interface of the window.
        Creates a QLabel for digital time display, an AnalogClock widget for analog time display,
        and a QPushButton to toggle between the two displays.
        """
        self.setWindowTitle('Time Display - Digital & Analog')
        self.setGeometry(100, 100, 400, 400)

        # Main widget for layout
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        # Create a vertical layout to hold widgets
        self.layout = QVBoxLayout(self.main_widget)

        # Create a label for digital time display
        self.digital_label = QLabel(self)
        self.digital_label.setGeometry(50, 20, 300, 100)
        self.digital_label.setStyleSheet("font-size: 24px; color: black;")
        self.digital_label.setAlignment(Qt.AlignCenter)

        # Create an analog clock widget (defined below)
        self.analog_clock = AnalogClock(self)
        self.analog_clock.setGeometry(50, 20, 300, 300)
        self.analog_clock.hide()

        # Add a spacer item to push the button to the bottom
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(spacer)

        # Create a toggle button to switch between digital and analog
        self.toggle_button = QPushButton("Switch to Analog", self)
        self.toggle_button.clicked.connect(self.toggle_mode)
        self.layout.addWidget(self.toggle_button)

        # Set up a timer to refresh the time every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second

        self.update_time()  # Show initial time

    def toggle_mode(self):
        """
        Toggles between digital and analog time display modes.
        """
        if self.mode == 'digital':
            self.mode = 'analog'
            self.digital_label.hide()
            self.analog_clock.show()
            self.toggle_button.setText("Switch to Digital")
        else:
            self.mode = 'digital'
            self.analog_clock.hide()
            self.digital_label.show()
            self.toggle_button.setText("Switch to Analog")

    def update_time(self):
        """
        Updates the displayed time in both digital and analog formats.
        """
        current_time = QTime.currentTime()

        # Update digital display
        time_str = current_time.toString('hh:mm:ss')
        self.digital_label.setText(time_str)

        # Update analog display
        self.analog_clock.update()  # Redraw the analog clock


class AnalogClock(QWidget):
    """
    Custom widget for displaying the current time as an analog clock.
    Draws clock face and hands using QPainter.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(300, 300)  # Set a fixed size for the clock

    def paintEvent(self, event):
        """
        Custom paint event to draw the clock face and hands.
        This is called whenever the widget needs to be redrawn.
        """
        painter = QPainter(self)
        rect = self.rect()

        # Draw the clock face
        painter.setRenderHint(QPainter.Antialiasing)
        center = rect.center()
        radius = min(rect.width(), rect.height()) // 2 - 10

        # Draw the outer circle (clock face)
        painter.setPen(QPen(Qt.black, 6))
        painter.drawEllipse(center, radius, radius)

        # Draw hour ticks
        painter.setPen(QPen(Qt.black, 2))
        for i in range(12):
            angle = math.radians(i * 30)
            x1 = center.x() + math.cos(angle) * (radius - 10)
            y1 = center.y() - math.sin(angle) * (radius - 10)
            x2 = center.x() + math.cos(angle) * (radius - 20)
            y2 = center.y() - math.sin(angle) * (radius - 20)
            painter.drawLine(x1, y1, x2, y2)

        # Get current time
        time = QTime.currentTime()

        # Draw the hour hand
        painter.setPen(QPen(Qt.black, 4))
        self.draw_hand(painter, center, radius * 0.5, (time.hour() % 12 + time.minute() / 60) * 30)

        # Draw the minute hand
        painter.setPen(QPen(Qt.black, 3))
        self.draw_hand(painter, center, radius * 0.75, time.minute() * 6)

        # Draw the second hand
        painter.setPen(QPen(Qt.red, 2))
        self.draw_hand(painter, center, radius * 0.85, time.second() * 6)

    def draw_hand(self, painter, center, length, angle):
        """
        Draws a clock hand at a specific angle and length.
        :param painter: QPainter object to draw on
        :param center: center of the clock
        :param length: length of the hand
        :param angle: angle of the hand in degrees
        """
        angle_radians = math.radians(angle - 90)  # Offset by 90 degrees to start from 12 o'clock
        end_x = center.x() + math.cos(angle_radians) * length
        end_y = center.y() + math.sin(angle_radians) * length
        painter.drawLine(center.x(), center.y(), end_x, end_y)
