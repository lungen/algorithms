# 5.2.1 ordered sequential search


def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos += 1

    return found

lista = [1,2,3,5,7]
print(ordered_sequential_search(lista, 5))
print(ordered_sequential_search(lista, 4))
        


