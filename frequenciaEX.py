texto = "Filipe Portugal"

contagem = {}

for letra in texto:
    letra = letra.lower()
    if letra.isspace() == False:
        if letra in contagem.keys():
            contagem[letra] += 1
        else:
            contagem[letra] = 1

print(contagem)