'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here

    i = 0
    end = len(arr) - 1
    while i < end:
        if arr[i] == 0:
            arr.append(arr[i])
            del arr[i]
            end -= 1
        else:
            i += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")