# Encapsulation

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!!"

    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
my_tesla = ElectricCar("Tesla", "404", "kWh")
print(my_tesla.get_brand())

# my_car = Car("Toyota", "Corolla")

# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullname())


