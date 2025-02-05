n = int(input().strip())  # Number of magnets
previous = input().strip()  # First magnet (Starts first group)
groups = 1  # At least one group always

for _ in range(n - 1):
    current = input().strip()
    if current != previous:  # If different, new group starts
        groups += 1
    previous = current  # Update previous magnet

print(groups)
