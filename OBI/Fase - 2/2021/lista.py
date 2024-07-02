elementos_lista = int(input())
lista = [int(numero) for numero in input().split()]
    
indice = 0
indice_final = elementos_lista - 1
operacoes = 0
lista_formatada = []

while indice < indice_final:
     
    if lista[indice] == lista[indice_final]:
        
        if (indice + 1) < (indice_final - 1):
            lista_formatada.append(lista[indice])
        
        indice += 1
        indice_final -= 1
           
    elif lista[indice] > lista[indice_final]:
            
        lista[indice_final - 1] += lista[indice_final]
        lista_formatada.append(lista[indice_final - 1])
        
        indice_final -= 1
        operacoes += 1
            
    elif lista[indice] < lista[indice_final]:
            
        lista[indice + 1] += lista[indice]
        lista_formatada.append(lista[indice + 1])

        indice += 1
        operacoes += 1

print(operacoes)

# Adicional:  
print(lista_formatada)  