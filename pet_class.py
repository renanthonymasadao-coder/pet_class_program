class Pet:

    # CONSTRUCTOR
    def __init__(self, name="", animal_type="", age=0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

   # SET METHODS
    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    # GET METHODS
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

   # EXTRA METHOD
    def pet_sound(self):

        animal = self.__animal_type.lower()

        if animal == "dog":
            return "Woof Woof!"
        elif animal == "cat":
            return "Meow Meow!"
        elif animal == "bird":
            return "Tweet Tweet!"
        else:
            return "Cute sound!"

    # DISPLAY METHOD
    def display_pet_info(self):

        print("\n===================================")
        print("        PET INFORMATION")
        print("===================================")

        print(f"Pet Name     : {self.__name}")
        print(f"Animal Type  : {self.__animal_type}")
        print(f"Pet Age      : {self.__age}")

        print(f"Pet Sound    : {self.pet_sound()}")

        print("===================================")