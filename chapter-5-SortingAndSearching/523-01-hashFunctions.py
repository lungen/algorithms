# 5.2.3 HASHING 
# HASH-FUNCTIONS


def mid_finder(item):
    item = str(item)
    div = len(item) // 2
    if not len(item) % 2:  # gerade zahl
        return str(item[div-1] + item[div])
    else:
        return str(item[div])


l = [54, 26, 93, 17, 77, 31]

for idx, element in enumerate(l):
    print(element, element%11, int(mid_finder(element*element))%11)


def hash(a_string, table_size):

    sum = 0
    count = 0

    for letter in a_string:
        count += 1
        sum += (ord(letter) * count)

    print(sum)
    return sum % 11


print(hash('cat', 11))
