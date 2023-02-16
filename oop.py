class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
        print(f"Hello! My name is {self.name} and my age is {self.age}")
#creating my object
person1=person("Json",18)
person1.say_hello()
person2=person("Ken",21)
person2.say_hello()
#create a class called cars with the following attributes/properties
#make.mode.year then create a function that prints make,mode and year
#then create three objects
class Cars:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display(self):
        print(f"The car is {self.make} and a model of {self.model} and built in {self.year}")
car1=Cars("Defender 110", "Land Rover", 2023)
car1.display()
car2=Cars("Supra","Toyota",2022)

class fruits:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def display(self):
        print(f"I like eating {self.name} its {self.color} color makes it look juicy")
fruit1=fruits("Mangoes","red")
fruit1.display()
fruit2=fruits("orange","orange")
fruit2.display()