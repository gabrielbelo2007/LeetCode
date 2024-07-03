numeros = [int(x) for x in input().split()]
numeros.sort()

menor_num = (numeros[1] - numeros[0] * 2) * -1 
print(menor_num)
