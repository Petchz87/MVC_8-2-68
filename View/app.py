from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from Controller.driver_controller import DriverController
from View.general_drive_view import GeneralDriverView
from View.new_driver_view import NewDriverView
from View.public_driver_view import PublicDriverView


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = DriverController()
        self.controller.view = self
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Driver License System")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Enter Driver License Number:")
        self.license_input = QLineEdit()
        self.search_button = QPushButton("Search")
        self.summary_button = QPushButton("Show Summary")

        self.search_button.clicked.connect(self.search_driver)
        self.summary_button.clicked.connect(self.toggle_summary)

        layout.addWidget(self.label)
        layout.addWidget(self.license_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.summary_button)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.setLayout(layout)

    def search_driver(self):
        license_number = self.license_input.text()
        self.controller.find_driver(license_number)

    def show_error(self, message):
        QMessageBox.warning(self, "Error", message)

    def show_general_driver(self, driver):
        self.view = GeneralDriverView(driver)
        self.view.show()

    def show_new_driver(self, driver):
        self.view = NewDriverView(driver)
        self.view.show()

    def show_public_driver(self, driver):
        self.view = PublicDriverView(driver)
        self.view.show()

    def show_summary(self):
        summary = self.controller.get_summary()

        self.table.setRowCount(len(summary))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ประเภท", "ปกติ", "หมดอายุ", "ถูกระงับ"])

        for row, (driver_type, statuses) in enumerate(summary.items()):
            normal = statuses.get("ปกติ", 0)
            expired = statuses.get("หมดอายุ", 0)
            suspended = statuses.get("ถูกระงับ", 0)

            self.table.setItem(row, 0, QTableWidgetItem(driver_type))
            self.table.setItem(row, 1, QTableWidgetItem(str(normal)))
            self.table.setItem(row, 2, QTableWidgetItem(str(expired)))
            self.table.setItem(row, 3, QTableWidgetItem(str(suspended)))

        self.setGeometry(100, 100, 550, 300)
        self.summary_button.setText("Close Summary")

    def close_summary(self):
        self.setGeometry(100, 100, 300, 200)
        self.table.clear()
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        self.summary_button.setText("Show Summary")

    def toggle_summary(self):
        if self.summary_button.text() == "Show Summary":
            self.show_summary()
        else:
            self.close_summary()
