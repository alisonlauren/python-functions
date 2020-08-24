def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

number_to_check = [2, 5, 7, -10] 

def is_odd(list_of_numbers):
    new_list = []

    for number in list_of_numbers:
        if not is_even(number):
            new_list.append(number)

    return new_list

number_to_check = [2, 5, 6, 7, -10]

print(is_odd(number_to_check))