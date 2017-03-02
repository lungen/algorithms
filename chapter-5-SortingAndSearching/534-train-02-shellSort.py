def shellSort(alist):
    divisor = len(alist) // 2
    while divisor > 0:
        for i in range(divisor):
            gapInsertionSort(alist, i, divisor)
        divisor = divisor // 2


def gapInsertionSort(alist, start, gap):
    for j in range(start + gap, len(alist), gap):
        currentValue = alist[j]
        position = j
        while position >= gap and alist[position - gap] > currentValue:
            alist[position] = alist[position - gap]
            position -= gap

        alist[position] = currentValue


alist = [34, 22, 11, 1, 2, 7, 12, 32]
print(alist)
shellSort(alist)
print(alist)
