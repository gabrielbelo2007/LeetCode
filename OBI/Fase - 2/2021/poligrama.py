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

for divisor in divisores_total:
    rodar = qnt_letras // int(divisor) - 1
    checar = rodar
    certo = 0
    
    anagrama = palavra[0:int(divisor)]
        
    anagrama_letras = set(anagrama)
    nova_palavra = palavra
    for letra in anagrama_letras:
        nova_palavra = nova_palavra.replace(letra, "")
    
    valor = 0       
    if nova_palavra == "": 
        while rodar > 0:
            valor += 1
            
            inicio = int(divisor) * valor
            final =  int(divisor) * (valor + 1)
                    
            anagrama_2 = palavra[inicio:final]   
                    
            contador = 0
            for letra in anagrama_letras:
                if anagrama_2.count(letra) == anagrama.count(letra):
                    contador += 1
                    
            if contador == len(anagrama_letras):
                certo += 1
                rodar -= 1
                
            else:
                rodar = 0
                break
                
        if certo == checar:
            print(anagrama)
            break
else:
    print("*")