class Dog:
    def __init__(self, kind, age, name, vaccinated = False):
        self.kind = kind
        self.age = age
        self.name = name
        self.vaccinated = vaccinated

dog_1 = Dog(name = "Joy" , kind = "German Shepherd" , age = 4)
dog_2 = Dog(name = "Jhimmy" , kind = "Pomeranian" , age = 2)

print(dog_1.__dict__)
print(dog_2.__dict__)