def min_rotations_to_print(s):
    total_rotations = 0
    current_position = 'a'
    
    for char in s:
        # Calculate the positions
        current_index = ord(current_position) - ord('a')
        target_index = ord(char) - ord('a')
        
        # Calculate clockwise and counterclockwise distances
        clockwise_distance = (target_index - current_index) % 26
        counterclockwise_distance = (current_index - target_index) % 26
        
        # Take the minimum of the two distances
        total_rotations += min(clockwise_distance, counterclockwise_distance)
        
        # Update the current position to the target character
        current_position = char
        
    return total_rotations

# Input reading
exhibit_name = input().strip()

# Get the result
result = min_rotations_to_print(exhibit_name)

# Print the result
print(result)