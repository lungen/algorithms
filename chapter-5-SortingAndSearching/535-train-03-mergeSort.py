def mergeSort(alist):
    if len(alist) > 1:
        # split
        mid = len(alist) // 2
        leftSide = alist[:mid]
        rightSide = alist[mid:]
        mergeSort(leftSide)
        mergeSort(rightSide)
        # merge
        i, j, k = 0, 0, 0
        while i < len(leftSide) and j < len(rightSide):
            if leftSide[i] < rightSide[j]:
                alist[k] = leftSide[i]
                i += 1
            else:
                alist[k] = rightSide[j]
                j += 1
            k += 1
        while i < len(leftSide):
            alist[k] = leftSide[i]
            i += 1
            k += 1
        while j < len(rightSide):
            alist[k] = rightSide[j]
            j += 1
            k += 1


alist = [22, 45, 12, 32, 18, 66, 12, 22]
print(alist)
mergeSort(alist)
print(alist)
