def count_guest_uniform_games(n, uniforms):
    count = 0

    # Iterate over each pair of teams
    for i in range(n):
        home_color = uniforms[i][0]  # Home uniform color of the host team
        for j in range(n):
            if i != j:  # Ensure we are not comparing the same team
                guest_color = uniforms[j][1]  # Guest uniform color of the guest team
                if home_color == guest_color:
                    count += 1  # Increment count if colors match

    return count

# Input reading
n = int(input().strip())
uniforms = [tuple(map(int, input().strip().split())) for _ in range(n)]

# Get the result
result = count_guest_uniform_games(n, uniforms)

# Print the result
print(result)