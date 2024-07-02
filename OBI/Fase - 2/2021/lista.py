elementos_lista = int(input())
lista = [int(numero) for numero in input().split()]
    
indice = 0
indice_final = elementos_lista - 1
operacoes = 0

while indice < indice_final:
     
    if lista[indice] == lista[indice_final]:
        
        indice += 1
        indice_final -= 1
           
    elif lista[indice] > lista[indice_final]:
            
        lista[indice_final - 1] += lista[indice_final]
        
        indice_final -= 1
        operacoes += 1
            
    elif lista[indice] < lista[indice_final]:
            
        lista[indice + 1] += lista[indice]

        indice += 1
        operacoes += 1
   
print(operacoes)
