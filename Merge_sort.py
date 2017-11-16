def merge_sort(arr, left, right):
    if left < right:

        mid = int((left + (right - 1)) / 2)

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    num_of_element_in_firstarray = mid - left + 1
    num_of_element_in_another_array = right - mid

    left_array = [0] * (num_of_element_in_firstarray)
    right_array = [0] * (num_of_element_in_another_array)

    for i in range(0, num_of_element_in_firstarray):
        left_array[i] = arr[left + i]

    for j in range(0, num_of_element_in_another_array):
        right_array[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < num_of_element_in_firstarray and j < num_of_element_in_another_array:
        if left_array[i] <= right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1

    while i < num_of_element_in_firstarray:
        arr[k] = left_array[i]
        i += 1
        k += 1

    while j < num_of_element_in_another_array:
        arr[k] = right_array[j]
        j += 1
        k += 1
