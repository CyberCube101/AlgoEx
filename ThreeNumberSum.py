
''' Write a function that takes a non empty array of distinct integers and an integer

representing a target sum. The function should find all triplets in the array that sum to the target

array=[12,3,1,2,-6,5,-8,6]
targetSum=0

[[-8,2,6],[-8,3,5],[-6,1,5]]

'''


def threeNumberSum(array, targetSum):
    zippedlist = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            for k in range(j + 1, len(array)):
                if sum([array[i], array[j], array[k]]) == targetSum:
                    combination = [array[i], array[j], array[k]]
                    combination.sort()
                    zippedlist.append(combination)
    zippedlist.sort()
    return zippedlist


array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
print(threeNumberSum(array=array, targetSum=targetSum))
