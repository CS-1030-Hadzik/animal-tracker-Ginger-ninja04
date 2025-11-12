class Animal:
    """
    Base class representing a generic animal.
    """

    # Class-level attribute
    kingdom = "Animalia"

    # Class-level list to store all animals
    all_animals = []

    def __init__(self, name, species):
        self.name = name
        self.species = species
        # Add each new instance to the class-level list
        Animal.all_animals.append(self)

    def speak(self):
        print("The animal makes a noise.")

    def __str__(self):
        return f"Kingdom: '{self.kingdom}', Name: '{self.name}', Species: '{self.species}'"

