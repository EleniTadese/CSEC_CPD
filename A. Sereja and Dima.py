def card_game(n, cards):
    sereja_score = 0
    dima_score = 0
    left = 0
    right = n - 1
    turn = 0  # 0 for Sereja's turn, 1 for Dima's turn
    
    while left <= right:
        if cards[left] > cards[right]:
            chosen_card = cards[left]
            left += 1
        else:
            chosen_card = cards[right]
            right -= 1
        
        if turn == 0:  # Sereja's turn
            sereja_score += chosen_card
        else:  # Dima's turn
            dima_score += chosen_card
        
        turn = 1 - turn  # Switch turns
    
    return sereja_score, dima_score

# Input reading
n = int(input().strip())
cards = list(map(int, input().strip().split()))

# Get the result
sereja_points, dima_points = card_game(n, cards)

# Print the result
print(sereja_points, dima_points)