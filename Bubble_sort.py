def bubble_sort(arr):
    no_of_element = len(arr)
    for k in range(0, no_of_element - 1):
        for i in range(0, no_of_element - k - 1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
