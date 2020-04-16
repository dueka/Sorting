# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0]
    # TO-DO
    j, k = 0, 0
    while len(arrA) and len(arrB) != 0 and len(merged_arr) < elements:
        if arrA[j] < arrB[k]:
            merged_arr.append(arrA[j])
            j += 1
        else:
            merged_arr.append(arrB[k])
            j += 1
        return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    # m = arr/2
    # mergeSort(arr, l, m)
    # mergeSortt(arr, m+1, r)
    # merge(arr, l, m, r)
    if len(arr) > 1:
        middle = len(arr)//2
        left_array = arr[:middle]
        right_array = arr[middle:]

        # merge_Sort(left_array)
        # merge_Sort(right_array)
        return merge(left_array, right_array)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
