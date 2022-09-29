# Zachary Smith
# PA_10

class Car:

    # Class constructor
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    # property decorators
    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    # setters
    def set_make(self, make):
        self._make = make

    def set_model(self, model):
        self._model = model

    def set_year(self, year):
        self._year = year


class ElectricCar(Car):
    # Class constructor
    def __init__(self, make, model, year, battery, miles):
        Car.__init__(self, make, model, year)
        self.battery_size = battery
        self.miles_per_charge = miles

    # property decorators
    def get_battery_size(self):
        return self.battery_size

    def get_miles_per_charge(self):
        return self.miles_per_charge

    # setters
    def set_battery_size(self, battery):
        self.battery_size = battery

    def set_miles_per_charge(self, miles):
        self.miles_per_charge = miles




def main():
    # Read car input
    print("Car Input:")
    make = input(" Enter the make: ")
    model = input(" Enter the model: ")
    year = input(" Enter the year: ")

    # Prints car information
    car = Car(make, model, year)
    print("\nCar Information:")
    print(" Make:", car.get_make())
    print(" Model:", car.get_model())
    print(" Year:", car.get_year())

    # Reads Electric car input
    print("\nElectric Car input:")
    make = input(" Enter the make: ")
    model = input(" Enter the model: ")
    year = input(" Enter the year: ")
    battery = input(" Enter the battery size: ")
    miles = input(" Enter the miles between charge: ")

    # Prints Electric Car Information
    electric_car = ElectricCar(make, model, year, battery, miles)
    print("\nCar Information:")
    print(" Make:", electric_car.get_make())
    print(" Model:", electric_car.get_model())
    print(" Year:", electric_car.get_year())
    print(" Battery Size:", electric_car.get_battery_size())
    print(" Miles Between Charge:", electric_car.get_miles_per_charge())


main()  # Calling main method
