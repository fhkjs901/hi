import csv

cars = []

class car:
    def __init__(self, car_number, model, year, driver_name, distance_km, fuel_used_liters):
        self.car_number = car_number
        self.model = model
        self.year = year
        self.driver_name = driver_name.strip()
        self.distance_km = float(distance_km)
        self.fuel_used_liters = float(fuel_used_liters)

    def get_fuel_efficiency(self):
        return self.distance_km / self.fuel_used_liters if self.fuel_used_liters > 0 else 0

    def display_info(self):
        print(f"차량번호: {self.car_number}")
        print(f"모델명: {self.model} ({self.year})")
        print(f"평균연비: {self.get_fuel_efficiency():.2f} km/L\n")

def load_cars(filename):
    try:
        with open(filename, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                cars.append(car(
                    row["car_number"],
                    row["model"],
                    int(row["year"]),
                    row["driver_name"],
                    row["distance_km"],
                    row["fuel_used_liters"]
                ))
    except FileNotFoundError:
        print("CSV 파일을 찾을 수 없습니다.")
        exit()

def find_driver():
    driver_name = input("운전자 이름을 입력하세요: ").strip()
    driver_cars = [car for car in cars if car.driver_name == driver_name]

    if not driver_cars:
        print(f"'{driver_name}' 운전자는 데이터에 없습니다.")
        return

    total_distance = 0
    total_fuel = 0

    for car in driver_cars:
        car.display_info()
        total_distance += car.distance_km
        total_fuel += car.fuel_used_liters

load_cars("car.csv")
find_driver()
