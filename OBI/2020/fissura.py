linhas_forca = input().replace(" ", "")
linhas = int(linhas_forca[0])
forca = int(linhas_forca[1])

mapas = []

primeiro_mapa = input()
mapa_saida = ""
    
if int(primeiro_mapa[0]) < int(forca):
    mapa_saida += "*"
    primeiro_mapa = primeiro_mapa.replace(primeiro_mapa[0], "")
    
    indice = 0
    for valor in primeiro_mapa:
        if int(valor) <= int(forca) and mapa_saida[indice] == "*":
            mapa_saida += "*"
            indice += 1
        else:
            mapa_saida += valor
            indice += 1
        
    linhas -= 1
    mapas.append(mapa_saida)

    mapa = 0
    while linhas > 0:
        mapa_entrada = input()
        mapa_saida = ""
        indice = 0
        indice_mapa = 0
        
        while mapas[mapa][indice_mapa] != "*":
            mapa_entrada = list(mapa_entrada)
            mapa_saida += mapa_entrada[0]
            mapa_entrada.pop(0)
            indice_mapa += 1
            indice += 1
        
        else:
            mapa_entrada = "".join(mapa_entrada)
            for valor in mapa_entrada:    
            
                if int(valor) <= int(forca) and mapa_saida == "":
                    mapa_saida += "*"
                    indice_mapa += 1

                elif int(valor) <= int(forca) and mapa_saida[indice - 1] == "*":
                    mapa_saida += "*"
                    indice += 1
                    indice_mapa += 1
                
                elif int(valor) <= int(forca) and mapas[mapa][indice_mapa] == "*":
                    mapa_saida += "*"
                    indice += 1
                    indice_mapa += 1
                
                else:
                    mapa_saida += valor
                    indice += 1
                    indice_mapa += 1
        
        mapa += 1
        linhas -= 1
        mapas.append(mapa_saida)
    
    for mapa in mapas:
        print(mapa)

else:
    mapas.append(primeiro_mapa)
    linhas -= 1
    
    while linhas > 0:
        mapa_entrada = input()
        mapas.append(mapa_entrada)
        linhas -= 1
    
    for mapa in mapas:
        print(mapa)

""" 
8 6
27755478
29985439
34899989
22115569
66736689
99886555
44433399
99986991
"""