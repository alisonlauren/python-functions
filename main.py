from pet import Pet, CuddlyPet

# Begin with no pets.
pets = []

main_menu = [   
    "Adopt a Pet",
    "Play with Pet",
    "Feed Pet",
    "View status of pets",
    "Do nothing",
]

adoption_menu = [
    "Pet",
    "CuddlyPet"
]

def print_menu_error():
    print("That was not a valid choice. Try again.\n\n\n")    

def choices_to_string(choice_list):
    choice_string = ""
    num = 1
    for choice in choice_list:
        choice_string += "%d: %s\n" % (num, choice)
        num += 1
    choice_string += "Please choose an option: "
    return choice_string

def get_user_choice(choice_list):
    choice = -1
    choice_string = choices_to_string(choice_list)
    while choice == -1:
        try:
            choice = int(input(choice_string))
            if choice <= 0 or choice > len(choice_list):
                raise ValueError
        except ValueError:
            print_menu_error()
    return choice

def main():    
    while True:
        choice = get_user_choice(main_menu)
        if (choice == 1):
            pet_name = input("What would you like your pet name to be? ")
            type_choice = get_user_choice(adoption_menu)
            if (type_choice == 1):
                pets.append(Pet(pet_name))
            elif (type_choice == 2):
                pets.append(CuddlyPet(pet_name))
            num_pets = len(pets)
            print(f"You just added {pet_name}, and now you have {num_pets} pet(s)")
        
        elif (choice == 2):
            for pet in pets:
                pet.get_love()

        elif (choice == 3):
            for pet in pets:
                pet.eat_food()

        elif (choice == 4):
            for pet in pets:
                print(pet)

        for pet in pets:
            pet.be_alive()
            
main()
