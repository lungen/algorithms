def r_binarySearch(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        print("mp: ", a_list[midpoint])
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return r_binarySearch(a_list[:midpoint], item)
            else:
                return r_binarySearch(a_list[midpoint + 1:], item)

#lista = [1,2,3,5,8,13,17,21,31]
lista = [3,5,6,8,11,12,14,15,17,18]
print(r_binarySearch(lista, 16))

