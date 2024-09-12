'''This module has two function -
1. merge_sort(arr) - Takes an array as input and performs merge sort on it
2. recombine(left_array, right_array) - This takes two sorted input arrays
and merges them in a sorted fashion'''

import rand


def merge_sort(arr_func):
    '''This function performs a recursive merge sort to the array input passed'''
    if len(arr_func) == 1:
        return arr_func

    half = len(arr_func) // 2

    return recombine(merge_sort(arr_func[:half]), merge_sort(arr_func[half:]))


def recombine(left_arr, right_arr):
    '''This function performs the merging of the two sorted input arrays
    left_array and right_array in a sorted fashion'''

    left_index, right_index, merge_arr = 0, 0, []

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr.append(right_arr[i])

    for i in range(left_index, len(left_arr)):
        merge_arr.append(left_arr[i])

    return merge_arr


array = rand.random_array([None] * 20)
arr_out = merge_sort(array)

print(arr_out)
