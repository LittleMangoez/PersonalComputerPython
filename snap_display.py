import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QHBoxLayout

class SnapDisplay(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the layout
        self.layout = QVBoxLayout()

        # Create sections for each data type
        self.setup_reminders_section()
        self.setup_notes_section()
        self.setup_calendar_section()

        # Set the layout for the widget
        self.setLayout(self.layout)
        self.setWindowTitle("Reminders, Notes, and Events")

    # Section for reminders
    def setup_reminders_section(self):
        reminders_label = QLabel("Reminders")
        self.reminders_list = QListWidget()

        # Placeholder data for reminders
        self.reminders_list.addItem("Buy groceries")
        self.reminders_list.addItem("Finish report")

        # Add to layout
        self.layout.addWidget(reminders_label)
        self.layout.addWidget(self.reminders_list)

    # Section for notes
    def setup_notes_section(self):
        notes_label = QLabel("Notes")
        self.notes_list = QListWidget()

        # Placeholder data for notes
        self.notes_list.addItem("Meeting notes from 10/18")
        self.notes_list.addItem("Ideas for the new project")

        # Add to layout
        self.layout.addWidget(notes_label)
        self.layout.addWidget(self.notes_list)

    # Section for calendar events
    def setup_calendar_section(self):
        events_label = QLabel("Calendar Events")
        self.events_list = QListWidget()

        # Placeholder data for calendar events
        self.events_list.addItem("Team meeting - 10/21, 10:00 AM")
        self.events_list.addItem("Doctor's appointment - 10/22, 1:30 PM")

        # Add to layout
        self.layout.addWidget(events_label)
        self.layout.addWidget(self.events_list)

# Main application
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create the SnapDisplay window and show it
    window = SnapDisplay()
    window.show()

    # Run the application
    sys.exit(app.exec_())
