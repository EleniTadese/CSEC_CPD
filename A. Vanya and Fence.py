friends_number, fence_height = map(int, input().split())
friends_heights = list(map(int, input().split()))
total_road_width = 0

for height in friends_heights:
    if height > fence_height:
        total_road_width += 2
    else:
        total_road_width += 1

# Print the minimum width of the road required
print(total_road_width)