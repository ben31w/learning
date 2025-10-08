from car import Car

my_car = Car('audi', 'a4', 2019)
print(my_car.get_descriptive_name())

my_car.update_mileage(69_000)
my_car.update_mileage(50_000)
my_car.read_odometer()

my_car.add_miles(420)
my_car.read_odometer()