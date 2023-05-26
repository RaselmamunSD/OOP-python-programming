def maximize_operations(n, arr):
    max_operations = float('inf')  # Initialize with infinity
    
    for num in arr:
        operations = 0
        while num % 2 == 0:
            num //= 2
            operations += 1
        max_operations = min(max_operations, operations)
    
    return max_operations

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Call the function and print the result
print(maximize_operations(n, arr))
