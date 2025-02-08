from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout

class GeneralDriverView(QWidget):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.initUI()

    def initUI(self):
        self.setWindowTitle("บุคคลทั่วไป - ข้อมูลผู้ขับขี่")
        layout = QVBoxLayout()

        self.info_label = QLabel(f"หมายเลขใบขับขี่: {self.driver.license_number}\n"
                                 f"สถานะ: {self.driver.status}")
        layout.addWidget(self.info_label)

        if self.driver.status == "ปกติ":
            self.test_button = QPushButton("ทดสอบสมรรถนะ")
            self.test_button.clicked.connect(self.toggle_test)
            layout.addWidget(self.test_button)

        self.setLayout(layout)

    def toggle_test(self):
        self.test_button.setEnabled(False)
        if self.test_button.text() == "ทดสอบสมรรถนะ":
            self.test_button.setText("สิ้นสุดการทดสอบ")
        else:
            self.test_button.setText("ทดสอบสมรรถนะ")
