from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from Controller.driver_controller import DriverController
import random

class PublicDriverView(QWidget):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.complaints = random.randint(0, 10)  # สุ่มค่าการร้องเรียน
        self.controller = DriverController()
        self.controller.view = self
        self.initUI()

    def initUI(self):
        self.setWindowTitle("คนขับรถสาธารณะ - ข้อมูลผู้ขับขี่")
        layout = QVBoxLayout()

        self.info_label = QLabel(f"หมายเลขใบขับขี่: {self.driver.license_number}\n"
                                 f"สถานะ: {self.driver.status}\n"
                                 f"จำนวนร้องเรียน: {self.complaints}")
        layout.addWidget(self.info_label)

        if self.driver.status == "ปกติ":
            self.test_button = QPushButton("ทดสอบสมรรถนะ")
            self.test_button.clicked.connect(self.toggle_test)
            layout.addWidget(self.test_button)
        elif self.complaints > 5:
            self.training_button = QPushButton("อบรม")
            self.training_button.clicked.connect(self.toggle_training)
            layout.addWidget(self.training_button)

        self.setLayout(layout)

    def toggle_test(self):
        self.test_button.setEnabled(False)
        if self.test_button.text() == "ทดสอบสมรรถนะ":
            self.test_button.setText("สิ้นสุดการทดสอบ")
        else:
            self.test_button.setText("ทดสอบสมรรถนะ")

    def toggle_training(self):
        self.training_button.setEnabled(False)
        if self.training_button.text() == "อบรม":
            self.training_button.setText("สิ้นสุดการอบรม")
            self.complaints = 0
            self.toggle_test()
        else:
            self.training_button.setText("อบรม")
