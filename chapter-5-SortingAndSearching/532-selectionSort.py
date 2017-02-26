# 5.3.2 SELECTION SORT


def selectionSort(aList):
    for fillSlot in range(len(aList) - 1, 0, -1):
        posOfMax = 0

        for location in range(1, fillSlot + 1):
            if aList[location] > aList[posOfMax]:
                posOfMax = location

        aList[fillSlot], aList[posOfMax] = aList[posOfMax], aList[fillSlot]


aList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectionSort(aList)
print(aList)
