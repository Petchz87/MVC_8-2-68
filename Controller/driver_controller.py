from Model.model import Database

class DriverController:
    def __init__(self):
        self.database = Database("Model/driver_database.csv")

    def validate_license_number(self, license_number):
        if license_number and (license_number.isdigit() and len(license_number) == 9 or license_number[0] != '0'):
            return True
        return False

    def find_driver(self, license_number):
        if not self.validate_license_number(license_number):
            self.view.show_error("หมายเลขใบขับขี่ไม่ถูกต้อง")
            return

        driver = self.database.get_driver(license_number)
        if driver:
            self.show_driver_view(driver)
        else:
            self.view.show_error("ไม่พบหมายเลขใบขับขี่")

    def show_driver_view(self, driver):
        age = driver.get_age()
        if driver.driver_type == "บุคคลทั่วไป":
            if age > 70:
                driver.status = "หมดอายุ"
            elif age < 16:
                driver.status = "ถูกระงับ"
            self.update_driver_status(driver.license_number, driver.status)
            self.view.show_general_driver(driver)
        elif driver.driver_type == "มือใหม่":
            if age > 50:
                driver.status = "หมดอายุ"
            elif age < 16:
                driver.status = "ถูกระงับ"
            self.update_driver_status(driver.license_number, driver.driver_type, driver.status)
            self.view.show_new_driver(driver)
        elif driver.driver_type == "คนขับรถสาธารณะ":
            if age > 60:
                driver.status = "หมดอายุ"
            elif age < 20:
                driver.status = "ถูกระงับ"
            self.update_driver_status(driver.license_number, driver.driver_type, driver.status)
            self.view.show_public_driver(driver)

    def get_summary(self):
        return self.database.get_driver_summary()

    def update_driver_status(self, license_number, driver_type, status):
        self.database.update_data(license_number, driver_type, status)