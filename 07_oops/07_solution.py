# Static Method

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!!"
    
    def fuel_type(self):
        return "Petrol and Diesel"
    
    @staticmethod
    def generator_description():
        return "Cars are means of transport"

    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"
        
# my_tesla = ElectricCar("Tesla", "404", "kWh")
# print(my_tesla.fuel_type())

my_car = Car("Tata", "Safari")
Car("Tata", "Nexon")
# print(Car.total_car)
print(my_car.generator_description())
