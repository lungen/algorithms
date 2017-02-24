# 5.2.2 The Binary Search


def binarySearch(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:

        midpoint = (first + last) // 2

        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found




lista = [1,2,3,9,11,14,15,19,24,28,35]
print(binarySearch(lista, 14))
