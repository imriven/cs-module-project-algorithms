'''
Input: an integer
Returns: an integer
'''
cookies = [1, 2, 3]

def eating_cookies(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    count = 0
    for i in range(len(cookies)):
        count += eating_cookies(n - cookies[i])
    return count


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 30

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
