from animal import Animal

class Dog(Animal):
    """
    Derived class representing a dog, which is a type of Animal.
    """

    def __init__(self, name, species, breed):
        # Initialize name and species using the Animal constructor
        super().__init__(name, species)
        self.breed = breed

    def speak(self):
        print("The dog barks.")

    def __str__(self):
        return f"Kingdom: {self.kingdom}, Name: {self.name}, Species: {self.species}, Breed: {self.breed}"
