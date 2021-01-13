#defining function and passing one arguement
def is_even(number):
    #if number is even...
    if number % 2 == 0:
        #then this boolean returns true
        return True
    else:
        #anything else, false
        return False

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


#setting variable to a list
number_to_check = [2, 5, 6, -10] 
#defining a new function and passing one arguement
def only_evens(list_of_numbers):
    #ensuring new list is empty
    new_list = []
#for loop, checking number in list of numbers variable
    for number in list_of_numbers:
        #if is even function works on the inputed number..
        if is_even(number):
            #then add new the new number to the empty new list
            new_list.append(number)
#calling the function
    return new_list
#same variable as before
number_to_check = [2, 5, 6, -10]
#print onlyevens functions against numbers to check variable
print(only_evens(number_to_check))

number_to_check = [2, 5, 6, -10] 
def only_evens(list_of_numbers):
    new_list = []
    for number in list_of_numbers:
        if is_even(number):
            new_list.append(number)
    return new_list
    print(only_evens(number_to_check))