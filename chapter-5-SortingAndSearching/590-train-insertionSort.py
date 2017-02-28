def insertionSort(l):
    for index, _value in enumerate(l[:-1], 1):

        currentValue = l[index]
        position = index

        while position > 0 and l[position - 1] > currentValue:
            l[position] = l[position - 1]
            position = position - 1

        l[position] = currentValue

    return l


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(alist)
print(insertionSort(alist))
