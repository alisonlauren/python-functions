def even_numbers(num):
    if num < 0:
        return "That number is negative"
    else:
        return "That number is positive"

while True:
    num = int(input("Pick number, I'll tell you if its positive: "))
    message = even_numbers(num)
    print(message)

