'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
#Wednesday

# def single_number(arr):
#     seen = []
#     for num in arr:
#         if num in seen:
#             seen.remove(num)
#         else:
#             seen.append(num)
#     return seen[0]

#Thusday

def single_number(arr):
    result = 0
    for item in arr:
        result ^= item
    return result
#bitwise XOR

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")