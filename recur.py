def rec(k):
    if k == 0:
        return 1


    return k * rec(k-1)
    

result = rec(5)
print(result)
