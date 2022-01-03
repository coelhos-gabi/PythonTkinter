from tkinter import *

login = Tk()
login.title("Login")

Label(login, text="Usuário:").grid(row=0, sticky=W)
Label(login, text="Senha:").grid(row=1, sticky=W)

boxUsuario = Entry(login).grid(row=0, column=1)
boxSenha = Entry(login).grid(row=1, column=1)
entrar = Button(login, text="Entrar").grid(row=2, column=1, sticky=E)

login.mainloop()