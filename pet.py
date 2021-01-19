class Pet:
    #for default values, set in the parameters
    def __init__(self, name, fullness = 50, happiness = 50, hunger = 5, mopiness = 5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness 
        self.hunger = hunger
        self.mopiness = mopiness
    
    def __str__(self):
        return f"""
            {self.name}:
                fullness: {self.fullness}
                happiness: {self.happiness}
        """

        #methods in a class always have self inside param
    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30
    #incapsulation
    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness
    def eat_treat(self, treat):
        self.fullness += treat.tasty
        self.happiness += treat.enjoy

#inherit from pet, don't need to change anything (pass)
class CuddlyPet(Pet):
    def __init__(self, name, fullness = 50, hunger = 5):
        super().__init__(name, fullness, 100, hunger, 2)


    def cuddle(self, other_pet):
        other_pet.get_love()

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2

class Treat:
    def __init__(self, tasty = 10, enjoy = 10):
        self.tasty = tasty
        self.enjoy = enjoy

class Bones(Treat):
    def __init__(self):
        super().__init__(40,75)

class DayOldPotatoChildUnderCouch(Treat):
    def __init__(self):
        super().__init__(3, 45)

class humanFoodLeftOnTable(Treat):
    def __init__(self):
        super().__init__(4000, 10000)






