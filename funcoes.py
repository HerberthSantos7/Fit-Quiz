import json

# Função para carregar os dados do quiz a partir de um arquivo JSON
def carregar_quiz(nome_arquivo, tema):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        return dados.get(tema)  # Usa .get() para evitar erro caso a chave não exista

# Função para verificar a resposta do usuário
def verificar_resposta(pergunta_index, resposta_usuario, quiz_data):
    resposta_correta = quiz_data[pergunta_index]["resposta_correta"]
    explicacao = quiz_data[pergunta_index]["explicacao"]

    # Verifica a resposta ignorando espaços em branco, maiúsculas/minúsculas
    if resposta_usuario.startswith(resposta_correta):
        return True, f"Correto! {explicacao}"
    else:
        return False, f"Errado! A resposta correta é '{resposta_correta}'. {explicacao}"
