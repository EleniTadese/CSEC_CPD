def years_to_surpass(limak_weight, bob_weight):
    
    years = 0  
    while limak_weight <= bob_weight:
        limak_weight *= 3  
        bob_weight *= 2    
        years += 1         
    
    return years  

limak_weight, bob_weight = map(int, input().split())
print(years_to_surpass(limak_weight, bob_weight))
