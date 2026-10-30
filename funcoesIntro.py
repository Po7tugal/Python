def saudacao(nome: str,curso="GPSI"):
    print(f"Bem Vindo ao curso de {curso}, {nome}")

saudacao("Carlos")
print(saudacao)

# def criar_lista(aluno1,aluno2):
#    lista = []
#    lista.append(aluno1)
#    lista.append(aluno2)
#    return lista

def criar_lista(*alunos):
    lista = []
    for aluno in alunos:
        lista.append(aluno)
    return lista

# print(criar_lista("Ana","João"))
x = criar_lista("Ana","João")
y = criar_lista("Ana","João","Claudio","Rui","Mario")
z = ["A1","A2","A3","A4"]
nova_lista = criar_lista(*z)
print(x,y,z)

def config(**configuracoes):
    for chave,valor in configuracoes.items():
        print(f"{chave}: {valor}")

config(memoria="16GB",disco="SSD 256GB",sistema="Windows 11")

dicionario = { "memoria": "8GB", "disco": "SSD 512GB","sistema": "Ubuntu" }
config(**dicionario)

def maiores_dois_valores(n1,n2,n3):
    maior = n1
    maior2 = 0
    if n2 > maior and n2 > n3:
        maior = n2
        if n1 > n3:
            maior2 = n1
        else:
            maior2 = n3

        return (maior, maior2)