from operator import mul
from functools import reduce

'''
Input: a List of integers
Returns: a List of integers
'''
#Wednesday

# def product_of_all_other_numbers(arr):
#     result =  []
#     for i, num in enumerate(arr):
#        arr2 = arr.copy()
#        arr2.pop(i)
#        result.append(reduce(mul, arr2, 1))
#     return result
            
#Thusday

def product_of_all_other_numbers(arr):
    length = len(arr)
    result = [0] * length
    result[0] = 1
    for i in range(1, length):
        result[i] = arr[i - 1] * result[i - 1]
    right = 1
    for i in reversed(range(length)):
        result[i] = result[i] * right
        right *= arr[i]
    return result



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 7, 3, 4]
    # arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]    
    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
