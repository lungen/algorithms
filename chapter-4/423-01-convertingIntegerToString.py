# 4.2.3 Converting an Integer to a String in Any Base
# P. 121

def toStr(nr, base):
    conv_str = '0123456789ABCDEF'

    if nr < base:
        return conv_str[nr]
    else:
        return toStr(nr // base, base) + conv_str[nr % base]

print(toStr(1678, 16))
