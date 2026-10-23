lista = [1,2,3,4,5,6,7,8,9,10]
palavras = ["Filipe","Sim","Programar,Aranha"]
palavras2 = "Filipe Sim,Programar"
frutas = ["Banana","Maca","Morango"]


pares = [num+1 if num < 5 else num for num in lista if num % 2 == 0]
print(pares)

quadrados = [num*num for num in lista]
print(quadrados)

letras = [len(letra) for letra in palavras]
print(letras)

numGrande = [num for num in lista if num > 5]
print(numGrande)

maiusculas = [letra for letra in palavras2 if letra == letra.upper() and letra.isspace() == False and letra != ","]
print(maiusculas)

multiplos = [num*2 if num % 3 == 0 else num for num in lista]
print(multiplos)

inicialA = [palavra.upper() for palavra in palavras if palavra.startswith("A")]

frutasGrandes = [len(fruta) if len(fruta) > 5 else 0 for fruta in frutas]
print(frutasGrandes)


