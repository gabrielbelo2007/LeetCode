total_amigos, qntd_reunioes = input().split()
qntd_reunioes = int(qntd_reunioes)

amigo_infec, reuniao_infec = input().split()

infectados = [amigo_infec]
num_reuniao =  1
reunioes_infectadas = False

while qntd_reunioes > 0:
    reuniao = input().split()
    reuniao.pop(0)
    
    if reunioes_infectadas == False:
        reunioes_infectadas = True if num_reuniao == int(reuniao_infec) else False
        num_reuniao += 1

    infectado_reuniao = True if set(reuniao).intersection(infectados) != set() else False
    
    if reunioes_infectadas and infectado_reuniao:
        nao_infec_reuniao = set(reuniao).difference(infectados)
        infectados += nao_infec_reuniao
        
    qntd_reunioes -= 1

if len(infectados) == 1 and infectados[0] == 0:
    print(0)
else:
    print(len(infectados))
