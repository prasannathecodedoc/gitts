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



..................


# Linear Search in Python


def linearSearch(array, n, x):

    # Going through array sequencially
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


array = [2, 4, 0, 1, 9]
x = 1
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)



.........




# Binary Search in python


def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")



.......

SOURCE CODE
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'A')



.......


SOURCE CODE
# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'A')




