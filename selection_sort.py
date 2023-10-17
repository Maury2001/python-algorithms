import time 

start = time.time()

def selection_sort(input_list):
   for idx in range(len(input_list)):
      min_idx = idx
      for j in range( idx +1, len(input_list)):
         if input_list[min_idx] > input_list[j]:
            min_idx = j
      # Swap the minimum value with the compared value
      input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
l = [5,64,3,4,9,8,7,2,11,34,66,77,89]
selection_sort(l)
print(l)

end = time.time()
print(end-start)