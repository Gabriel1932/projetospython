# Simulador de dado
# Simular o uso de um dado, gerando valor de 1 a 6

import random 
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Você gostaria de gerar um novo valor ao dado ?"
        # layout
        self.layout = [
            [sg.Text("Jogar o dado ?")],
            [sg.Button("sim"), sg.Button("não")]
        ]
        
    def Iniciar(self):
        # Criar uma janela
        self.janela = sg.Window("Simulador de dado", layout=self.layout)
        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # fazer alguma cosia com esse valores
        try: 
            if  self.eventos == "sim" or self.eventos == "s":
                self.GerarValorDado()
            elif self.eventos == "não" or self.eventos == "n":
                        print("obrigado por participar ai")
            else:
                    print("FAvor digitar sim ou não")
        except:
                print("Ocorreu um erro ai viu malandro")
    def GerarValorDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()