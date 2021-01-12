#defining function and passing one arguement
def is_even(number):
    #is the number even?
    if number % 2 == 0:
        #using a boolean, it's true!
        return True
    else:
        #anything else, its false!
        return False
#setting variable to string of integers
number_to_check = [2, 5, 7, -10] 
#defining function and passing one arguement
def is_odd(list_of_numbers):
    #setting variable to an empty list
    new_list = []
#for loop, for number in list of numbers variables
    for number in list_of_numbers:
        #if number is NOT able to pass true on the iseven function...
        if not is_even(number):
            #than go ahead and add it to the new list
            new_list.append(number)
#calling the function to run
    return new_list
#same set of variables as before..
number_to_check = [2, 5, 6, 7, -10]
#printing the numbersto check that can run true using the is odd function
print(is_odd(number_to_check))