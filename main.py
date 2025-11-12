from animal import Animal
from dog import Dog

if __name__ == "__main__":
    # Create an instance of the Animal class
    generic_animal = Animal("Generic", "Unknown")
    print(generic_animal)            # Test __str__
    generic_animal.speak()           # Test speak method

    # Create an instance of the Dog class
    buddy = Dog("Fido", "Canine", "Bulldog")
    print(buddy)                     # Test overridden __str__
    buddy.speak()                    # Test overridden speak method

    # Print all animals
    print("All Animals:")
    for animal in Animal.all_animals:
        print(animal)
