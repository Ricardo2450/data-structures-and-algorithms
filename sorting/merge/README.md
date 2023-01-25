# Blog Notes: Merge Sort

# Ricardo soto-Fabela

## Contributors
* Aubrey
* Angelos

The code is divided into two functions: mergeSort() and printList().

1. The mergeSort() function takes in an array as input and checks if its length is greater than 1.

2. If the length of the array is greater than 1, the array is divided into two subarrays called L and M by finding the middle point.

3. Then the mergeSort() function is called recursively on both L and M subarrays. This will continue until each subarray has only one element, at which point they are considered sorted.

4. Once the subarrays are sorted, i, j, and k are set to 0.

5. The code enters into a while loop where it compares the first element of L and M subarrays. The smaller element is placed in the original array and the pointer is incremented. This is done until one subarray is completely traversed.

6. After the while loop, two more while loops are used to put the remaining elements of subarrays into the original array.

7. The printList() function takes in the sorted array and prints it.

8. The main driver program initiates an array and calls the mergeSort() function on that array.

9. The sorted array is then passed to printList() function to print it.

Overall, this code uses the divide and conquer approach to sort the input array by recursively dividing it into smaller subarrays and then merging them back together in a sorted order. It has time complexity of O(n log n) and is considered one of the efficient sorting algorithms.
