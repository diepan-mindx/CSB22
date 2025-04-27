class Animal:
    def __init__(self, name="", age=2, species=""):
        self.name = name
        self.age = age
        self.species = species
    
    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.species}."
        
        
obj1 = Animal("A", 3, "Dog")
print(obj1.__str__())

class A:
    def __init__(self) -> None:
        pass
    
    @classmethod
    def abc(cls):
        pass
    
A.abc()