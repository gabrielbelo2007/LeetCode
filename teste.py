palavra = "abc"
numero = palavra.count("d")
print(numero)

"""
for valor in divisores_total:
    anagrama = palavra[0:int(valor)]
    
    anagrama_letras = set(anagrama)
    nova_palavra = palavra
    for letra in anagrama_letras:
        nova_palavra = nova_palavra.replace(letra, "")
        
        if nova_palavra == "":
            contador = 0
            verificar = palavra[int(valor):(int(valor)*2)]
            for letra in anagrama_letras:
                if letra in verificar:
                    contador += 1
            if contador == len(anagrama_letras): 
                print(anagrama)
                break
            else:
                print("*")
                break
"""