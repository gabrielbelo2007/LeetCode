elementos_lista = int(input())
lista = input().split()

operações = 0
indice_final = -1
elementos_analisar = elementos_lista // 2

for elemento in lista:
    while elementos_analisar > 0:
        elementos_analisar -= 1
        if elemento != lista[indice_final]:
                operações += 1
                indice_final -= 1
                break
        else:
                indice_final -= 1
                break
    else:
        break
    
print(operações)
