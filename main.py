from recursos import crud,interface,arquivos

def main():
    tarefas= arquivos.carregar_tarefas()
    
    while True:
        
        opcao = interface.menu()
        
        if opcao=='1':
            titulo_tarefa=input("Digite a nova tarefa: ")
            crud.adicionar_tarefas(tarefas,titulo_tarefa)
        
        elif opcao=='2':
            crud.mostrar_tarefas(tarefas)
        
        elif opcao=="3":
            indice=int(input("Número da tarefa concluída: "))-1
            crud.concluir_tarefa(tarefas,indice)
        
        elif opcao=='4':
            indice=int(input("Número da tarefa para remover: "))-1
            crud.remover_tarefa(tarefas,indice)
            
        elif opcao=='5':
            print('saindo...')
            break
        
        else:
            print('opção invalida')
            
if __name__ == "__main__":
    main()