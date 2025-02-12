def final_position(s, t):
    position = 0  # Start at the first stone (0-based index)
    
    for instruction in t:
        if position < len(s) and s[position] == instruction:
            position += 1  # Move to the next stone if colors match

    return position + 1  # Convert to 1-based index for output

# Input reading
s = input().strip()
t = input().strip()

# Get the result
result = final_position(s, t)

# Print the result
print(result)