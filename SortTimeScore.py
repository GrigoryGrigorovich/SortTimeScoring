import time
 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

arr = [i for i in range(100000)] 
start_time = time.time() 
sorted_arr = quick_sort(arr) 
end_time = time.time() 
print(" %s seconds" % (end_time - start_time))
