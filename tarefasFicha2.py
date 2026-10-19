tarefas = []

print("------- GESTAO DE TAREFAS -------\n")

while True:

    op = (int(input("Qual Operação você deseja realizar:" \
    "\n1 - Inserir uma nova tarefa ao fim" \
    "\n2 - Inserir novas tarefas ao fim" \
    "\n3 - Inserir nova tarefa em uma posição específica" \
    "\n4 - Remover tarefa pelo nome" \
    "\n5 - Remover tarefa pela posição" \
    "\n6 - Remover todas as tarefas da lista" \
    "\n7 - Contar quantas vezes uma determinada tarefa foi citada" \
    "\n8 - Ver o índex de uma tarefa" \
    "\n9 - Ordenar tarefas por ordem alfabética" \
    "\n10 - Invertes as tarefas da lista" \
    "\n11 - Fazer uma cópia independente da lista"
    "\n\nIndique a operação desejada: ")))

    if op >= 1 and op <= 11:

        match op:
            case 1: tarefas.append(input("\nQual sua próxima tarefa de hoje: "))
            case 2: tarefas.extend(input("\nQual suas próximas tarefas de hoje (divida as tarefas por ,) : ").split(','))
            case 3: tarefas.insert(int(input("\nIndique a posição para mudar uma tarefa: ")),input("Agora Indique qual sua nova tarega nessa posição: "))
            case 4: tarefas.remove(input("\nInsira o nome da tarefa que você deseja remover: "))
            case 5: 
                pos = input("\nQual posição você deseja excluir sua função (Para excluir a última diretamente pressione enter sem digitar nada): ")
                if pos == "":
                    tarefas.pop()
                else:
                    tarefas.pop(int(pos))
            case 6: 
                confirmacao = (input("\nTem certeza que deseja excluir todas as tarefas (S/N)?"))
                if confirmacao.upper() == "S":
                    tarefas.clear()
            case 7: tarefas.count(input("\nDiga a tarefa que você deseja ver quantas vezes foi citada: ): "))
            case 8: tarefas.index(input("\nDiga a tarefa que você deseja ver o índex da primeira ocorrencia: ): "))
            case 9: tarefas.sort()
            case 10: tarefas.reverse()
            case 11: tarefas.copy()

        print(f"\nSuas tarefas são: {tarefas}\n")

    else:
        print("Número inválido, Digite outra operação\n")