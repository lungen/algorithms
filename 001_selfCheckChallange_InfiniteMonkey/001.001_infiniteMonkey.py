import random

goal = 'methinks it is like a weasel'

abcOrd = list(range(97, 123))
abcOrd.append(32)
abc = [chr(i) for i in abcOrd]

def generateString():
    # gernerate random string from 26 letters in alphabet plus the space

    s = str()
    for i in range(1,  29):
        s += random.choice(abc)

    return s


def score(s):
    # score the generated string with the goal

    if s == goal:
        return True
    #print(s)
    return False


def score_2(s):

    sc = ''
    for l, m in zip(s, goal):
        if l == m:
            sc += l
    return sc


def runner():

    i = 0
    best = -1
    bestGoal = ''
    timer = 1000000
    #while True:
    while i < 9000000:
        a = generateString()
        b = score_2(a)
        best = max(best, len(b))
        if len(b) > len(bestGoal):
            bestGoal = b
        if b == goal:
            print("GOT IT")
        if score(a):
            print("SCORE - GOT IT")
        if i == timer:
            print(i, best, bestGoal)
            timer += 1000000
        i += 1
    print(best, bestGoal)

runner()
