c_senha, letras_escon, palavras = input().split()
senha = input().split()
letras_escon = int(letras_escon)

letras_poss = []
while letras_escon > 0:
    letras_poss.append(input())
    letras_escon -= 1
    
senha_corr = int(input())

indice = 0
while senha_corr > 0:
    for letra in senha:
        if letra == "#":
            letras_escon.insert(indice, letras_poss)  # ALTERAR
            indice += 1
            letras_escon.pop(indice)
        else:
            indice += 1
    
    senha_corr -= 1
