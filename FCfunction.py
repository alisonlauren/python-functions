#defining function and passing one arguement
def f_to_c(faren):
    #telling the function what it will run
    return (faren - 32) * (5/9)
#asking for user input, ensuring its an integer
user_input = int(input("Enter farenheight degree to get celcius conversion: "))
#creating variable that calls the function and collides it with the user input
degree_conversion = f_to_c(user_input)
#printing an f string with degree conversion
print(f'{degree_conversion} degrees in Celcius.')


    




