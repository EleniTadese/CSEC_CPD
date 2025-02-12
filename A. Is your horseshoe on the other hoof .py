def min_horseshoes_to_buy(s1, s2, s3, s4):
    # Use a set to find unique colors
    unique_colors = {s1, s2, s3, s4}
    # Calculate the number of horseshoes to buy
    return 4 - len(unique_colors)

# Input reading
s1, s2, s3, s4 = map(int, input().strip().split())

# Get the result
result = min_horseshoes_to_buy(s1, s2, s3, s4)

# Print the result
print(result)