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
        print(anagrama)
        break

else:
    print("*")

# 4
# xyyy -> xy 
# correto = "*"