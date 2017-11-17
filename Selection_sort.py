def swap(minimum_num, another_num):
    return another_num, minimum_num


def selection_sort(arr):
    no_of_elements = len(arr)
    for i in range(0,no_of_elements - 1):
        minimum_num_index = i
        for j in range(i + 1, no_of_elements):
            if arr[j] < arr[minimum_num_index]:
                minimum_num_index = j
        arr[minimum_num_index], arr[i] = swap(arr[minimum_num_index], arr[i])
