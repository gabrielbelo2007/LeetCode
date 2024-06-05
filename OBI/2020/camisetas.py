numeros_premiados = int(input())
tamanhos_solicitados = input().replace(" ", "")
camisas_P = int(input())
camisas_M = int(input())

lista_tamanhos = [int(tamanho) for tamanho in tamanhos_solicitados]
quantas_P = lista_tamanhos.count(1)
quantas_M = lista_tamanhos.count(2)

if quantas_P == camisas_P and quantas_M == camisas_M:
    print("S")
else:
    print("N")
