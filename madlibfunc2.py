def calculate(farenheight, arg2):
    if arg2 is int(farenheight - 32) * 5/9:
        return arg2

while True:
    farenheight = int(input("Give me a temp in farenheight and I'll convert to celcuis:   "))
    message = calculate(farenheight, arg2)
    print(message)

    
