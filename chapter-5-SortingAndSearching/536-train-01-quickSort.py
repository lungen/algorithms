def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitPoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitPoint - 1)
        quickSortHelper(alist, splitPoint + 1, last)


def partition(alist, first, last):
    done = False
    leftMark = first + 1
    rightMark = last
    pivotValue = alist[first]

    while not done:
        while alist[leftMark] <= pivotValue and \
                leftMark <= rightMark:
                    leftMark += 1
        while alist[rightMark] >= pivotValue and \
                rightMark >= leftMark:
                    rightMark -= 1
        if rightMark < leftMark:
            done = True
        else:
            tmp = alist[leftMark]
            alist[leftMark] = alist[rightMark]
            alist[rightMark] = tmp

    tmp = alist[first]
    alist[first] = alist[rightMark]
    alist[rightMark] = tmp

    return rightMark


alist = [44, 33, 22, 1, 2, 5, 66, 44, 31, 82]
print(alist)
quickSort(alist)
print(alist)
