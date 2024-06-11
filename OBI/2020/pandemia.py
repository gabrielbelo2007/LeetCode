total_amigos, qntd_reunioes = input().split()
qntd_reunioes = int(qntd_reunioes)

amigo_infec, reuniao_infec = input().split()

infectados = []
num_reuniao =  1
reunioes_infectadas = False

while qntd_reunioes > 0:
    reuniao = input().split()
    
    if num_reuniao == int(reuniao_infec):
        reunioes_infectadas = True
    else:
        num_reuniao += 1
    
    reuniao.pop(0)
    
    if reunioes_infectadas and amigo_infec in reuniao:
        
        for amigo in reuniao:
            if amigo not in infectados:
                infectados += amigo
            
    elif set(reuniao).intersection(infectados): 
        
        for amigo in reuniao:
            if amigo not in infectados:
                infectados += amigo
  
    qntd_reunioes -= 1

print(len(infectados))
