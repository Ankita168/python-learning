class Dog:
    def __init__(self , kind, age, name, vaccination = False):

        self.kind = kind
        self.age = age
        self.name =name
        self.vaccination = vaccination

        print('Instance Initialized')

    def get_kind(self):
        return self.kind

    def set_kind(self, kind):
        self.kind = kind

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
    
    def get_vaccination(self):
        return self.vaccination

    def set_vaccination(self, vaccinated):
        self.vaccination = vaccinated

    def get_details(self):
        return f"Name:{self.name} , Kind:{self.kind} , Age:{self.age}"

dog_1 =Dog("B" ,"4" , "Joy")
print(dog_1.get_details())

print(Dog.get_details(dog_1))