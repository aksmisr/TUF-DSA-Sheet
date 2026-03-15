"""This is  the  first problem of Array"""

def findLargestElement(arr, n):
    max = arr[0]  

    
    for i in range(1, n):
        if arr[i] > max:  
            max = arr[i]

    return max 

# Driver code
if __name__ == "__main__":
    arr1 = [2, 5, 1, 3, 0]
    n = len(arr1)  
    max = findLargestElement(arr1, n)  
    print("The largest element in the array is:", max)  
    arr2 = [8, 10, 5, 7, 9]
    n = len(arr2)  
    max = findLargestElement(arr2, n)  
    print("The largest element in the array is:", max)  