qnt_letras = int(input())
palavra = input()

# Divisores totais da palavra

def dividir(num):
    divisores = []
    for i in range(1, num//2+1):
        if num % i == 0: 
            divisores.append(str(i))
    return divisores

divisores_total = dividir(qnt_letras)

# Separar a palavra em anagramas

for valor in divisores_total:
    anagrama = palavra[0:int(valor)]
    
    anagrama_letras = set(anagrama)
    nova_palavra = palavra
    for letra in anagrama_letras:
        nova_palavra = nova_palavra.replace(letra, "")
        
    if nova_palavra == "": 
        anagrama_2 = palavra[int(valor):int(valor)*2]   
        
        contador = 0
        for letra in anagrama_letras:
            if anagrama_2.count(letra) == anagrama.count(letra):
                contador += 1

        if contador == len(anagrama_letras):
            print(anagrama)
            break

else:
    print("*")