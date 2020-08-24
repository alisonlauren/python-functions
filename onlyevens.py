def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

number_to_check = [2, 5, 6, -10] 

def only_evens(list_of_numbers):
    new_list = []

    for number in list_of_numbers:
        if is_even(number):
            new_list.append(number)

    return new_list

number_to_check = [2, 5, 6, -10]

print(only_evens(number_to_check))