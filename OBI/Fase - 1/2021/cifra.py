alfa_vogais = {
    "b": "a",
    "c": "a",
    "d": "e",
    "f": "e", 
    "g": "e",
    "h": "i",
    "j": "i",
    "k": "i",
    "l": "i",
    "m": "o",
    "n": "o",
    "p": "o",
    "q": "o",
    "r": "o",
    "s": "u",
    "t": "u",
    "v": "u",
    "x": "u",
    "z": "u"
}

alfa_consoante = {
    "b": "c",
    "c": "d",
    "d": "f",
    "f": "g",
    "g": "h",
    "h": "j",
    "j": "k",
    "k": "l",
    "l": "m",
    "m": "n",
    "n": "p",
    "p": "q",
    "q": "r",
    "r": "s",
    "s": "t",
    "t": "v",
    "v": "x",
    "x": "z",
    "z": "z"
}

palavra = input()
saida = ""

for letra in palavra:
    
    if letra not in alfa_vogais.keys():
        saida += letra
        continue
    
    saida += letra
    saida += alfa_vogais[letra]
    saida += alfa_consoante[letra]

print(saida)
