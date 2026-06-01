class Pet:

    # CONSTRUCTOR
    def __init__(self, name="", animal_type="", age=0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        
    # GET METHODS
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age