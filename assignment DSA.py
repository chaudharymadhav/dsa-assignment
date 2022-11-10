def Selection_Sort(arr, n):
    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if (arr[j] < arr[min_index]):
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    # Driver Code


n = 5
arr = [2, 0, 1, 4, 3]
Selection_Sort(arr, n)

print("The Sorted Array by using " \
      "Selection Sort is : ", end='')
for i in range(n):
    print(arr[i], end=" ")

# Time Complexity:  O(n2).

# Auxiliary Space: O(1).



"""Selection Sort : 
The selection sort algorithm generally is the first sorting algorithm that is taught to us.
Here in every iteration of the inner loop, the smallest element is replaced with the
starting element in each loop. After the end of each loop, we increment the starting position
by 1 and run it till the second last element in the array. Hence, by doing so at the end of the outer
loop we will be having a sorted array."""



def Bubble_Sort(arr, n):
    for i in range(1, n):
        for j in range(0, n - i):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Driver Code
n = 5
arr = [2, 0, 1, 4, 3]
arr = Bubble_Sort(arr, n)

print("The Sorted Array by using Bubble Sort is : ", end='')
for i in range(n):
    print(arr[i], end=" ")

# Time Complexity:  O(n2).

# Auxiliary Space: O(1).
""" Bubble Sort :
The bubble sort algorithm might look a little bit confusing when we first study it.
But here is the easy explanation of it. Here swapping is carried on in two ways.
In every iteration of the outer loop, the largest element is found and swapped with
the last element in the loop. In the inner loop, we do pairwise swapping of two
consecutive elements. In every inner loop, we go from the first element to the one 
less element we went in the previous loop. The image below shows the 1st iteration 
of the inner loop in the Bubble Sort Algorithm."""
