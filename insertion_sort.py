import time 

start = time.time()
def insertion_sort(list):
    for i in range(1, len(list)):
        j = i-1
        nxt_element = list[i]

    while (list[j]> nxt_element) and (j>= 0):
        list[j+i]= list[j]
        j=j-1

    list[j+1 ]= nxt_element

list= [5,64,3,4,9,8,7,2,11,34,66,77,89]
insertion_sort(list)
print(list)

end =time.time()
print(end-start)



