# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, low, high):
    # Your code here

    if low > high:
        return -1  # not found
    else:
        mid = (high + low) // 2

        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            # high = mid - 1
            return binary_search(arr, target, low, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, high)


# arr = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
# found = binary_search(arr, -8, 0, len(arr)-1)
# print('the element -8: ', found)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    start = 0
    end = len(arr) -1

    isAscending = arr[start] < arr[end]

    while start <= end:

      mid = (start + end) // 2

      if target == arr[mid]:
        return mid

      if isAscending:
        if target < arr[mid]:
          end = mid - 1
        else:
          start = mid + 1

      else:      
        if target > arr[mid]:
          end = mid - 1
        else:
          start = mid + 1

    return -1


    # start = arr[0]
    # end = arr[1]

    # low = 0
    # high = len(arr) - 1

    # if arr[start] < arr[end]:
    #     if low > high:
    #         return -1  # not found
    #     else:
    #         mid = (high + low) // 2

    #         if target == arr[mid]:
    #             return mid
    #         elif target < arr[mid]:
    #             # high = mid - 1
    #             return binary_search(arr, target, low, mid - 1)
    #         else:
    #             return binary_search(arr, target, mid + 1, high)
    # else:
    #     if low > high:
    #         return -1  # not found
    #     else:
    #         mid = (high + low) // 2

    #         if target == arr[mid]:
    #             return mid
    #         elif target > arr[mid]:
    #             # high = mid - 1
    #             return binary_search(arr, target, mid + 1, high)
    #         else:
    #             return binary_search(arr, target, low, mid - 1)