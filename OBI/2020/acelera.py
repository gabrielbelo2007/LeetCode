distancia_total = int(input())
distacia_emissor = 3

distancia_total -= distacia_emissor

distancia_receptor = distancia_total % 8

if distancia_receptor == 3:
    print(1)

elif distancia_receptor == 4:
    print(2)
    
else:
    print(3)
