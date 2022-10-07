from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font as tkFont
from tkcalendar import Calendar
import datetime
import math

#importando Controllers da aplicação
from ...Controllers.ServicoController import *
from .AppInitAdmin import *

class AppServico:
    def __init__(self, abaServico, Init):
        #definindo a tela de renderização
        self.tela_render = "AppInitAdmin"

        #recebendo o init dentro da classe para passar para a qualquer função
        self.Init = Init
        self.abaServico = abaServico

        #menu de funções
        self.frame_menu = Frame(self.abaServico, bg="#00767d")
        self.frame_menu.place(relx= 0.2, rely= 0.02, relwidth= 0.6, relheight= 0.05)

        self.btn_adicionar = Label(self.frame_menu, text="0       Adicionar       0",  bg="#0e6900", fg="#ffffff", font=tkFont.Font(family="Lucida Grande", size=13), border=2)
        self.btn_adicionar.place(relx= 0, rely= 0, relwidth= 0.15, relheight= 1)
        self.btn_adicionar.bind("<Button-1>", self.formularioServico)

        self.campo_busca = Entry(self.frame_menu, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_busca.place(relx= 0.15, rely= 0, relwidth= 0.65, relheight= 1)
        self.btn_busca = Button(self.frame_menu, text="BUSCAR", bg="#ffffff", fg= "#000000", command=lambda:[buscarServicos()])
        self.btn_busca.place(relx= 0.8, rely= 0, relwidth= 0.2, relheight= 1)
        def buscarServicos():
            ServicoController.buscarServicos(self)
        ServicoController.buscarServicos(self)

    def listarServicos(self):
        #configuração da barra de rolagem
        self.f_base_scroll = Frame(self.abaServico)
        self.f_base_scroll.place(relx= 0, rely= 0.09, relwidth= 1, relheight= 0.95)
        self.j_servicos = Frame(self.f_base_scroll, bg="#00767d")
        self.canva_rol = Canvas(self.j_servicos, bg="#00767d")
        self.canva_rol.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        self.yscrollbar = ttk.Scrollbar(self.j_servicos, orient="vertical", command=self.canva_rol.yview)
        self.yscrollbar.place(relx= 0.98, rely= 0, relwidth= 0.02, relheight= 1)
        self.canva_rol.configure(yscrollcommand=self.yscrollbar.set)
        self.canva_rol.bind('<Configure>', lambda e: self.canva_rol.configure(scrollregion = self.canva_rol.bbox('all')))
        self.frame_rol = Frame(self.canva_rol, bg="#00767d")
        self.canva_rol.create_window((0,0), window=self.frame_rol, anchor="nw")
        self.j_servicos.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)

        #for para criar frames dos serviços
        indice = 0
        #definindo os quadros da grade
        quadros = 4
        pos_relx = []
        rel_width = 1/quadros-0.02
        for i in range(quadros):
            pos_relx.append((1/quadros)*i)

        #chamando editar hóspede
        def callDeletarServico(event):
            if(messagebox.askquestion("Confirmar","Você tem certeza que quer deletar este serviço?")=="yes"):
                ServicoController.deletarServico(event.widget["text"].split()[0],self.Init)

        for row in range(math.ceil(len(self.rServicos)/quadros)):
            quadros = len(self.rServicos)%quadros if row==math.ceil(len(self.rServicos)/quadros)-1 and len(self.rServicos)%quadros!=0 == 0 else quadros
            self.estrutura = Frame(self.j_servicos, bg="#00767d")
            self.estrutura.pack(in_=self.frame_rol, side=TOP, ipadx=0.47*self.Init.monitor_w, ipady=70, padx=10, pady=20)

            for col in range(quadros):
                self.temp_frame = Frame(self.estrutura, bg="#ffffff")
                self.temp_frame.place(relx=pos_relx[col], rely=0, relwidth=rel_width, relheight=1)

                labels = ["Descrição", "Preço", "Status"]
                for i in range(len(labels)):
                    Label(self.temp_frame, text=f"{labels[i]}: {str(self.rServicos[indice][i+1])}", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=11)).place(relx=0.07, y=80/len(labels)*i+10, height=30)
                
                btn_editar = Label(self.temp_frame, text=f"{self.rServicos[indice][0]}  Editar  {self.rServicos[indice][0]}",  bg="blue", fg= "#ffffff", font=tkFont.Font(family="Lucida Grande", size=13))
                btn_editar.place(x= 5, rely= 0.7, width= 60, height= 30)
                btn_editar.bind("<Button-1>", self.formularioServico)

                btn_deletar = Label(self.temp_frame, text=f"{self.rServicos[indice][0]}  Deletar  {self.rServicos[indice][0]}",  bg="red", fg= "#ffffff", font=tkFont.Font(family="Lucida Grande", size=13))
                btn_deletar.place(x=70, rely= 0.7, width= 60, height= 30)
                btn_deletar.bind("<Button-1>", callDeletarServico)

                indice+=1

    def formularioServico(self, event):
        #puxando dados
        acao = event.widget["text"].split()[1]
        if acao=="Editar":
            self.idservico = event.widget["text"].split()[0]
            self.dados_servico = ServicoController.getInfoServico(self.idservico)
            descricao = self.dados_servico[1]
            preco = self.dados_servico[2]
            status = self.dados_servico[3]
        else:
            descricao = ''
            preco = ''
            status = ''

        #abrindo janela
        self.root2 = Toplevel()
        self.root2.title(acao)
        self.root2.configure(bg="#283d8f", highlightbackground="#283d8f", highlightthickness= 1, highlightcolor="#ffffff")
        w_root2 = 500
        self.root2.geometry(f"{w_root2}x{200}+{int(self.Init.monitor_w/2-w_root2/2)}+{100}")
        self.root2.resizable(False, False)
        self.root2.transient(self.Init.root)
        self.root2.focus_force()
        # self.root2.grab_set()
        # self.root2.iconbitmap(self.Init.pasta_app+"/imagens/logo2.ico")

        #definindo título
        self.label_titulo = Label(self.root2, text=f"{acao} Serviço", font=tkFont.Font(family="Lucida Grande", size=15), bg="#283d8f", fg= "#ffffff")
        self.label_titulo.place(relx= 0, rely= 0, relwidth= 1, relheight= 0.13)

        #abrindo frame para os widgets
        self.f_widgets = Frame(self.root2, bd= 4, bg="#283d8f",  highlightbackground="#283d8f", highlightthickness= 1, highlightcolor="#ffffff")
        self.f_widgets.place(relx= 0, rely= 0.13, relwidth= 1, relheight= 0.7)

        #carregando widgets
        self.widgetsForm()

        #inserindo dados atuais no formulário de edição
        self.campo_descricao.insert(0, descricao)
        self.campo_preco.insert(0, preco)
        self.campo_status.set(status)

        def callServicoController():
            if acao=="Editar":
                ServicoController.alterarServico(self, self.Init)
            else:
                ServicoController.cadastrarServico(self, self.Init)
        self.btn_salvar = Button(self.root2, text="SALVAR", bg="#ffffff", fg= "#000000", command=lambda:[callServicoController()])
        self.btn_salvar.place(relx= 0.1, rely= 0.82, relwidth= 0.8, relheight= 0.16)
    
    def widgetsForm(self):

        self.label_descricao = Label(self.f_widgets, text="Descrição", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_descricao.place(relx= 0.1, rely= 0.02, relwidth= 0.25, relheight= 0.3)
        self.campo_descricao = Entry(self.f_widgets, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_descricao.place(relx= 0.35, rely= 0.02, relwidth= 0.55, relheight= 0.3)

        self.label_preco = Label(self.f_widgets, text="Preço", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_preco.place(relx= 0.1, rely= 0.34, relwidth= 0.25, relheight= 0.3)
        self.campo_preco = Entry(self.f_widgets, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_preco.place(relx= 0.35, rely= 0.34, relwidth= 0.55, relheight= 0.3)

        self.label_status = Label(self.f_widgets, text="status", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_status.place(relx= 0.1, rely= 0.66, relwidth= 0.25, relheight= 0.3)
        self.campo_status = ttk.Combobox(self.f_widgets, values=["Disponível", "Indiponível"], state="readonly", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_status.place(relx= 0.35, rely= 0.66, relwidth= 0.55, relheight= 0.3)

        #definindo label de mensagem
        self.label_msg = Label(self.root2)
