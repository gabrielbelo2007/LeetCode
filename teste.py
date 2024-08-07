#letras_diferentes = 0
#letras_usadas = ""
#for letra in palavra:
    
#    if letra not in letras_usadas:
#        letras_diferentes += 1
#        letras_usadas += letra

#maior = 0
#letra_salva = 0
#for letra in letras_usadas:
#    contagem = palavra.count(letra)
#    maior = contagem if contagem > maior else maior
#   letra_salva = letra if maior == contagem else letra_salva

#print(letras_diferentes, maior, letra_salva)

palavra = "yx"

if "xy" in palavra:
    print("sim")
