from tkinter import *

class Principal:
    def __init__(self, window):
        self.window = window
        self.window.title("Thiago Costa")
        texto = Label(self.window, text="Escolha o que quer saber:")
        texto.grid(column=1, row=0, padx=10, pady=10)

        botao = Button(self.window, text="Hobbies", command=self.printar_hobbies)
        botao.grid(column=0, row=1, padx=10, pady=10)

        botao = Button(self.window, text="Habilidades", command=self.printar_habilidades)
        botao.grid(column=2, row=1, padx=10, pady=10)

    def printar_hobbies(self):
        new = Toplevel(self.window)
        Secundaria(new, False)

    def printar_habilidades(self):
        new = Toplevel(self.window)
        Secundaria(new, True)

class Secundaria:
    def __init__(self, window, var):
        self.window = window
        if var:
            self.habilidades()
        else:
            self.hobbies()
    
    def habilidades(self):
        self.window.title("Habilidades")
        Habilidades = ("Programação", "Trabalho em equipe", "Dedicação", "Rápido aprendizado")
        for a in range(len(Habilidades)):
            texto_resposta = Label(self.window, text=Habilidades[a])
            texto_resposta.grid(column=0, row=a, padx=100, pady=10)
        button = Button(self.window, text="Voltar", command=self.go_back)
        button.grid(column=0, row=len(Habilidades)+1, pady=10)

    def hobbies(self):
        self.window.title("Hobbies")
        Hobbies = ("Jogar com amigos (Esportes ou Eletrônicos)", "Tocar violão", "Assistir séries/animes", "Passar um tempo com a namorada\n")
        for a in range(len(Hobbies)):
            texto_resposta = Label(self.window, text=Hobbies[a])
            texto_resposta.grid(column=0, row=a, padx=10, pady=10)
        button = Button(self.window, text="Voltar", command=self.go_back)
        button.grid(column=0, row=len(Hobbies)+1, pady=10)

    def go_back(self):
        self.window.destroy()
    
window = Tk()
Principal(window)
window.mainloop()