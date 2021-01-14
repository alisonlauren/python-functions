## Validate Subsequence

# What is a subsequence? A subsequence is an array (set of numbers) that aren't
# necessarily adjacent in the array but are in the same order as the original sequence.

##Examples: Array - [1,2,3,4,5] Subsequence- [2,3,4]
#This is a subsequence because even though it doesn't contain all the numbers that
#The original sequence has, it does contain some of the values in the exact same order.

#Example: Array - [1,2,3,4] NOT Subsequence - [4,3,1]
#Output: False

#Example: Array - [5, 20, 44, 9] NOT Subsequence - [20, 44]
#Output: True

#Answer:

def isValidSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)

print(isValidSubsequence([1,2,3,4], [2,4]))
print(isValidSubsequence([1,2,3,4], [4, 2]))



