# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    # elements = len(arrA) + len(arrB)
    merged_arr = []
    # Your code here

    iA, iB = 0, 0

    while iA < len(arrA) and iB < len(arrB):
        if arrA[iA] < arrB[iB]:
            merged_arr.append(arrA[iA])
            iA += 1
        else:
            merged_arr.append(arrB[iB])
            iB += 1
    
    if iA == len(arrA):
        merged_arr.extend(arrB[iB:])
    else:
        merged_arr.extend(arrA[iA:])

    return merged_arr

# arr1 = [1, 3, 5]
# arr2 = [2, 4, 6]
# print(merge(arr1, arr2))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    i = int(len(arr) / 2)
    
    if len(arr) <= 1:
        return arr

    left, right = merge_sort(arr[:i]), merge_sort(arr[i:])

    return merge(left, right)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    return

def merge_sort_in_place(arr, l, r):
    # Your code here
    return
