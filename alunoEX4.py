aluno = {
    "Nome": "Ana Silva", 
    "Idade": 17,
    "Disciplinas": ["Matemática", "Física", "Informática"],
    "Notas": {  
        "Matemática": 18,
        "Física": 17,
        "Informática": 19
    }
}

aluno["Disciplinas"].append("Português")
aluno["Notas"]["Português"] = 16
aluno["Idade"] = 18
notas = []
media = 0

for disciplina in aluno["Disciplinas"]:
    print(disciplina)
    print(aluno["Notas"][disciplina])
    notas.append(aluno["Notas"][disciplina])
    media = round((sum(notas)/len(notas)),1)
    
print(f"A media do aluno é {media}")

