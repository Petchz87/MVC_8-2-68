from collections import defaultdict
import csv
from datetime import datetime

class Driver:
    def __init__(self, license_number, driver_type, birthdate, status):
        self.license_number = license_number  # หมายเลขใบขับขี่
        self.driver_type = driver_type  # ประเภทของผู้ขับขี่
        self.birthdate = birthdate  # วันเกิด
        self.status = status  # สถานะใบขับขี่

    def get_age(self):
        today = datetime.today()
        birth_date = datetime.strptime(self.birthdate, "%d/%m/%Y")
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

class Database:
    def __init__(self, filename):
        self.filename = filename
        self.drivers = self.load_data()

    def load_data(self):
        drivers = []
        try:
            with open(self.filename, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                print("File opened successfully!")

                for row in reader:
                    driver = Driver(
                        row['license_number'], row['driver_type'], row['birthdate'], row['status'])
                    drivers.append(driver)
        except FileNotFoundError:
            print("File not found")
        return drivers

    def get_driver(self, license_number):
        for driver in self.drivers:
            if driver.license_number == license_number:
                return driver
        return None
    
    def update_data(self, license_number, driver_type, status):
        with open(self.filename, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['license_number', 'driver_type', 'birthdate', 'status'])
            writer.writeheader()
            for driver in self.drivers:
                writer.writerow({
                    'license_number': driver.license_number,
                    'driver_type': driver.driver_type,
                    'birthdate': driver.birthdate,
                    'status': driver.status
                })
        
    def get_driver_summary(self):
        self.drivers = self.load_data()
        summary = defaultdict(lambda: defaultdict(int))
        for driver in self.drivers:
            driver_type = driver.driver_type
            status = driver.status
            summary[driver_type][status] += 1
        return summary
