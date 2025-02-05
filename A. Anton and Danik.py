num = int(input())
game = input()
anthon = game.count('A')
danik = game.count('D')
if anthon > danik:
    print("Anthon")
elif anthon < danik:
    print('Danik')
else:
    print('Freindship')

