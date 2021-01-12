#defining function and passing one arguement
def is_even(number):
    #if number is even and greater or equal to 0
    if (number % 2 == 0) and (number >= 0):
        #using boolean, true 
        return True
    else:
        #anything else, return false
        return False
    
#asking for user input on number, ensuring its an integer
user_input = int(input("Give me a number and I'll tell ya if it's positive and even: "))
#setting variable and collding user input with variable
answer = is_even(user_input)
#printing the answer variable
print(answer)


