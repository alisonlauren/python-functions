
##question 1:
gift_request = input("Hello, what would you like for christmas? ")
user_input = input("Santa: Have you been good or bad this year?  ")

if user_input.lower() == 'good':
    print(f"Okay, good for you, you get the {gift_request}")
elif user_input.lower() == 'bad':
    print(f"I don't feel bad for you, you'll never get {gift_request} ")
else:
    print("Try again, either say good or bad")

#question 2: