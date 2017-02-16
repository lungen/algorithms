"""
Write a function that takes a string as a parameter and returns True if the string is a palindrome,
False otherwise. Remember that a string is a palindrome if it is spelled the same both forward
and backward. for example: radar is a palindrome. for bonus points palindromes can also be
phrases, but you need to remove the spaces and punctuation before checking. for example:
    madam i’m adam is a palindrome. Other fun palindromes include:
        • kayak
        • aibohphobia
        • Live not on evil
        • Reviled did I live, said I, as evil I did deliver
        • Go hang a salami; I’m a lasagna hog.
        • Able was I ere I saw Elba
        • Kanakanak – a town in Alaska
        • Wassamassaw – a town in South Dakota
"""

# kayak

def palindromChecker(s):

    s = str(s)
    s = s.lower()

    #remove punctation recursive
    def remove_puncation(string):
        if len(string) == 1:
            return string[0]
        else:
            if string[0] in "',.;:" or string[0] == ' ':
                return remove_puncation(string[1:])
            else:
                return string[0] + remove_puncation(string[1:])
    
    s = remove_puncation(s)


    if len(s) == 1:
        return True
    else:
        if s[0] == s[-1]:
            return palindromChecker(s[1:-1])
        else:
            return False

#print(palindromChecker('kayak'))
#print(palindromChecker('aibohphobia'))
#print(palindromChecker('aibohphobia'))
print(palindromChecker('live not on evil'))
print(palindromChecker('Reviled did I live, said I, as evil I did deliver'))
