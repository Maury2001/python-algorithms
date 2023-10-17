import time

start = time.time()

def shellSort(input_list):
    gap = len(input_list) // 2
    while gap > 0:
        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i
            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j - gap
            input_list[j] = temp
        gap = gap // 2

my_list = [5,64,3,4,9,8,7,2,11,34,66,77,89]
shellSort(my_list)
print(my_list)


end = time.time()
print(end-start)