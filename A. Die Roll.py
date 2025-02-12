from math import gcd

def calculate_probability(Y, W):
    # Determine the highest roll
    max_roll = max(Y, W)
    # Calculate successful outcomes
    successful_outcomes = 6 - max_roll + 1
    total_outcomes = 6

    # Reduce the fraction
    divisor = gcd(successful_outcomes, total_outcomes)
    numerator = successful_outcomes // divisor
    denominator = total_outcomes // divisor
    
    return f"{numerator}/{denominator}"

# Input reading
Y, W = map(int, input().strip().split())

# Get the result
result = calculate_probability(Y, W)

# Print the result
print(result)