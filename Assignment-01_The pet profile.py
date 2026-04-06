
class Pet:
    
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def introduce(self):
        print("Hi! I am " + self.name + ", a " + str(self.age) + "-year-old " + self.species + ".")

    def birthday(self):
        self.age = self.age + 1
        print("Happy Birthday " + self.name + "! Now I am " + str(self.age) + " years old.")

    def is_senior(self):
        if self.age >= 8:
            return True
        else:
            return False


# 3 pet objects
pet1 = Pet("Bruno", "dog", 5)
pet2 = Pet("Billu", "cat", 8)
pet3 = Pet("Coco", "parrot", 3)

# Pet1
pet1.introduce()
pet1.birthday()
print("Is senior:", pet1.is_senior())
print()

# Pet2 
pet2.introduce()
pet2.birthday()
print("Is senior:", pet2.is_senior())
print()

# Pet3
pet3.introduce()
pet3.birthday()
print("Is senior:", pet3.is_senior())