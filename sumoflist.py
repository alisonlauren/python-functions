#find sum in list

total = 0
list =  [1,2,4,5]

for element in range(0, len(list)):
    total = total + list[element]

print("Sum is: ", total)

# find largest in list

list1 = [1,2,3,4,5,6]
print("Largest element is:" , max(list1))

# find smallest number
list2 = [0,1,2,3,4,5,6]
print("Smallest element is: ", min(list2))

# find even numbers in list
list3 = [10, 44, 5, 7, 3]
for num in list3:
    if num % 2 == 0:
        print(num, end = ", " )

# or.. 

def giveMeEven(list):
    newList = []
    for number in list:
        if number % 2 == 0:
            newList.append(number)
    return newList
print("The even numbers are... ")
print(giveMeEven([1,2,3,4,5,6,7,8]))

## give me only positive numbers

list4 = [70, -4, 3, 9999, -40000000]
newList4 = []
for num in list4:
    if num >= 0:
        newList4.append(num)
print(newList4)

## multiply a list

my_list = [11, 22, 35, 64, 15]
my_new_list = [number * 5 for number in my_list]
print(my_new_list)

## reverse string

def reverse_this(x):
    return x[::-1]

##In this particular example, the slice statement [::-1] means start at 
# the end of the string and end at position 0, move with the step -1, 
# negative one, which means one step backwards.

myString = reverse_this(" How does this look now that it's backward")
print(myString)

## multiply vector 

firstList = [5, 2, 3]
secondList = [1, 5, 4]
multiply = []
for number1, number2 in zip(firstList, secondList):
    multiply.append(number1 * number2)
print(multiply)

## the zip function in Python 3 returns an iterator. 
# Iterators can only be exhausted (by something like making 
# a list out of them) once. The purpose of this is to save 
# memory by only generating the elements of the iterator as you 
# need them, rather than putting it all into memory at once.



