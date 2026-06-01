from pet_class import Pet

# PROGRAM HEADER
print("===================================")
print("      PET CLASS PROGRAM")
print("   OOP + ENCAPSULATION DEMO")
print("===================================")

# USER INPUT
pet_name = input("Enter Pet Name: ")
animal_type = input("Enter Animal Type: ")
pet_age = int(input("Enter Pet Age: "))

# CREATE OBJECT
my_pet = Pet()

# SET VALUES USING SET METHODS
my_pet.set_name(pet_name)
my_pet.set_animal_type(animal_type)
my_pet.set_age(pet_age)

# DISPLAY PET INFO
my_pet.display_pet_info()

print("\nThank you for using the program!")