# Read input
s = input().strip()

# Count uppercase and lowercase letters
upper_count = sum(1 for c in s if c.isupper())
lower_count = len(s) - upper_count  # Remaining are lowercase letters

# Convert based on the count
if upper_count > lower_count:
    print(s.upper())
else:
    print(s.lower())
