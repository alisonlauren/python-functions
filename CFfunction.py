def c_to_f(cel):
    return (cel * (9/5)) + 32

user_input = int(input("Enter celcuis degree to get farenheight conversion: "))
degree_conversion = c_to_f(user_input)
print(f'{degree_conversion} degrees in Farenheight.')