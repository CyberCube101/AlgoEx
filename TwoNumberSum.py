def twoNumberSum(array, targetSum):
    myarray = []
    if array:
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if array[i] + array[j] == targetSum:
                    myarray.append(array[i])
                    myarray.append(array[j])
                else:
                    pass
    print(myarray)


if __name__ == '__main__':
    a = [3, 5, -4, 8, 11, 1, -1, 6]
    s = 10
    twoNumberSum(a, s)
