## Palindrome Check

# What is a palindrome? A word that is spelled the same backward and forward.
# Example: "racecar", "hannah", "tot"
# Write a function that takes in a string and returns a boolean (true/false) representing whether
# the string is a palindrome or not.

#input: 'racecar'
#output: true

#input: 'banana'
#output: false


##Answer 1:

string = input("Please Enter your own single word: ")
#what is that? its slicing and when you write it this way
#it starts from the end towards the first, using index values
if(string == string[:: -1]):
    print("True")
else:
    print("False")




##Answer 2: 

def isPalindrome(string, i =0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)


# print(isPalindrome("nun"))
# print(isPalindrome("pancakes"))