escola = {
    "aluno1": {
        "nome": "Ana Silva",
        "idade": 17,
        "cidade": "Porto",
        "curso": "Programador",
        "notas": {
            "Python": 18,
            "Excel": 16,
            "SQL": 15
        },
        "contacto": {
            "email": "ana@email.com",
            "telefone": "912345678"
        }
    },

    "aluno2": {
        "nome": "João Costa",
        "idade": 18,
        "cidade": "Braga",
        "curso": "Programador",
        "notas": {
            "Python": 14,
            "Excel": 17,
            "SQL": 16
        },
        "contacto": {
            "email": "joao@email.com",
            "telefone": "923456789"
        }
    },

    "aluno3": {
        "nome": "Maria Santos",
        "idade": 16,
        "cidade": "Aveiro",
        "curso": "Programador",
        "notas": {
            "Python": 19,
            "Excel": 18,
            "SQL": 20,
            "Extra": 16
        },
        "contacto": {
            "email": "maria@email.com",
            "telefone": "934567890"
        }
    }
}

media_idades_alunos = 0.0
soma_idades = 0

for aluno in escola.values():
    soma_idades +=  aluno["idade"]
media_idades_alunos = round(soma_idades / len(escola),2)
print(media_idades_alunos)

# Imprima o Nome do aluno e a Média

for aluno in escola.values():
    nome_aluno = aluno["nome"]
    notas_aluno = []
    for nota in aluno["notas"].values():
        notas_aluno.append(nota)
    media = round(sum(notas_aluno)/len(notas_aluno),1)
    print(f"Aluno(a) {nome_aluno} teve a média de {media} valores")

# Alunos do Porto

escola_porto = {}

for chave, valor in escola.items():
    if valor["cidade"] == "Porto":
        escola_porto[chave] = valor

# Dicitionary Comprehension
escola_porto2 = {chave:valor for chave, valor in escola.items() if valor["cidade"] == "Porto"}