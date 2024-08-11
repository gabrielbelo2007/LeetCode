c_senha, letras_escon, qnt_letras = input().split()
senha = input()

letras_escon = int(letras_escon)
qnt_letras = int(qnt_letras)

palavras = []
for valor in range(letras_escon):
    palavras.append(input())
 
senha_corr = int(input())
tentativas = letras_escon * qnt_letras

letra_c1 = 0
letra_cN = 0
contagem_letras = 0

senhas_testadas = []
while tentativas > 0:
    senha_verif = ""
    conjunto = 0

    for caracter in senha:
        if caracter == "#" and conjunto == 0:
            if contagem_letras % letras_escon == 0 and contagem_letras != 0:
                    letra_c1 += 1
                    letra_cN = 0
            
            senha_verif += palavras[conjunto][letra_c1]
            
            contagem_letras += 1
            if conjunto < letras_escon:
                conjunto += 1
        
        elif caracter == "#":
            senha_verif += palavras[conjunto][letra_cN]
            
            if conjunto < letras_escon - 1:
                conjunto += 1
            else:
                letra_cN += 1

        else:
            senha_verif += caracter
    
    tentativas -= 1
    senhas_testadas.append(senha_verif)

senhas_testadas.sort()
print(senhas_testadas[senha_corr - 1])
