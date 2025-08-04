class Motorboat:
    def __init__(self, fuel_capacity, current_fuel, total_distance):
        self.fuel_capacity = fuel_capacity
        self.current_fuel = current_fuel
        self.total_distance = total_distance

    def __str__(self):
        return f"Motorboat (Fuel Capacity: {self.fuel_capacity} gallons, Current Fuel: {self.current_fuel} gallons, Total Distance Traveled: {self.total_distance} miles)"

    def add_miles(self, miles):

        self.total_distance += miles


# Example usage:
my_boat = Motorboat(fuel_capacity=20, current_fuel=10, total_distance=122)
print(my_boat)

# Add 50 miles to the total distance
my_boat.add_miles(50)
print(my_boat)

# Attempt to add 100 miles (not enough fuel)
my_boat.add_miles(100)
