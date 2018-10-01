def binarySearch(arr, item):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] > item:
            hi = mid - 1
        elif arr[mid] < item:
            lo = mid + 1
        else:
            return mid
    return -1


def selectionSort(arr):
    for counter in range(0, len(arr)):
        smallest = counter
        for j in range(counter + 1, len(arr)):
            if arr[smallest] > arr[j]:
                smallest = j
        if smallest != counter:
            arr[smallest], arr[counter] = arr[counter], arr[smallest]


def bubbleSort(arr):
    for counter in range(0, len(arr)):
        for i in range(0, len(arr) - counter - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


def insertonSort(arr):
    for i in range(0, len(arr)):
        save = arr[i]
        j = i - 1
        while j >= 0 and save < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = save


a = [10, 3, 2, 56, 2]
# print(binarySearch(a,20))
print(a)
# selectionSort(a)
# bubbleSort(a)
insertonSort(a)
print(a)