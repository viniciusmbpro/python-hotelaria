from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import font as tkFont
from tkcalendar import Calendar
from tkinter import filedialog as fd
from tkinter.messagebox import *
from PIL import Image, ImageTk
import os

#importando Controllers da aplicação
from ...Controllers.HospedeController import *

class AppCadastro():
    def __init__(self, Init):
        #definindo a tela de renderização
        self.tela_render = "AppCadastro"
        self.Init = Init

        #criando o frame principal
        self.framePrincipal = Frame(Init.root, bd= 4, bg="#003360", highlightbackground="#003360", highlightthickness= 1, highlightcolor="#ffffff")
        self.framePrincipal.place(relx= 0.15, rely= 0.15, relwidth= 0.7, relheight= 0.7)

        #definindo título
        self.label_titulo = Label(self.framePrincipal, text="Criar conta", font=tkFont.Font(family="Lucida Grande", size=15), bg="#003360", fg= "#ffffff")
        self.label_titulo.place(relx= 0, rely= 0, relwidth= 1, relheight= 0.1)

        #lados do form
        self.f_esquerda = Frame(self.framePrincipal, bd= 4, bg="#003360", highlightbackground="#003360", highlightthickness= 1, highlightcolor="#ffffff")
        self.f_esquerda.place(relx= 0, rely= 0.1, relwidth= 0.5, relheight= 0.7)
        self.f_direita = Frame(self.framePrincipal, bd= 4, bg="#003360", highlightbackground="#003360", highlightthickness= 1, highlightcolor="#ffffff")
        self.f_direita.place(relx= 0.5, rely= 0.1, relwidth= 0.5, relheight= 0.7)

        self.label_nome = Label(self.f_esquerda, text="Nome", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_nome.place(relx= 0.1, rely= 0.02, relwidth= 0.2, relheight= 0.1)
        self.campo_nome = Entry(self.f_esquerda, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_nome.place(relx= 0.3, rely= 0.02, relwidth= 0.6, relheight= 0.1)

        self.label_rg = Label(self.f_esquerda, text="RG", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_rg.place(relx= 0.1, rely= 0.14, relwidth= 0.2, relheight= 0.1)
        self.campo_rg = Entry(self.f_esquerda, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_rg.place(relx= 0.3, rely= 0.14, relwidth= 0.6, relheight= 0.1)

        self.label_cpf = Label(self.f_esquerda, text="CPF", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_cpf.place(relx= 0.1, rely= 0.26, relwidth= 0.2, relheight= 0.1)
        self.campo_cpf = Entry(self.f_esquerda, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_cpf.place(relx= 0.3, rely= 0.26, relwidth= 0.6, relheight= 0.1)

        self.label_email = Label(self.f_esquerda, text="Email", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_email.place(relx= 0.1, rely= 0.38, relwidth= 0.2, relheight= 0.1)
        self.campo_email = Entry(self.f_esquerda, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_email.place(relx= 0.3, rely= 0.38, relwidth= 0.6, relheight= 0.1)

        self.label_telefone = Label(self.f_esquerda, text="telefone", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_telefone.place(relx= 0.1, rely= 0.5, relwidth= 0.2, relheight= 0.1)
        self.campo_telefone = Entry(self.f_esquerda, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_telefone.place(relx= 0.3, rely= 0.5, relwidth= 0.6, relheight= 0.1)

        def inserir_data():
            data = self.calendario.get_date()
            self.calendario.destroy()
            self.campo_data_nascimento.delete(0, END)
            self.campo_data_nascimento.insert(0, data)
        def calendario():
            self.calendario = Calendar(self.f_esquerda, bg="white", fg="black", locale="pt_br")
            self.calendario.place(relx=0.3, rely=0.2)
            self.btn_inserir_data = Button(self.calendario, text="inserir", bg="#ffffff", fg= "black", command=lambda:[inserir_data()])
            self.btn_inserir_data.place(relx= 0.5, rely= 0)
        self.label_data_nascimento = Label(self.f_esquerda, text="data_nascimento", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_data_nascimento.place(relx= 0.1, rely= 0.62, relwidth= 0.4, relheight= 0.1)
        self.campo_data_nascimento = Entry(self.f_esquerda, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_data_nascimento.place(relx= 0.5, rely= 0.62, relwidth= 0.3, relheight= 0.1)
        self.btn_calendario = Button(self.f_esquerda, text="+", bg="#ffffff", fg= "#000000", command=lambda:[calendario()], font=("Arial", 25))
        self.btn_calendario.place(relx= 0.8, rely= 0.62, relwidth= 0.1, relheight= 0.1)

        self.label_senha = Label(self.f_esquerda, text="Senha", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_senha.place(relx= 0.1, rely= 0.74, relwidth= 0.2, relheight= 0.1)
        self.campo_senha = Entry(self.f_esquerda, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_senha.place(relx= 0.3, rely= 0.74, relwidth= 0.6, relheight= 0.1)

        self.label_sexo = Label(self.f_esquerda, text="sexo", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_sexo.place(relx= 0.1, rely= 0.86, relwidth= 0.2, relheight= 0.1)
        self.campo_sexo = ttk.Combobox(self.f_esquerda, values=["Masculino", "Feminino", "Não declarar"], state="readonly", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_sexo.place(relx= 0.3, rely= 0.86, relwidth= 0.6, relheight= 0.1)

        def select_file(event):
            filetypes = ( ('image files', '*.jpg, .png .gif'), ('All files', '*.*') )
            filename = fd.askopenfilename( title='Open a file', initialdir='/', filetypes=filetypes )
            loadPreView(filename)
        def loadPreView(imgPath):
            self.imgPathFotoPerfil = imgPath
            img = Image.open(imgPath)
            img = img.resize((round(400), round((img.size[1]/img.size[0])*400)), Image.ANTIALIAS)
            os.remove(self.Init.pasta_app+"\\imagens\\img_temp.png") 
            img.save(self.Init.pasta_app+"\\imagens\\img_temp.png", format('png'))
            _image = PhotoImage(file=self.Init.pasta_app+"\\imagens\\img_temp.png")
            _image = _image.subsample(2,2)
            self.campo_preView.configure(image=_image)
        self.label_foto_perfil = Label(self.f_direita, text="Foto Perfil", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_foto_perfil.place(relx= 0.1, rely= 0.02, relwidth= 0.8, relheight= 0.1)
        self.campo_preView = Label(self.f_direita, bg="white")
        self.campo_preView.place(relx= 0.1, rely= 0.12, relwidth= 0.8, relheight= 0.6)
        self.campo_preView.bind("<Button-1>", select_file)
        loadPreView(self.Init.pasta_app+"\\imagens\\clique_aqui.png")

        self.label_endereco = Label(self.f_direita, text="Endereço", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_endereco.place(relx= 0.1, rely= 0.74, relwidth= 0.2, relheight= 0.1)
        self.campo_endereco = Entry(self.f_direita, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_endereco.place(relx= 0.3, rely= 0.74, relwidth= 0.6, relheight= 0.1)

        self.label_dados_bancarios = Label(self.f_direita, text="Dados Bancários", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_dados_bancarios.place(relx= 0.1, rely= 0.86, relwidth= 0.4, relheight= 0.1)
        self.campo_dados_bancarios = Entry(self.f_direita, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_dados_bancarios.place(relx= 0.5, rely= 0.86, relwidth= 0.4, relheight= 0.1)

        #definindo label de mensagem
        self.label_msg = Label(self.framePrincipal)

        self.btn_salvar = Button(self.framePrincipal, text="Cadastrar", bg="#ffffff", fg= "#000000", command=lambda:[HospedeController.cadastrarHospede(self, Init)])
        self.btn_salvar.place(relx= 0.15, rely= 0.86, relwidth= 0.7, relheight= 0.07)
        self.btn_salvar = Button(self.framePrincipal, text="Voltar", bg="#1f6a06", fg= "#ffffff", command=lambda:[Init.control.renderTela('AppLogin')])
        self.btn_salvar.place(relx= 0.25, rely= 0.94, relwidth= 0.5, relheight= 0.05)