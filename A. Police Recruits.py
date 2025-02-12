def count_untreated_crimes(events):
    untreated_crimes = 0
    available_officers = 0
    
    for event in events:
        if event == -1:  # A crime occurs
            if available_officers > 0:
                available_officers -= 1  # An officer investigates the crime
            else:
                untreated_crimes += 1  # No officers available, crime goes untreated
        else:  # Positive integer, recruits officers
            available_officers += event
    
    return untreated_crimes

# Input reading
n = int(input().strip())
events = list(map(int, input().strip().split()))

# Get the result
result = count_untreated_crimes(events)

# Print the result
print(result)