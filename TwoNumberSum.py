"""Write a function that takes a non-empty array of distinct integers.
The target sum has to be obtained by summing two different integers"""


def twonumbersum(array, targetsum):
    myarray = []
    if array:
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if array[i] + array[j] == targetsum:
                    myarray.append(array[i])
                    myarray.append(array[j])
                else:
                    pass
    print(myarray)


if __name__ == '__main__':
    a = [3, 5, -4, 8, 11, 1, -1, 6]
    s = 10
    twonumbersum(a, s)
