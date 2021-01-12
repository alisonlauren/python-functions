#defining function and passing one arguement
def c_to_f(cel):
    #setting the return by telling the argument what it will run
    return (cel * (9/5)) + 32
#asking for using input for celcuis degree, ensuring an int
user_input = int(input("Enter celcuis degree to get farenheight conversion: "))
#setting variable for using user input and calling my function
degree_conversion = c_to_f(user_input)
#printing an f string for degree conversion 
print(f'{degree_conversion} degrees in Farenheight.')