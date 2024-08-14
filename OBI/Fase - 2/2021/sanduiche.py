n_ingr, n_combin = input().split()
n_ingr = int(n_ingr)

inimigos = []
for valor in range(int(n_combin)):
    inimigos.append(input())
    
ingredientes = []
for valor in range(1, n_ingr + 1):
    ingredientes.append(str(valor))

sanduiches = []

sanduiche_total = ""
sanduiche_total = sanduiche_total.join(ingredientes)
sanduiches.append(sanduiche_total)

qnt_sand = n_ingr * (n_ingr - 1)
n_ingr -= 2

while n_ingr > 1:
    qnt_sand += n_ingr
    n_ingr -= 1


indice = 0
novo_indice = 1
while qnt_sand > 0:
    sanduiche_op = sanduiches[0]
    
    if indice <= len(sanduiches[0]) - 1:
        sanduiche_op = sanduiche_op.replace(sanduiche_op[indice],"")
        sanduiches.append(sanduiche_op)
    
    else:
        for valor in range (0, len(sanduiches[novo_indice])):
            sanduiche_op = sanduiche_op.replace(sanduiches[novo_indice][valor], "")
        
        sanduiches.append(sanduiche_op)
        novo_indice += 1
    
    indice += 1
    qnt_sand -= 1
    
print(sanduiches)
