def count_removals(n, stones):
    removals = 0
    for i in range(n - 1):
        if stones[i] == stones[i + 1]:
            removals += 1
    return removals

# Input reading
n = int(input().strip())
stones = input().strip()

# Get the result
result = count_removals(n, stones)

# Print the result
print(result)