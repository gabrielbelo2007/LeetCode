quantos_numeros = int(input())

numeros_registrados = []
while quantos_numeros > 0:
    numero = int(input())
    
    if numero != 0:
        numeros_registrados.append(numero)
        quantos_numeros -= 1
    
    else:
        numeros_registrados.pop()
        quantos_numeros -= 1
        

if numeros_registrados != []:
    soma = 0
    for valor in numeros_registrados:
        soma += valor
    print(soma)
else:
    print(0)
