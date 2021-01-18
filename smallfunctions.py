### madlib
def make_formal_greeting(name, title, location):
    return f"{intro} {name}, the {title} of {location}"

intro = "Now comes"
result = make_formal_greeting("Rob", "King", "The North")
print(result)

result = make_formal_greeting("The North", "Rob", "King")
print(result)

result = make_formal_greeting("Sadie", "Doggie", "Kingwood")
print(result)

##calculate farenheight
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

###odd numbers
def odd_numbers(num):
    if num % 2 != 0:
        return "That number is odd."
    else:
        return "That number is even."

while True:
    num = int(input("Pick number, I'll tell you if its odd: "))
    message = odd_numbers(num)
    print(message)
    break



##even numbers
def even_numbers(num):
    even_list = [4,6]
    if num % 2 == 0:
        even_list.append(num)
        print(even_list)
        return "That number is even."
    else:
        return "That number is odd."

while True:
    num = int(input("Pick number, I'll tell you if its even: "))
    message = even_numbers(num)
    print(message)
    break


##medium
##find smallest string

def getSmallWord(n):
    #- Use set because set will add one one word when user enter duplicate words.
    words = set()
    for i in range(n):
        word = raw_input("Enter word: ")
        words.add(word)

    #- Assign First word as smallest.
    smallest_word = words.pop()

    #- Iterate words from the 1 index. because we assign 0th element as Smallest.
    for word in words:
        #- Check Lenght of current elemnt from the User Input with the Smallest Word.
        if len(word)<len(smallest_word):
            smallest_word = word

    return smallest_word

## or 

test_list = ['gfg', 'is', 'best'] 

# printing original list  
print("The original list : " + str(test_list)) 

# Minimum String length 
# using min() + generator expression 
res = min(len(ele) for ele in test_list) 

# printing result 
print("Length of minimum string is : " + str(res)) 

##next medium question


user_input = (input("please enter a word: "))
def word_count(str):
    counts = dict()
    words = str.split()
    
    for letter in words:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    sortedValues = sorted(counts, key=counts.get, reverse=True)
    sortedCounts = {}
    
    for value in sortedValues:
        sortedCounts[value] = counts[value]
    
    return sortedCounts
       
print(word_count(user_input))