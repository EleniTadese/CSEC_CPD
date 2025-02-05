
def beautiful_matrix(matrix):
    center_x, center_y = 2, 2
    
  
    for i in range(5):
        for j in range(5):
         
            if matrix[i][j] == 1:
                return abs(i - center_x) + abs(j - center_y)  
    

matrix = [list(map(int, input().split())) for _ in range(5)]

print(beautiful_matrix(matrix))
