entrada = input()
numero_registros = int(entrada)
registros_salvos = []

while numero_registros > 0:
    
    recebe_registros = input().split(" ")
    registros_salvos.append(recebe_registros)
    numero_registros -= 1
    
print(registros_salvos)

saida = []
amigos_visualizados = []

for registro in registros_salvos:
    
    # Impede a verificação dos valores de "enviado", de "tempo" e de amigos já conferidos
    if registro[0] in ["E", "T"]:
        continue
    elif registro[1] in amigos_visualizados:
        continue
    
    # Calcula se o amigo teve resposta
    respondeu_amigo = 0
    for checar_resposta in registros_salvos:
        if checar_resposta[1] == registro[1] and checar_resposta[0] != "T":
            respondeu_amigo += 1
    
    tempo_resposta = 0
    if respondeu_amigo % 2 == 0:  # Executado se o amigo foi respondido
        
        # Contar o tempo de resposta
        quantas_respostas = respondeu_amigo / 2
        while quantas_respostas > 0:  # NAO ESTA PARANDO DE SER EXECUTADO!! (RESOLVER)
            for checar_tempo in registros_salvos:
                # Executado enquanto ainda tiver tempo de resposta para esse amigo
                    
                    # Quando chega em uma resposta enviada para o amigo
                    if checar_tempo[0] == "E" and checar_tempo[1] == registro[1]:
                        quantas_respostas -= 1
                    
                    # Quando tem tempo adicional
                    elif checar_tempo[0] == "T": 
                        tempo_resposta += int(checar_tempo[1])\
                    
                    # Quando é apenas um registro
                    else:
                        tempo_resposta += 1
            else:
                break
              
        saida += registro[1] + " " + str(tempo_resposta)
         
    else:  # Executado se o amigo não foi respondido
        saida += registro[1] + "-1"
        amigos_visualizados.append(registro[1])

print(saida)
