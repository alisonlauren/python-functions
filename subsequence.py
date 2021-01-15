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

#we take in the array and sequence
def isValidSubsequence(array, sequence):
    #tracking our index by init it to 0
    seqIdx = 0
    #for each value in the array
    for value in array:
        # if our seqidx equals the len of sequence, then stop looping
        if seqIdx == len(sequence):
            break
        #if the sequence continues to match the value of the array, keep going
        if sequence[seqIdx] == value:
            seqIdx += 1
        # you can now return the the answer once its looped over all values
    return seqIdx == len(sequence)

print(isValidSubsequence([1,2,3,4], [2,4]))
print(isValidSubsequence([1,2,3,4], [4, 2]))




