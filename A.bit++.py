
# Read the number of statements
n = int(input())
 
# Initialize x
x = 0
 
# Process each statement
for _ in range(n):
    statement = input().strip()
    if '++' in statement:
        x += 1
    elif '--' in statement:
        x -= 1
 
# Print the final value of x
print(x)