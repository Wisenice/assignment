# TOPIC 1
# Define the Car class
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def display_details(self):
        print(f"Car: {self.make} {self.model} ({self.year}), Color: {self.color}")

# Instantiate three different car objects
car = Car("Toyota", "Camry", 2022, "Red")

# Display details of each car
car.display_details()


# TOPIC 2
#  Define the Car class
" we define a car class with an _init_method, which initializes the object's attributes when it's created." 
"The _init_method takes in make, model,year, and color parameters and assigns them to the object's attributes self.attribute_name." 
# Defining methods
"we define two methods: Display_Details and update_color"
"display_details prints out the car's attributes in a formmatted way."
"Update_color changes the car's color attribute to a new value."
# Creating car objects and calling method
"we create three car object(car1, car2, car3) by calling the car class with specific attribute values."
"Each object has its own set of attributes,which are stored in memory."
# calling methods
"we call the display_detail method on car1 to print out its attributes."
"we call the update_color method on car1, car2 and car3 to change from its original color attribute to the other after update. eg from white to black"
"We also call display_detail again to print out the updated attributes."
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
# Defining Methods
    def display_details(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")

    def update_color(self, new_color):
        self.color = new_color
        print(f"The color has been updated to {self.color}")

# 
my_car1 = Car("Toyota", "Land cruiser", 2014, "White")
my_car1.display_details()
my_car1.update_color("black")
my_car1.display_details()

my_car2 = Car("Toyota", "Mark_X", 2018, "black")
my_car2.display_details()
my_car2.update_color("Yellow")
my_car2.display_details()

my_car1 = Car("Honda", "Civic", 2018, "blue")
my_car1.display_details()
my_car1.update_color("Grey")
my_car1.display_details()




# TOPIC 3
# Define the Car class
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def display_details(self):
        print(f"Car: {self.make} {self.model} ({self.year}), Color: {self.color}")

# Prompt the user for car details
make = input("Enter the make of the car: ")
model = input("Enter the model of the car: ")
year = input("Enter the year of the car: ")
color = input("Enter the color of the car: ")

# Create a Car object with the provided details
new_car = Car(make, model, year, color)

# Display the car's information
print("\nDetails of the new car:")
new_car.display_details()
