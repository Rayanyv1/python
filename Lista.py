
## Funcionalidades Atuais

* Adicionar novas tarefas à lista.
* Listar todas as tarefas pendentes.
* Marcar tarefas como concluídas.
* Remover tarefas da lista.



# Criar uma lista 
tarefas = []

#Função pra mostrar menu 
def mostrar_menu():

    print("\n=== Lista de Tarefas ===")
    print("1. ver tarefas")
    print("2. Adicionar tarefas")
    print("3. Remover tarefas")
    print("4. Sair")

#loop princcipal 
while True:
    mostrar_menu()
    escolha = input("Escolha uma opção:")

    if escolha == "1":
        if not tarefas:
            print("Nenhuma tarefa na lista!")
        else:
            print("\ntarefas:")
            for i, tarefas in enumerate(tarefas, start=1):
                print(f"{i}, {tarefas}")
    
    elif escolha == "2":
        nova_tarefa = input("Digite uma nova tarefa: ")
        tarefas.append(nova_tarefa)
        print("tarefa adicionada")
    
    elif escolha == "3":
        if not tarefas:
            print("nenhuma tarefa para remover!")
        else:
            for i, tarefas in enumerate(tarefas, start=1):
                print(f"{i}, {tarefas}")
        numero = int(input("Digite o numero de tarefa para remover: "))
        if 1 <= numero <= len(tarefas):
            removida = tarefas.pop(numero -1)
            print(f"Tarefa '{removida}' removida!")
        else:
            print("Numero innvalido")
    elif escolha == "4":
        print("Saindo... ate mais!")
        break
    else:
        print("Opção invalida, tente novamente")