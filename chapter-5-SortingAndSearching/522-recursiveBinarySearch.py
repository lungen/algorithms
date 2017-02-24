def r_binarySearch(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return r_binarySearch(a_list[:midpoint], item)
            else:
                return r_binarySearch(a_list[midpoint + 1:], item)

lista = [1,2,3,5,8,13,17,21,31]
print(r_binarySearch(lista, 5))

