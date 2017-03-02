def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitPoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitPoint - 1)
        quickSortHelper(alist, splitPoint + 1, last)


def partition(alist, first, last):
    pivotValue = alist[first]
    leftMark = first + 1
    rightMark = last
    done = False
    while not done:
        while leftMark <= rightMark and \
                alist[leftMark] <= pivotValue:
            leftMark = leftMark + 1
        while alist[rightMark] >= pivotValue and \
                rightMark >= leftMark:
            rightMark = rightMark - 1
        if rightMark < leftMark:
            done = True
        else:
            temp = alist[leftMark]
            alist[leftMark] = alist[rightMark]
            alist[rightMark] = temp

    temp = alist[first]
    alist[first] = alist[rightMark]
    alist[rightMark] = temp

    return rightMark


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)

