'''
Input: a List of integers
Returns: a List of integers
'''
#Wednesday

# def moving_zeroes(arr):
#     removals = 0
#     for num in arr:
#         if num == 0:
#             removals += 1
#     for i in range(0, removals):
#         arr.remove(0)
#     arr.extend([0] * removals)
#     return arr

#Thursday


def moving_zeroes(arr):
    non_zero = 0
    for i in range(0, len(arr)):
        if arr[i] != 0:
            arr[non_zero] = arr[i]
            non_zero += 1
    while non_zero < len(arr):
        arr[non_zero] = 0
        non_zero += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
