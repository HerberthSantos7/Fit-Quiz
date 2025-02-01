import funcoes #Importa as funções do arquivo funcoes.py

if __name__ == "__main__":
    print("Bem-vindo ao Quiz! Escolha um tema:")
    print()
    print("1. Saúde Alimentar")
    print("2. Treino Físico")
    print()

    tema = int(input("Digite o número do tema escolhido: "))
    funcoes.limpar_tela(1)
    print("Prontos?")
    print("Vamos Começar!!!")
    funcoes.limpar_tela(2)

    if tema == 1:
        funcoes.executar_quiz('quiz_saude_alimentar.json', 'quiz_saude_alimentar')
    elif tema == 2:
        funcoes.executar_quiz('quiz_treino_fisico.json', 'quiz_treino_fisico')
    else:
        print("Tema inválido. Por favor, reinicie o programa e escolha um tema válido.")

