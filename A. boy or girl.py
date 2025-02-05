# Read input
username = input().strip()

# Find the number of distinct characters
distinct_chars = set(username)

# Check if the count of distinct characters is odd or even
if len(distinct_chars) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
