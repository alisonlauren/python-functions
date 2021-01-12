#defining function and passing one arguement
def is_even(number):
    #if number is even
    if (number % 2 == 0): 
        #then, it's true 
        return True
    else:
        #anything else, it's false
        return False
#defining second function with one arguement
def is_odd(number):
    # if number is NOT true according to is even function.... 
   if not is_even(number):
       #then return true
       return True
   else:
       #anything else, False
        return False

#asking for user input, ensuring its an integer
user_input = int(input("Give me a number and I'll tell you if its odd: "))
#setting variable that collide function and user input
answer = is_odd(user_input)
#printing variable answer
print(answer)
    
