def traverse(nodep,nodeq):
    if(nodep == None and nodeq == None):
        print("return")
        return
    elif(nodep != None and nodeq == None):

        return False
    elif(nodep == None and nodeq != None):
        print("nodep == None and nodeq != None")
        return False
    if(nodep.val == nodeq.val):
        print("Is equal")
        traverse(nodep.left, nodeq.left)
        traverse(nodep.right, nodeq.right)
    else:
        print("Else")
        isTrue = False
        return isTrue


def isSameTree(p, q):
    isTrue = True
    traverse(p,q)
    return isTrue



