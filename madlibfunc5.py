def odd_numbers(num):
    if num % 2 != 0:
        return "That number is odd."
    else:
        return "That number is even."

while True:
    num = int(input("Pick number, I'll tell you if its odd: "))
    message = odd_numbers(num)
    print(message)