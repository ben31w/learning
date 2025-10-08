import car
import electric_car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = electric_car.ElectricCar('telsa', 'roadster', 2019)
print(my_tesla.get_descriptive_name())