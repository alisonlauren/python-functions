class Pet:
    #for default values, set in the parameters
    def __init__(self, name, fullness = 50, happiness = 50, hunger = 5, mopiness = 5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness 
        self.hunger = hunger
        self.mopiness = mopiness

        #methods in a class always have self inside param
    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30
    #incapsulation
    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness

#inherit from pet, don't need to change anything (pass)
class CuddlyPet(Pet):
    def __init__(self, name, fullness, hunger):
        super().__init__(name, fullness, 100, hunger, 2)


    def cuddle(self, other_pet):
        other_pet.get_love()

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2

thor = Pet("Thor", 50, 20, 10, 1)
nelson = Pet('Nelson', 100, 50, 5, 2)

print(thor.name)
print(thor.fullness)
thor.eat_food()
print(thor.fullness)

