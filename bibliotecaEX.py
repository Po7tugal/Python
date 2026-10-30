biblioteca = {
    "livro1": {
        "titulo": "Python Fluente",
        "autor": "Luciano Ramalho",
        "ano": 2015,
        "disponivel": True
    },
    "livro2": {
        "titulo": "Pense em Python",
        "autor": "Allen B. Downey",
        "ano": 2012,
        "disponivel": False
    },
    "livro3": {
        "titulo": "Introdução à Programação com Python",
        "autor": "Nilo Ney Coutinho Menezes",
        "ano": 2019,
        "disponivel": True
    }
}

titulos = []

for livro in biblioteca.values():
    print(livro["titulo"])
    if livro["autor"] == "Luciano Ramalho":
        titulos.append(livro["titulo"])

biblioteca["livro4"] = {
    "titulo": "Continuação à Programação com Python",
    "autor": "Filipe Marques da Costa",
    "ano": 2017,
    "disponivel": True
}

print(f"---------------- BIBLIOTECA ------------------\n\n{biblioteca}")
print(f"\nTítulos do livro escrito por Luiano Ramalho: {titulos}")

