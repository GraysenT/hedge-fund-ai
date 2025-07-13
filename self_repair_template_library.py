Here is a Python code template that includes a class for managing house objects, with methods for common logic repairs and self-correction. This template uses basic principles such as checking for errors in house attributes and automatically correcting them if possible.

```python
class House:
    def __init__(self, address, num_rooms, num_bathrooms, square_feet, year_built):
        self.address = address
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.square_feet = square_feet
        self.year_built = year_built
        self.validate_attributes()

    def validate_attributes(self):
        if not isinstance(self.num_rooms, int) or self.num_rooms < 1:
            self.num_rooms = self.correct_rooms(self.num_rooms)
        
        if not isinstance(self.num_bathrooms, int) or self.num_bathrooms < 1:
            self.num_bathrooms = self.correct_bathrooms(self.num_bathrooms)
        
        if not isinstance(self.square_feet, int) or self.square_feet < 100:
            self.square_feet = self.correct_square_feet(self.square_feet)
        
        if not isinstance(self.year_built, int) or self.year_built < 1600 or self.year_built > 2023:
            self.year_built = self.correct_year_built(self.year_built)

    def correct_rooms(self, rooms):
        print(f"Invalid number of rooms: {rooms}. Setting to default value of 1.")
        return 1

    def correct_bathrooms(self, bathrooms):
        print(f"Invalid number of bathrooms: {bathrooms}. Setting to default value of 1.")
        return 1

    def correct_square_feet(self, square_feet):
        print(f"Invalid square footage: {square_feet}. Setting to minimum valid value of 100.")
        return 100

    def correct_year_built(self, year_built):
        print(f"Invalid year built: {year_built}. Setting to a plausible recent year of 2000.")
        return 2000

    def __str__(self):
        return (f"House at {self.address}\n"
                f"Rooms: {self.num_rooms}, Bathrooms: {self.num_bathrooms}\n"
                f"Square Feet: {self.square_feet}, Built in {self.year_built}")

# Example usage
house = House("123 Main St", 3, 2, 1500, 1990)
print(house)

house_with_errors = House("124 Main St", 0, -1, 50, 1500)
print(house_with_errors)
```

This code defines a `House` class that initializes with several attributes and checks them for common logical errors, such as negative numbers or non-integer values. If an error is detected, it corrects the value to a default or minimum valid value and prints a message about the correction. This ensures that the object maintains a valid state.