import json, os, time, random

# Função para limpar a tela com temporização
def limpar_tela(tempo_espera):
    time.sleep(tempo_espera)  # Espera pelo tempo especificado em segundos
    # Verifica o sistema operacional e executa o comando apropriado
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Unix/Linux/MacOS
        os.system('clear')

# Função para carregar os dados do quiz a partir de um arquivo JSON
def carregar_quiz(nome_arquivo, tema):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        return dados.get(tema)  # Usa .get() para evitar erro caso a chave não exista
    
# Função para verificar a resposta do usuário
def verificar_resposta(pergunta_index, resposta_usuario, quiz_data):
    resposta_correta = quiz_data[pergunta_index]["resposta_correta"]
    explicacao = quiz_data[pergunta_index]["explicacao"]

    if resposta_usuario.strip().lower() == resposta_correta[0].strip().lower():  # Verifica a letra da resposta correta
        return True, f"Correto! {explicacao}"
    else:
        return False, f"Errado! A resposta correta é '{resposta_correta}'. {explicacao}"

# Função principal para executar o quiz
def executar_quiz(nome, tema):
    quiz_data = carregar_quiz(nome, tema)
    
    if quiz_data is None:
        print("Erro ao carregar os dados do quiz.")
        return

    random.shuffle(quiz_data)

    score = 0

    for i, item in enumerate(quiz_data):
        pergunta = item["pergunta"]
        opcoes = item["opcoes"]

        print(f"Pergunta {i + 1}: {pergunta}")
        print()
        for opcao in opcoes:
            print(opcao)
            
        print()

        resposta_usuario = input("Sua resposta: ")
        correto, feedback = verificar_resposta(i, resposta_usuario, quiz_data)
        if correto:
            score += 1   
        print(feedback)
        limpar_tela(1)
    
    if score >= 8:
        print("Parabéns!!!")
        print(f"Você acertou {score} de {len(quiz_data)} perguntas!")
    elif score == 5:
        print("Você acertou metade, continue tentado")
        print(f"Você acertou {score} de {len(quiz_data)} perguntas!")
    else:
        print("Você acertou menos da metade, tente novamente, você consegue!!")
        print(f"Você acertou {score} de {len(quiz_data)} perguntas!")
