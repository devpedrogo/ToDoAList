from database import create_table
from tarefa import adicionar_tarefa, concluir_tarefa, listar_tarefas, excluir_tarefa, listar_filtro

if __name__ == "__main__":
    create_table()
    while True:
        opcao = int(input("\nEscolha uma opção: \n1 - Adicionar Tarefa\n2 - Listar Tarefas\n3 - Concluir Tarefa\n4 - Excluir Tarefa\n5 - Sair\n--> "))

        if opcao == 1:
            print("\n--- Adicionar Nova Tarefa ---")

            titulo = input("Título da tarefa: ").strip()
            descricao = input("Descrição: ").strip()
            prioridade = int(input("Prioridade da tarefa (1: Baixa, 2: Média, 3: Alta): "))

            adicionar_tarefa(titulo, descricao, prioridade)

        elif opcao == 2:
            print("\n--- Opções de Listagem ---")
            print("1: Listar todas as tarefas")
            print("2: Filtrar por Prioridade (Baixa, Média, Alta)")
            print("3: Filtrar por Status (Pendente ou Concluída)")

            opcao = int(input("Escolha uma opção (1-3): "))

            if opcao == 1:
                listar_tarefas()

            elif opcao == 2:
                print("\n--- Filtrar por Prioridade ---")
                print("1: Baixa | 2: Média | 3: Alta")
                while True:
                    prioridade = int(input("Digite o número da prioridade para filtrar: "))
                    try:
                        if 1 <= prioridade <= 3:
                            listar_filtro(filtro_prioridade=prioridade, filtro_status=None)
                            break
                        else:
                            print("ERRO! Escolha inválida. Use 1, 2 ou 3.")
                    except ValueError:
                        print("ERRO! Entrada inválida. Digite um número.")

            elif opcao == 3:
                print("\n--- Filtrar por Status ---")
                print("0: Pendente | 1: Concluída")
                while True:
                    status = int(input("Digite o número do status para filtrar (0 ou 1): "))
                    try:
                        if status in [0, 1]:
                            listar_filtro(filtro_prioridade=None, filtro_status=status)
                            break
                        else:
                            print("ERRO! Escolha inválida. Use 0 ou 1.")
                    except ValueError:
                        print("ERRO! Entrada inválida. Digite um número.")

            else:
                print("AVISO! Opção inválida.")

        elif opcao == 3:
            listar_tarefas()
            id_escolhido = int(input("Digite o id da tarefa que desejas concluir: "))
            concluir_tarefa(id_escolhido)

        elif opcao == 4:
            listar_tarefas()
            id_escolhido = int(input("Digite o id da tarefa que desejas excluir: "))
            excluir_tarefa(id_escolhido)

        elif opcao == 5:
            print("... Programa finalizado!")
            break