class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all  = []

    def __init__(self,name,pet_type,owner = None):

        if pet_type not in Pet.PET_TYPES:
              raise Exception(f"Invalid pet_type '{pet_type}'. Must be one of: {Pet.PET_TYPES}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self,value):
        if isinstance(value,Owner):
           self._owner = value
        else:
            return False

class Owner:
    def __init__(self,name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self,pet):
        if not isinstance(pet,Pet):
            raise TypeError("Pet must be an instane of the class")
        pet.owner = self
    def get_sorted_pets(self):
        return sorted(self.pets(), key = lambda p:p.name)







    