numero_registros = int(input())
registros_salvos = []

while numero_registros > 0:
    
    recebe_registros = input().split(" ")
    registros_salvos.append(recebe_registros)
    numero_registros -= 1
    
registros_restantes = [valor for valor in registros_salvos]

saida = []
amigos_visualizados = []

for registro in registros_salvos:
    
    # Impede a verificação dos valores de "enviado", de "tempo" e de amigos já conferidos
    if registro[0] in ["E", "T"] or registro[1] in amigos_visualizados:
        registros_restantes.pop(0)
        continue
    
    # Calcula se o amigo teve resposta
    respondeu_amigo = 0
    for checar_resposta in registros_salvos:
        if checar_resposta[1] == registro[1] and checar_resposta[0] != "T":
            respondeu_amigo += 1
    
    tempo_resposta = 0
    if respondeu_amigo % 2 == 0:  # Executado se o amigo foi respondido

        quantas_respostas = respondeu_amigo / 2  # Contar quantas respostas ele teve
        teve_T = False
        
        for checar_tempo in registros_restantes:
            # Executado enquanto ainda tiver respostas para esse amigo
            if quantas_respostas > 0:
                # Quando chega em uma resposta enviada para o amigo
                if checar_tempo[0] == "E" and checar_tempo[1] == registro[1]:
                    quantas_respostas -= 1
                    if teve_T == False: # Caso a resposta venha logo apos o tempo adicional nao contar tempo a mais
                        tempo_resposta += 1
                    teve_T = False
                    
                    # Quando tem tempo adicional
                elif checar_tempo[0] == "T": 
                    tempo_resposta += int(checar_tempo[1])
                    teve_T = True
                    
                    # Quando é apenas um registro
                elif checar_tempo[1] != registro[1]:
                    if teve_T == True:  # Conferindo se o registro veio seguido de tempo adicional
                        teve_T = False 
                        continue
                    else:
                        tempo_resposta += 1
            else:
                break
        
        # Adicionando o amigo + o seu tempo de resposta
        saida.append(registro[1] + " " + str(tempo_resposta))
        amigos_visualizados.append(registro[1])
        registros_restantes.pop(0)

    else:  # Adicionando o amigo que não foi respondido
        saida.append(registro[1] + " " + "-1")
        amigos_visualizados.append(registro[1])
        registros_restantes.pop(0)

saida.sort()
for valor in saida:
    print(valor)
