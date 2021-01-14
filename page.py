

def even_or_odd():
        num = int(input('What is your number? '))
        while num % 2 == 0:
            return f'{num} is an even number'
        else:
            print('Your number is odd!')
