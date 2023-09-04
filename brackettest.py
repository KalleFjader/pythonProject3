s = "()[]{}"


def isValid(s):
    t = True
    f = False
    storage = []

    n = "("
    m = "["
    d = "{"

    if (len(s) % 2 != 0):
        print("Insta false")
        return f
    else:
        h = round(len(s) / 2)
        storage.append(s[0])
        print(h)
        print("Storage to begin with")
        print(storage[0])
        for x in range(0, h+1):
            print(s[(x+1)])
            print("storage")
            print(storage)
            if (s[(x + 1)] == ")"):
                if ")" in storage:
                    storage.remove("(")
            elif (s[(x+1)] == "]"):
                if "]" in storage:
                    storage.remove("[")
            elif (s[(x + 1)] == "}"):
                if "}" in storage:
                    storage.remove("{")
            else:
                print("appended")
                storage.append(s[x+1])

    if (len(storage) == 0):
        print("True ")
        print(storage)
    else:
        print("False ")
        print(storage)

def isValid2(s):
    t = True
    f = False
    storage = []

    if (len(s) % 2 != 0):
        print("Insta false")
        return f
    storage.append(s[0])
    for x in range(0, len(s)-1):
        if (s[(x + 1)] == "(" or s[(x + 1)] == "[" or s[(x + 1)] == "{"):
            storage.append(s[(x + 1)])
        elif (s[(x + 1)] == ")" and storage.pop() != "("):
            return f
        elif (s[(x + 1)] == "]" and storage.pop() != "["):
            return f
        elif (s[(x + 1)] == "}" and storage.pop() != "{"):
            return f
    if(len(storage) == 0):
        return t






isValid2(s)