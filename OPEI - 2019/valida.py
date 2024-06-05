N = input().strip()

contador = 2
multiplo_10 = 0
for valor in N: 
    if contador % 2 == 0:
        multiplicacao = int(valor) * 2
        contador += 1
        
        if multiplicacao >= 10:
            multiplicacao = str(multiplicacao)
            multiplo_10 += int(multiplicacao[0]) + int(multiplicacao[1])
        
        else:
            multiplo_10 += multiplicacao
            
    else:
        multiplo_10 += int(valor) * 1
        contador += 1

S = "SIM" if multiplo_10 % 10 == 0 else "NAO"
print(S)
