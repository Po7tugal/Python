quadrados = {str(i): i*i for i in range(1,11)}
print(quadrados)

palavras = ["Alicate","Dados","Parlamento","Python","Dicionario"]
dic_palavras = {palavra: len(palavra) for palavra in palavras}
print(dic_palavras)

notas = {"Ana": 18, "Bruno": 15, "Carla": 17, "David": 12, "Eva": 19}
melhores_alunos = {aluno: nota for aluno, nota in notas.items() if nota >= 15}