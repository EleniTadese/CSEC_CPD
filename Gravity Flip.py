
def gravity_flip(n, cubes):

    cubes.sort()
  
    return cubes


n = int(input())  
cubes = list(map(int, input().split()))  


result = gravity_flip(n, cubes)


print(*result)
