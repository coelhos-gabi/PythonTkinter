from tkinter import *

conversor = Tk()
conversor.title("Fahrenheit to Celsius")


final = StringVar()

def converter():
    temperatura = float(entrada.get())
    celsius = (temperatura - 32) * 5/9
    final.set(str(round(celsius,1)) + " graus Celsius")


temperaturaF = Label(conversor, text="Insira a temperatura em Fahrenheit:")
entrada = Entry(conversor)
botao = Button(conversor, text="Converter", command = converter)
labelResultado = Label(conversor, textvariable = final)


temperaturaF.grid()
entrada.grid()
labelResultado.grid()
botao.grid()

conversor.mainloop()
