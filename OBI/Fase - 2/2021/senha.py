c_senha, letras_escon, qnt_letras = input().split()
senha = list(input())

letras_escon = int(letras_escon)
qnt_letras = int(qnt_letras)

palavras = []
for valor in range(letras_escon):
    ordenar = list(input())
    ordenar.sort()
    ordenar = "".join(ordenar)
    palavras.append(ordenar)

senha_corr = int(input()) - 1
   
conjunto = -1  
contador = 0
verificado = 0

while senha.count("#") > 0:
    trocar = -1
    contador = 0
    
    for letra in senha:
        trocar += 1
        
        if letra == "#":
            contador += 1
            if contador == letras_escon - verificado:
                indice = senha_corr % qnt_letras
                senha[trocar] = palavras[conjunto][indice]
                
                senha_corr = senha_corr // qnt_letras
                verificado += 1
                conjunto -= 1
        
else:
    senha_certa = ""
    print(senha_certa.join(senha))