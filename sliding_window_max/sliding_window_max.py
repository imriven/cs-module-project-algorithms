from collections import deque

'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
#WENESDAY

# def sliding_window_max(nums, k):
#     results = []
#     for i, num in enumerate(nums):
#         if i + k <= len(nums):
#             results.append(max(nums[i:i + k]))
#     return results

 #THURSDAY

def sliding_window_max(nums, k):
    q = deque()
    results = []
    for i in range(k):
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        q.append(i)
    for i in range(k, len(nums)):
        results.append(nums[q[0]])
        while q and q[0] <= i - k:
            q.popleft()
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        q.append(i)
    results.append(nums[q[0]])
    return results


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
