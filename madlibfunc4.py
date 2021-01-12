def even_numbers(num):
    if num % 2 == 0:
        return "That number is even."
    else:
        return "That number is odd."

while True:
    num = int(input("Pick number, I'll tell you if its even: "))
    message = even_numbers(num)
    print(message)