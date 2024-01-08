import time

def binary_search(arr, x):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1    
    return -1

def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

arr = list(range(1, 10000001))
n = len(arr)

x = 0
choice = 1
index1, index2 = 0, 0

while choice != 0:
    print("===========================")
    print("1. binary search")
    print("2. linear search")
    print("0. exit")
    print("===========================")
    choice = int(input("Pilih algoritma yang akan digunakan untuk melakukan pencarian : "))

    start = time.time()

    if choice == 1:
        x = int(input("Masukkan angka yang ingin dicari: "))
        index1 = binary_search(arr, x)
        if index1 != -1:
            print(f"The element {x} was found at index {index1}")
        else:
            print("The element was not found")
    elif choice == 2:
        x = int(input("Masukkan angka yang ingin dicari: "))
        index2 = linear_search(arr, x)
        if index2 != -1:
            print(f"The element {x} was found at index {index2}")
        else:
            print("The element was not found")

    stop = time.time()
    duration = float(stop - start)
    print(f"Running time: {duration} seconds\n")

    choice = int(input("Pilih algoritma yang akan digunakan untuk melakukan pencarian : "))

print("Program berakhir")
