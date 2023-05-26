def min_elements_removed(n, sequence):
    frequency = [0] * (n+1)  # Initialize frequency list with zeros

    for num in sequence:
        if num <= n:
            frequency[num] += 1

    max_removed = 0  # Maximum number of elements to be removed

    for i in range(1, n+1):
        if frequency[i] > i:
            max_removed += frequency[i] - i

    return max_removed

# Read the input
n = int(input())
sequence = list(map(int, input().split()))

# Call the min_elements_removed function
result = min_elements_removed(n, sequence)

# Print the result
print(result)

