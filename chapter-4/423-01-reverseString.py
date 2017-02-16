# a function that takes a string and returns a reverse

def revString(s):
    
    s = str(s)

    if len(s) == 1:  #BASE CASE
        return s[0]
    else:
        return s[-1] + revString(s[:-1])

print(revString('salami'))
