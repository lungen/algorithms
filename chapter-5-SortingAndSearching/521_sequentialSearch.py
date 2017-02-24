# 5.2.1 The Sequential Search


def sequential_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1

    return found

print(sequential_search([1, 2, 'a'], 'b'))
print(sequential_search([1, 2, 'a'], 2))

