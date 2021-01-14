def is_even(number):
    #if number can be divided by two and have nothing left over its even
    if (number % 2 == 0):  
        return True
    else:
        #otherwise its not
        return False

def is_odd(number):
    #if the number does not pass the "is_even" function conditional
   if not is_even(number):
       #its odd
       return True
   else:
        return False

user_input = int(input("Give me a number and I'll tell you if its odd: "))
answer = is_odd(user_input)
print(answer)
    
