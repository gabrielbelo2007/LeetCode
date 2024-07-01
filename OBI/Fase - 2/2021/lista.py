# Somar os numeros um do lado do outro até a lista ser igual de traz para frente
# 10 60 20 40 10
# 10 60 -> 20 + 40 <- 10
# 10 60 60 10

elementos_lista = int(input())
lista = [int(numero) for numero in input().split()]

operações = 0

def verificar(lista):
    for i in range(len(lista)):
        if lista[i] == lista[-(i + 1)]:
            continue
        else:
            return False
    return True
    
indice = 0
indice_final = -1
while verificar(lista) is False:
    if lista[indice] != lista[indice_final]:
        operações += 1
        
        if indice < (len(lista) - 1):
            try:  # ANALISAR
                if lista[indice] == min(lista[indice] + lista[indice + 1], lista[indice + 1] + lista[indice + 2]):
                    lista[indice + 1] = min(lista[indice] + lista[indice + 1], lista[indice + 1] + lista[indice + 2])
                    lista.pop(indice + 2)
                else:
                    lista[indice] = lista[indice] + lista[indice + 1]
                    lista.pop(indice + 1)

            except:
                lista[indice] = lista[indice] + lista[indice + 1]
                lista.pop(indice + 1)
                
        else:
            lista[indice] = lista[indice] + lista[indice - 1]
            lista.pop(indice - 1)
            
    else:
        indice += 1
        indice_final -= 1

print(operações)
