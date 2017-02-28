def shellSort(alist):

    dividor = len(alist) // 2

    while dividor > 0:
        for i in range(dividor):
            gap_increment_sort(alist, i, dividor)

        dividor = dividor // 2


def gap_increment_sort(alist, start, gap):

    for j in range(start + gap, len(alist), gap):

        currentValue = alist[j]
        position = j

        while position >= gap and alist[position - gap] > currentValue:
            alist[position] = alist[position - gap]

            position = position - gap

        alist[position] = currentValue


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(alist)
shellSort(alist)
print(alist)
