# Classes and Objects
class Car:
    # class variable accesible from all instances
    amount_cars = 0

    # this is our constructer used for initialising insitances of a class
    def __init__(self, manufacturer, model, hp):
        self.manufacturer = manufacturer
        self.model = model
        self.hp = hp
        Car.amount_cars += 1
        # hidden attributes are only accesible within the class .ie they are private
        self.__hidden = "Hello"

    # this is our destructer this is called when an isntance is deleted
    def __del__(self):
        print("Car deleted")
        Car.amount_cars -= 1

    def print_info(self):
        print("Manufacturer: {}, Model: {}, HP: {}".format(self.manufacturer, self.model, self.hp))


jimmy = Car("ee", "22", 12)
jimmy.print_info()
print(Car.amount_cars)
del jimmy
print(Car.amount_cars)


class Person:  # super class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getOlder(self, years):
        self.age += years


class Programmer(Person):  # child class
    def __init__(self, name, age, language):
        super(Programmer, self).__init__(name, age)  # superfunction inhertes from superclass
        self.language = language

    def favLanguage(self):
        print("My favorite programming language is {}".format(self.language))


john = Programmer("John", 20, "C++")
print(john.age)
john.favLanguage()
john.getOlder(2)
print(john.age)


class Vector:
    def __init__(self, x, y):  # constucter
        self.x = x
        self.y = y

    def __add__(self, other):  # defines what happens when 2 Vector Objects are added together
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other):  # defines what happens when 2 Vector Objects are subtracted
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __str__(self):  # Defines what happens when we print our Vector
        return "x: {} y: {}".format(self.x, self.y)


v1 = Vector(1, 2)
v2 = Vector(2, 4)
v3 = v1 + v2
print(v1)
print(v2)
print(v3)
