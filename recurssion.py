def tri_recurse(k):
    if (k>0):
        result = k+tri_recurse(k-1)
        print(result)
    else:
        result = 0 

    return result  


print('\n\nrecurssion result')
tri_recurse(6)

