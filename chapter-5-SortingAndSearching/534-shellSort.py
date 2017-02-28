def shellSort(alist):
    sublistCount = len(alist) // 2
    while sublistCount > 0:
        for startPosition in range(sublistCount):
            gapInsertionSort(alist, startPosition, sublistCount)

            print("After increments of size {0} the list is {1}"
                  .format(sublistCount,  alist))

            sublistCount = sublistCount // 2


def gapInsertionSort(alist,  start,  gap):

    for i in range(start + gap,  len(alist),  gap):

        currenValue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currenValue:

            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currenValue


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(alist)
print(alist)
