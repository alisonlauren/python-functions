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

def palindrome(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]
    return string == reversedString

print(palindrome("hello"))
print(palindrome("racecar"))

##Answer 2: 

def isPalindrome(string, i =0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)


print(isPalindrome("nun"))
print(isPalindrome("pancakes"))