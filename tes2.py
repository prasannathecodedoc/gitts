def Selection_Sort(array):
    for i in range(0, len(array) - 1):
        smallest = i
        for j in range(i + 1, len(array)):
            if array[j] < array[smallest]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]

array = input('Enter the list of numbers: ').split()
array = [int(x) for x in array]
Selection_Sort(array)
print('List after sorting is : ', end='')
print(array)


def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
                
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
            
        # Place key at after the element just smaller than it.
        arr[j + 1] = key

arr = [9, 8, 6, 7, 1]
print("Unsorted Array:", arr)
insertion_sort(arr)
print('Sorted Array: ', arr)

def counting_Sort(arr, p):
    s = len(arr)
    result = [0] * s
    c = [0] * 10
    
    # count of elements
    for i in range(0, s):
        index = arr[i] // p
        c[index % 10] += 1
        
    # cumulative count
    for i in range(1, 10):
        c[i] += c[i - 1]

    # sorted order
    i = s - 1
    while i >= 0:
        index = arr[i] // p  
        result[c[index % 10] - 1] = arr[i]
        c[index % 10] -= 1
        i -= 1
        
    for i in range(0, s):
        arr[i] = result[i]


#  radix sort
def radix_Sort(arr):
    maximum = max(arr)

    p = 1
    while maximum // p > 0:
        counting_Sort(arr, p)
        p *= 10

#driver code
array = [354, 954, 411, 9]
print("The original array is: ", array)
radix_Sort(array)
print("The sorted array is: ", array)
