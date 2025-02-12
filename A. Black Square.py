def calculate_calories(a, s):
    total_calories = 0
    for char in s:
        strip_index = int(char) - 1  # Convert '1', '2', '3', '4' to indices 0, 1, 2, 3
        total_calories += a[strip_index]
    return total_calories

# Input reading
a = list(map(int, input().strip().split()))
s = input().strip()

# Get the result
result = calculate_calories(a, s)

# Print the result
print(result)

