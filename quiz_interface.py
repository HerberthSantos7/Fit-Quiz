import tkinter as tk
from tkinter import messagebox
import funcoes
import random

class QuizInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Fit Quiz")
        self.root.geometry("650x450")  # Define o tamanho da janela (largura x altura)
        self.root.resizable(False, False)  # Desativa a opção de redimensionamento

        self.show_initial_screen()

    def show_initial_screen(self):
        self.clear_frame()
        self.initial_label = tk.Label(self.root, text="Bem-vindo ao Fit Quiz!", font=("Helvetica", 20))
        self.initial_label.pack(pady=40)

        self.start_button = tk.Button(self.root, text="Novo Jogo", command=self.choose_theme, font=("Helvetica", 14))
        self.start_button.pack(pady=20)

        self.exit_button = tk.Button(self.root, text="Sair", command=self.root.quit, font=("Helvetica", 14))
        self.exit_button.pack(pady=20)

    def choose_theme(self):
        self.clear_frame()
        self.theme_label = tk.Label(self.root, text="Escolha um tema:", font=("Helvetica", 14))
        self.theme_label.pack(pady=20)

        self.theme_var = tk.StringVar(value="1")
        themes = [("Saúde Alimentar", "quiz_saude_alimentar"), ("Treino Físico", "quiz_treino_fisico")]
        for theme, value in themes:
            radio = tk.Radiobutton(self.root, text=theme, variable=self.theme_var, value=value, font=("Helvetica", 12))
            radio.pack(anchor="center", pady=5)

        self.start_button = tk.Button(self.root, text="Começar", command=self.start_quiz, font=("Helvetica", 12))
        self.start_button.pack(pady=20)

    def start_quiz(self):
        tema = self.theme_var.get()
        self.iniciar_quiz(f'{tema}.json', tema)

    def iniciar_quiz(self, arquivo, tema):
        perguntas = funcoes.carregar_quiz(arquivo, tema)
        if perguntas is None:
            messagebox.showerror("Erro", "Erro ao carregar os dados do quiz.")
            return

        self.clear_frame()
        self.app = QuizApp(self.root, perguntas)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

class QuizApp:
    def __init__(self, root, perguntas):
        self.root = root
        self.score = 0
        self.perguntas = perguntas
        random.shuffle(self.perguntas)
        self.current_question = 0

        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack(expand=True, fill="both")

        self.question_label = tk.Label(self.frame, text=self.perguntas[self.current_question]["pergunta"], wraplength=600, justify="center", font=("Helvetica", 14))
        self.question_label.pack(pady=10, anchor="center")

        self.selected_answer = tk.StringVar()  # Variável para armazenar a resposta selecionada
        self.radio_frame = tk.Frame(self.frame)
        self.radio_frame.pack(anchor="center")

        self.create_radio_buttons()

        self.submit_button = tk.Button(self.frame, text="Próxima Pergunta", command=self.check_answer, font=("Helvetica", 12))
        self.submit_button.pack(pady=20, anchor="center")

    def create_radio_buttons(self):
        self.choice_vars = []
        self.radio_buttons = []
        for choice in self.perguntas[self.current_question]["opcoes"]:
            radio = tk.Radiobutton(self.radio_frame, text=choice, variable=self.selected_answer, value=choice, wraplength=600, justify="left", font=("Helvetica", 12))
            radio.pack(anchor="w", pady=5)
            self.radio_buttons.append(radio)

    def check_answer(self):
        selected_choice = self.selected_answer.get()
        if not selected_choice:
            messagebox.showwarning("Aviso", "Por favor, selecione uma opção.")
            return

        correto, feedback = funcoes.verificar_resposta(self.current_question, selected_choice, self.perguntas)

        if correto:
            self.score += 1

        messagebox.showinfo("Resultado", feedback)
        self.current_question += 1

        if self.current_question < len(self.perguntas):
            self.update_question()
        else:
            messagebox.showinfo("Quiz Finalizado", f"Sua pontuação final é: {self.score}")
            self.root.quit()

    def update_question(self):
        self.question_label.config(text=self.perguntas[self.current_question]["pergunta"])
        self.selected_answer.set("")  # Limpa a seleção para a próxima pergunta
        for radio in self.radio_buttons:
            radio.destroy()
        self.create_radio_buttons()

def iniciar_quiz():
    root = tk.Tk()
    app = QuizInterface(root)
    root.mainloop()
