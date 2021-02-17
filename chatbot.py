# -*- coding: utf-8 -*- 
from tkinter import *

root = Tk()

def send():
    send ="Você: " + e.get()
    txt.insert(END, "\n"+send)
    if(e.get() == "opa"):
        txt.insert(END, "\n" + "Bot: opa fi")
    if(e.get() == "tudo ok ?"):
        txt.insert(END, "\n" + "Bot: tudo sim e vc ? ")
    if(e.get() == "to bem"):
        txt.insert(END, "\n" + "Bot: massa geral")
    if(e.get() == "ta fazendo o q de bom ?"):
        txt.insert(END, "\n" + "Bot: 010101")
    if(e.get() == "hehe"):
        txt.insert(END, "\n" + "Bot: poisé 01")
    else:
        txt.insert(END, "\n" + "Bot: escreve humano, não entendi nada ")
    e.delete(0, END)
    

txt=Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
send = Button(root, text="Send", command=send).grid(row=1, column=1)
e.grid(row=1, column=0)
root.title("ChatBOT")
root.mainloop()
