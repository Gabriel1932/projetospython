import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            "Com certeza, vc deve fazer isso",
            "Não sei, vc q sabe",
            "Não faz isso não",
            "Acho q ta na hora certa"
        ]

    def Iniciar(self):
        #Layout
        layout = [
            [sg.Text("Faça sua pergunta:")],
            [sg.Input()],
            [sg.Output(size=(20, 10))],
            [sg.Button("Decida por mim")]
        ]
        #criar janela
        self.janela = sg.Window("Decida por mim", layout=layout)  
        #Ler os valores para
        while True:
            self.eventos, self.valores = self.janela.Read()
            #Fazer algo com valores
            if self.eventos == "Decida por mim":
                print(random.choice(self.respostas))
            

decida = DecidaPorMim()
decida.Iniciar()