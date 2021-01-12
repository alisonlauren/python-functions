def is_even(number):
    if (number % 2 == 0):  
        return True
    else:
        return False

def is_odd(number):
   if not is_even(number):
       return True
   else:
        return False

user_input = int(input("Give me a number and I'll tell you if its odd: "))
answer = is_odd(user_input)
print(answer)
    
