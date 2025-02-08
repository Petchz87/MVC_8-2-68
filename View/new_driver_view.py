from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from Controller.driver_controller import DriverController

class NewDriverView(QWidget):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.controller = DriverController()
        self.controller.view = self
        self.written_test_done = False
        self.practice_test_done = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle("มือใหม่ - ข้อมูลผู้ขับขี่")
        layout = QVBoxLayout()

        self.info_label = QLabel(f"หมายเลขใบขับขี่: {self.driver.license_number}\n"
                                 f"ประเภท: {self.driver.driver_type}\n"
                                 f"สถานะ: {self.driver.status}")
        layout.addWidget(self.info_label)

        if self.driver.status == "ปกติ":
            self.written_test_button = QPushButton("สอบข้อเขียน")
            self.written_test_button.clicked.connect(self.toggle_written_test)
            layout.addWidget(self.written_test_button)

            self.practice_test_button = QPushButton("สอบปฏิบัติ")
            self.practice_test_button.clicked.connect(self.toggle_practice_test)
            layout.addWidget(self.practice_test_button)

        self.setLayout(layout)

    def toggle_written_test(self):
        self.written_test_button.setEnabled(False)
        if self.written_test_button.text() == "สอบข้อเขียน":
            self.written_test_button.setText("สิ้นสุดการสอบข้อเขียน")
            self.written_test_done = True
        else:
            self.written_test_button.setText("สอบข้อเขียน")
            self.written_test_done = False
        self.check_and_update_driver_status()

    def toggle_practice_test(self):
        self.practice_test_button.setEnabled(False)
        if self.practice_test_button.text() == "สอบปฏิบัติ":
            self.practice_test_button.setText("สิ้นสุดการสอบปฏิบัติ")
            self.practice_test_done = True
        else:
            self.practice_test_button.setText("สอบปฏิบัติ")
            self.practice_test_done = False
        self.check_and_update_driver_status()

    def check_and_update_driver_status(self):
        if self.written_test_done and self.practice_test_done:
            self.driver.driver_type = "บุคคลทั่วไป"
            self.update_driver_status(self.driver.license_number, self.driver.driver_type, self.driver.status)

    def update_driver_status(self, license_number, driver_type, status):
        self.controller.update_driver_status(license_number, driver_type, status)
