def binaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newValue):
    root[0] = newValue


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


r = binaryTree(3)
insertLeft(r, 4)
insertLeft(r, 5)
insertRight(r, 6)
insertRight(r, 7)
print(r)
l = getLeftChild(r)
print(l)


x = binaryTree('a')
insertLeft(x, 'b')
insertRight(x, 'c')
insertRight(getRightChild(x), 'd')
insertLeft(getRightChild(getRightChild(x)), 'e')
print(x)


t = binaryTree('a')
insertLeft(t, 'b')
insertRight(getLeftChild(t), 'd')
insertRight(t, 'c')
insertLeft(getRightChild(t), 'e')
insertRight(getRightChild(t), 'f')
print(t)
