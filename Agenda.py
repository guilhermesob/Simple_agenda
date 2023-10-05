agenda = {}  # Inicializa um dicionário vazio para a agenda

def adicionar_evento():
    data = input("Digite a data do evento (formato DD/MM/AAAA): ")
    evento = input("Digite o nome do evento: ")
    
    if data in agenda:
        # Se a data já estiver na agenda, adiciona o evento à lista existente
        agenda[data].append(evento)
    else:
        # Se a data não estiver na agenda, cria uma nova lista com o evento
        agenda[data] = [evento]
    
    print("Evento adicionado com sucesso!")

def mostrar_agenda():
    print("\n--- Agenda ---")
    for data, eventos in agenda.items():
        print(f"{data}:")
        for evento in eventos:
            print(f"- {evento}")
    print("---\n")

objetivos = {
    "Manhã": ["Alongamentos", "Banho e escovação dos dentes", "Café da manhã e preparação para a academia"],
    "Atividades Físicas": ["Primeira corrida", "Treino na academia", "Alongamentos pós-treino", "Visitar pessoas próximas", "Shake de proteína e banho", "Estacas ou atividades semelhantes"],
    "Meio-Dia": ["Almoço", "Revisão pós-almoço"],
    "Tarde": ["Trabalho em engenharia de software e estudo de redes", "Atividades físicas (shadow box e capoeira com idiomas)", "Estacas ou atividades semelhantes", "Continuação do trabalho em engenharia de software e redes", "Jantar"],
    "Noite": ["Desenho (a cada dois dias)", "Tempo livre / relaxamento", "Hora de dormir"],
}

tarefas_concluidas = {meta: [] for meta in objetivos}
pontuacao = 0

def exibir_objetivos_e_tarefas():
    global pontuacao
    for meta, tarefas in objetivos.items():
        print(f"{meta}:")
        for i, tarefa in enumerate(tarefas, start=1):
            status = "[X]" if tarefa in tarefas_concluidas.get(meta, []) else "[ ]"
            print(f"  {i}. {status} {tarefa}")
        pontuacao += len(tarefas_concluidas.get(meta, []))

def marcar_tarefas():
    global pontuacao
    meta_selecionada = input("Digite o nome do objetivo: ")
    tarefas_selecionadas = input("Digite os números das tarefas a marcar como concluídas (separados por vírgula): ")
    tarefas_selecionadas = list(map(int, tarefas_selecionadas.split(",")))

    if meta_selecionada in objetivos:
        for tarefa_num in tarefas_selecionadas:
            if 0 < tarefa_num <= len(objetivos[meta_selecionada]):
                tarefa = objetivos[meta_selecionada][tarefa_num - 1]
                if tarefa not in tarefas_concluidas[meta_selecionada]:
                    tarefas_concluidas[meta_selecionada].append(tarefa)
                    print(f"Tarefa '{tarefa}' marcada como concluída em '{meta_selecionada}'.")
                    pontuacao += 1
                else:
                    print(f"Tarefa '{tarefa}' já está marcada como concluída.")
            else:
                print(f"Número de tarefa inválido: {tarefa_num}")
    else:
        print("Objetivo inválido.")

def desmarcar_tarefas():
    global pontuacao
    meta_selecionada = input("Digite o nome do objetivo: ")
    tarefas_selecionadas = input("Digite os números das tarefas a desmarcar como concluídas (separados por vírgula): ")
    tarefas_selecionadas = list(map(int, tarefas_selecionadas.split(",")))

    if meta_selecionada in objetivos:
        for tarefa_num in tarefas_selecionadas:
            if 0 < tarefa_num <= len(objetivos[meta_selecionada]):
                tarefa = objetivos[meta_selecionada][tarefa_num - 1]
                if tarefa in tarefas_concluidas[meta_selecionada]:
                    tarefas_concluidas[meta_selecionada].remove(tarefa)
                    print(f"Tarefa '{tarefa}' desmarcada como não concluída em '{meta_selecionada}'.")
                    pontuacao -= 1
                else:
                    print(f"Tarefa '{tarefa}' não estava marcada como concluída.")
            else:
                print(f"Número de tarefa inválido: {tarefa_num}")
    else:
        print("Objetivo inválido.")

while True:
    print("\n** Agenda, Objetivos e Tarefas **")
    print("Escolha uma opção:")
    print("1. Adicionar evento à agenda")
    print("2. Mostrar agenda")
    print("3. Exibir objetivos e tarefas")
    print("4. Marcar tarefas como concluídas")
    print("5. Desmarcar tarefas como não concluídas")
    print("6. Sair")

    escolha = input("Digite o número da opção: ")

    if escolha == "1":
        adicionar_evento()
    elif escolha == "2":
        mostrar_agenda()
    elif escolha == "3":
        exibir_objetivos_e_tarefas()
        print(f"Pontuação atual: {pontuacao}")
    elif escolha == "4":
        marcar_tarefas()
    elif escolha == "5":
        desmarcar_tarefas()
    elif escolha == "6":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
