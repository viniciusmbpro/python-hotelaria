from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import font as tkFont

#importando Controllers da aplicação
from ..Controllers import *

class AppLogin():
    def __init__(self, Init):
        #criando o frame
        self.framePrincipal = Frame(Init.root, bd= 4, bg="#1f3f52",
                            highlightbackground="#ffffff", highlightthickness= 1)
        self.framePrincipal.place(relx= 0.25, rely= 0.25, relwidth= 0.5, relheight= 0.5)

        #definindo título
        self.label_titulo = Label(self.framePrincipal, text="Login", font=tkFont.Font(family="Lucida Grande", size=30), bg="#1f3f52", fg= "#ffffff")
        self.label_titulo.place(relx= 0.25, rely= 0, relwidth= 0.5, relheight= 0.2)

        #definindo formulário
        fontLogin=tkFont.Font(family="Lucida Grande", size=12)

        self.label_email = Label(self.framePrincipal, text="Email", bg="#ffffff", fg= "#000000", font= fontLogin)
        self.label_email.place(relx= 0.1, rely= 0.3, relwidth= 0.2, relheight= 0.12)
        self.campo_email = Entry(self.framePrincipal, width = 50, bg="#ffffff", fg= "#000000", font= fontLogin)
        self.campo_email.place(relx= 0.3, rely= 0.3, relwidth= 0.6, relheight= 0.12)
        Init.root.focus_force()

        self.label_senha = Label(self.framePrincipal, text="Senha", bg="#ffffff", fg= "#000000", font= fontLogin)
        self.label_senha.place(relx= 0.1, rely= 0.45, relwidth= 0.2, relheight= 0.12)
        self.campo_senha = Entry(self.framePrincipal, width = 50, bg="#ffffff", fg= "#000000", font= fontLogin)
        self.campo_senha.place(relx= 0.3, rely= 0.45, relwidth= 0.6, relheight= 0.12)

        self.label_erro = Label(self.framePrincipal, text="falha no login, preecha os campos corretamente", bg="#a81d1d", fg= "white", font= fontLogin)

        self.btn_entrar = Button(self.framePrincipal, text="ENTRAR", font= tkFont.Font(size=10),
                            bg="#ffffff", fg= "#000000", command=lambda:[Init.control.autenticar(self, Init)])
        self.btn_entrar.place(relx= 0.1, rely= 0.7, relwidth= 0.8, relheight= 0.12)

        self.btn_criar_conta = Button(self.framePrincipal, text="CRIAR CONTA", 
                                font= tkFont.Font(size=8), bg="#1f6a06", 
                                fg= "#ffffff", command=lambda:[Init.control.renderTela('AppCadastro')])
        self.btn_criar_conta.place(relx= 0.1, rely= 0.85, relwidth= 0.8, relheight= 0.07)
