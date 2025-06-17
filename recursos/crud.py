def adicionar_tarefas(tarefas,titulo):
    tarefas.append({'titulo':titulo,'status':False})
    
def mostrar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa.")
    for i, tarefa in enumerate(tarefas):
        status = "✔" if tarefa['concluida'] else "✘"
        print(f"{i} - {tarefa['titulo']} [{status}]")
        
def concluir_tarefa(tarefas, indice):
    tarefas[indice]['status'] = True        

def remover_tarefa(tarefas,indice):
    del tarefas[indice]