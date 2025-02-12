def minimum_shovels(k, r):
    for n in range(1, 11):  # Check from 1 to 10 shovels
        total_cost = n * k
        if total_cost % 10 == 0 or total_cost % 10 == r:
            return n
    return -1  # This should never reach because we can always buy 10 shovels

# Input reading
k, r = map(int, input().strip().split())

# Get the result
result = minimum_shovels(k, r)

# Print the result
print(result)