from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import font as tkFont
from tkinter.colorchooser import askcolor
from tkinter import filedialog as fd
from tkinter.messagebox import *
from PIL import Image, ImageTk
from tkcalendar import Calendar
import datetime
import os

#importando Controllers da aplicação
from ...Controllers.HospedeController import *

class AppConfig():      
    def __init__(self, Init):
        self.tela_render = "AppConfig"
        self.Init = Init

        #criando o frame
        self.framePrincipal = Frame(self.Init.root, bd= 4, bg="#002e4f",highlightbackground="#ffffff", highlightthickness= 1)
        self.framePrincipal.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        
        #menu logado
        self.menu_logado = Frame(self.framePrincipal, bd= 4, bg="#004170")
        self.menu_logado.place(relx= 0.64, rely= 0.025, relwidth= 0.3, relheight= 0.05)
        self.label_nome_logado = Label(self.menu_logado, text=(Init.session['nome'][0]), font=tkFont.Font(family="Lucida Grande", size=14), bg="#004170", fg= "white")
        self.label_nome_logado.place(relx= 0, rely= 0, relwidth= 0.4, relheight= 1)
        self.btn_sair = Button(self.menu_logado, text="SAIR", 
                                font= tkFont.Font(size=10), bg="red", 
                                fg= "#ffffff", command=lambda:[Init.control.sair()])
        self.btn_sair.place(relx= 0.8, rely= 0, relwidth= 0.2, relheight= 1)
        self.btn_home = Button(self.menu_logado, text="HOME", 
                                font= tkFont.Font(size=10), bg="#00767d", 
                                fg= "#ffffff", command=lambda:[Init.control.renderTela('AppInitHospede')])
        self.btn_home.place(relx= 0.4, rely= 0, relwidth= 0.4, relheight= 1)

        #imagem do perfil
        self.img_foto_perfil = PhotoImage(file=f"{self.Init.pasta_app}\\imagens\\{Init.session['foto_perfil']}")
        self.img_foto_perfil = self.img_foto_perfil.subsample(6,6)
        self.label_foto_perfil = Label(self.framePrincipal, image=self.img_foto_perfil, bd=2, bg="#002e4f", highlightbackground="#004170", highlightthickness= 5)
        self.label_foto_perfil.place(relx= 0.6, rely= 0.005, relwidth= 0.06, relheight= 0.09)
        #definindo título
        self.label_titulo = Label(self.framePrincipal, text="Configure e personalise a sua conta", font=tkFont.Font(family="Lucida Grande", size=20), bg="#002e4f", fg= "#ffffff")
        self.label_titulo.place(relx= 0, rely= 0, relwidth= 0.4, relheight= 0.1)

        #abas para os configurações
        self.abas = ttk.Notebook(self.framePrincipal)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)

        self.aba1.configure(background="#00767d")
        self.aba2.configure(background="#00767d")

        self.abas.add(self.aba1, text="Alterar dados da conta")
        self.abas.add(self.aba2, text="Alterar tema do sistema")

        self.abas.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

        #chamando formulario
        self.formularioHospede()

        #color picker
        self.btn_color_picker = Button(self.aba2, text="color picker", 
                        font= tkFont.Font(size=30), bg="#00767d", 
                        fg= "#ffffff", command=lambda:[askcolor()])
        self.btn_color_picker.place(relx= 0.3, rely= 0.3, relwidth= 0.4, relheight= 0.4)

    def formularioHospede(self):
        self.frame_formulario = Frame(self.aba1, bd= 4, bg="#002e4f",highlightbackground="#ffffff", highlightthickness= 1)
        self.frame_formulario.place(relx= 0.1, rely= 0.1, relwidth= 0.8, relheight= 0.8)
        #puxando dados
        self.idhospede = self.Init.session['idusuario']
        self.dados_hospede = HospedeController.getInfoHospede(self.idhospede)
        nome = self.dados_hospede[0]
        rg = self.dados_hospede[1]
        cpf = self.dados_hospede[2]
        email = self.dados_hospede[3]
        senha = self.dados_hospede[4]
        telefone = self.dados_hospede[5]
        data_nascimento = self.dados_hospede[6]
        sexo = self.dados_hospede[7]
        foto_perfil = self.dados_hospede[8]
        endereco = self.dados_hospede[9]
        dados_bancarios = self.dados_hospede[10]
        data_criacao = self.dados_hospede[11]

        #definindo título
        self.label_titulo = Label(self.frame_formulario, text="Editar Conta", font=tkFont.Font(family="Lucida Grande", size=15), bg="#002e4f", fg= "#ffffff")
        self.label_titulo.place(relx= 0, rely= 0, relwidth= 1, relheight= 0.1)

        #lados do form
        self.f_esquerda = Frame(self.frame_formulario, bd= 4, bg="#002e4f",  highlightbackground="#002e4f", highlightthickness= 1, highlightcolor="#ffffff")
        self.f_esquerda.place(relx= 0, rely= 0.1, relwidth= 0.5, relheight= 0.8)
        self.f_direita = Frame(self.frame_formulario, bd= 4, bg="#002e4f",  highlightbackground="#002e4f", highlightthickness= 1, highlightcolor="#ffffff")
        self.f_direita.place(relx= 0.5, rely= 0.1, relwidth= 0.5, relheight= 0.8)
        
        #carregando widgets
        self.widgetsForm()

        #inserindo dados atuais no formulário de edição
        self.campo_nome.insert(0, nome)
        self.campo_rg.insert(0, rg)
        self.campo_cpf.insert(0, cpf)
        self.campo_email.insert(0, email)
        self.campo_senha.insert(0, senha)
        self.campo_telefone.insert(0, telefone)
        self.campo_data_nascimento.insert(0, data_nascimento)
        c=0
        if sexo == "Feminino": c=1
        elif sexo == "Não declarar": c=2
        self.campo_sexo.current(c)
        self.campo_endereco.insert(0, endereco)
        self.campo_dados_bancarios.insert(0, dados_bancarios)

        self.btn_salvar = Button(self.frame_formulario, text="SALVAR", bg="#ffffff", fg= "#000000", command=lambda:[HospedeController.alterarHospede(self, self.Init)])
        self.btn_salvar.place(relx= 0.1, rely= 0.93, relwidth= 0.8, relheight= 0.07)
    
    def widgetsForm(self):

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
        loadPreView(f"{self.Init.pasta_app}\\imagens\\{self.Init.session['foto_perfil']}")

        self.label_endereco = Label(self.f_direita, text="Endereço", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_endereco.place(relx= 0.1, rely= 0.74, relwidth= 0.2, relheight= 0.1)
        self.campo_endereco = Entry(self.f_direita, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_endereco.place(relx= 0.3, rely= 0.74, relwidth= 0.6, relheight= 0.1)

        self.label_dados_bancarios = Label(self.f_direita, text="Dados Bancários", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_dados_bancarios.place(relx= 0.1, rely= 0.86, relwidth= 0.4, relheight= 0.1)
        self.campo_dados_bancarios = Entry(self.f_direita, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_dados_bancarios.place(relx= 0.5, rely= 0.86, relwidth= 0.4, relheight= 0.1)

        #definindo label de mensagem
        self.label_msg = Label(self.frame_formulario)
