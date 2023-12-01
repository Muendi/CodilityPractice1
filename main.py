def longest_switching_slice(A):
    max_length = 1
    current_length = 1

    for i in range(1, len(A)):
        if A[i] == A[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    return max(max_length, current_length)

# Example usage:
A = [3, 2, 3, 2, 3]
result = longest_switching_slice(A)
print(f"The length of the longest switching slice in {A} is {result}")
