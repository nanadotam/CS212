def palis (word): 
    a = word[0]
    b = word[-1]
    c = word[1:-1]

    if a == b:
        return True
    elif len(word) == a + b + c:
        return True
    else:
        return False

print(palis("noon"))