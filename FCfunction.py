def f_to_c(faren):
    return (faren - 32) * (5/9)

user_input = int(input("Enter farenheight degree to get celcius conversion: "))
degree_conversion = f_to_c(user_input)
print(f'{degree_conversion} degrees in Celcius.')


    




