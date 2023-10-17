import time

start = time.time()
def bubblesort(list):

    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]> list[idx+1]:
                temp = list[idx]
                list[idx]= list[idx+1]
                list[idx+1]= temp

list = [5,64,3,4,9,8,7,2,11,34,66,77,89]
bubblesort(list)
print(list)

end = time.time()
print(end - start)