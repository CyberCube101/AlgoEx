'''Given two non-empty arrays of integers, write a function that determines whether the second array is a
subsequence of the first..
array=[5,1,22,25,6,-1,8,10]
sequence=[1,6,-1,10]
'''


def isValidSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):  # make sure we dont go out of bounds
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)  # we have gone through the whole sequence


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

print(isValidSubsequence(array=array, sequence=sequence))
