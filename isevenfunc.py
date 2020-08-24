
def is_even(number):
    if (number % 2 == 0):  
        return True
    else:
        return False
    

user_input = int(input("Give me a number and I'll tell ya if it's positive: "))
answer = is_even(user_input)
print(answer)


