soma_algarismos = int(input())
inicio_intervalo = int(input())
fim_intervalo = int(input())

qnts_somas = 0
for valor in range(inicio_intervalo, fim_intervalo + 1):
    valor = str(valor)
    
    total = 0
    for algarimos in valor:
        total += int(algarimos)
    
    if total == soma_algarismos:
        qnts_somas += 1

print(qnts_somas)
