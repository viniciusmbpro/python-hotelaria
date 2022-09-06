from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font as tkFont
from tkcalendar import Calendar
import datetime
import math

#importando Controllers da aplicação
from ...Controllers.ProdutoController import *
from .AppInitAdmin import *

class AppProduto:
    def __init__(self, abaProduto, Init):
        #definindo a tela de renderização
        self.tela_render = "AppInitAdmin"

        #recebendo o init dentro da classe para passar para a qualquer função
        self.Init = Init
        self.abaProduto = abaProduto

        #menu de funções
        self.frame_menu = Frame(self.abaProduto, bg="#00767d")
        self.frame_menu.place(relx= 0.2, rely= 0.02, relwidth= 0.6, relheight= 0.05)

        self.btn_adicionar = Label(self.frame_menu, text="0       Adicionar       0",  bg="#0e6900", fg="#ffffff", font=tkFont.Font(family="Lucida Grande", size=13), border=2)
        self.btn_adicionar.place(relx= 0, rely= 0, relwidth= 0.15, relheight= 1)
        self.btn_adicionar.bind("<Button-1>", self.formularioProduto)

        self.campo_busca_produtos = Entry(self.frame_menu, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_busca_produtos.place(relx= 0.15, rely= 0, relwidth= 0.65, relheight= 1)
        self.btn_busca = Button(self.frame_menu, text="BUSCAR", bg="#ffffff", fg= "#000000", command=lambda:[buscarProdutos()])
        self.btn_busca.place(relx= 0.8, rely= 0, relwidth= 0.2, relheight= 1)
        def buscarProdutos():
            ProdutoController.buscarProdutos(self)
        ProdutoController.buscarProdutos(self)

    def listarProdutos(self):
        #configuração da barra de rolagem
        self.f_base_scroll = Frame(self.abaProduto)
        self.f_base_scroll.place(relx= 0, rely= 0.09, relwidth= 1, relheight= 0.95)
        self.j_produtos = Frame(self.f_base_scroll, bg="#00767d")
        self.canva_rol = Canvas(self.j_produtos, bg="#00767d")
        self.canva_rol.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        self.yscrollbar = ttk.Scrollbar(self.j_produtos, orient="vertical", command=self.canva_rol.yview)
        self.yscrollbar.place(relx= 0.98, rely= 0, relwidth= 0.02, relheight= 1)
        self.canva_rol.configure(yscrollcommand=self.yscrollbar.set)
        self.canva_rol.bind('<Configure>', lambda e: self.canva_rol.configure(scrollregion = self.canva_rol.bbox('all')))
        self.frame_rol = Frame(self.canva_rol, bg="#00767d")
        self.canva_rol.create_window((0,0), window=self.frame_rol, anchor="nw")
        self.j_produtos.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        
        #for para criar frames dos produtos
        indice = 0
        #definindo os quadros da grade
        quadros = 4
        pos_relx = []
        rel_width = 1/quadros-0.02
        for i in range(quadros):
            pos_relx.append((1/quadros)*i)

        #chamando editar hóspede
        def callDeletarProduto(event):
            if(messagebox.askquestion("Confirmar","Você tem certeza que quer deletar este produto?")=="yes"):
                ProdutoController.deletarProduto(event.widget["text"].split()[0],self.Init)

        for row in range(math.ceil(len(self.rProdutos)/quadros)):
            quadros = len(self.rProdutos)%quadros if row==math.ceil(len(self.rProdutos)/quadros)-1 and len(self.rProdutos)%quadros!=0 == 0 else quadros
            self.estrutura = Frame(self.j_produtos, bg="#00767d")
            self.estrutura.pack(in_=self.frame_rol, side=TOP, ipadx=0.47*self.Init.monitor_w, ipady=70, padx=10, pady=20)

            for col in range(quadros):
                self.temp_frame = Frame(self.estrutura, bg="#ffffff")
                self.temp_frame.place(relx=pos_relx[col], rely=0, relwidth=rel_width, relheight=1)

                labels = ["Descrição", "Preço", "Estoque"]
                for i in range(len(labels)):
                    Label(self.temp_frame, text=f"{labels[i]}: {str(self.rProdutos[indice][i+1])}", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=11)).place(relx=0.07, y=80/len(labels)*i+10, height=30)
                
                btn_editar = Label(self.temp_frame, text=f"{self.rProdutos[indice][0]}  Editar  {self.rProdutos[indice][0]}",  bg="blue", fg= "#ffffff", font=tkFont.Font(family="Lucida Grande", size=13))
                btn_editar.place(x= 5, rely= 0.7, width= 60, height= 30)
                btn_editar.bind("<Button-1>", self.formularioProduto)

                btn_deletar = Label(self.temp_frame, text=f"{self.rProdutos[indice][0]}  Deletar  {self.rProdutos[indice][0]}",  bg="red", fg= "#ffffff", font=tkFont.Font(family="Lucida Grande", size=13))
                btn_deletar.place(x=70, rely= 0.7, width= 60, height= 30)
                btn_deletar.bind("<Button-1>", callDeletarProduto)

                indice+=1

    def formularioProduto(self, event):
        #puxando dados
        acao = event.widget["text"].split()[1]
        if acao=="Editar":
            self.idproduto = event.widget["text"].split()[0]
            self.dados_produto = ProdutoController.getInfoProduto(self.idproduto)
            descricao = self.dados_produto[1]
            preco = self.dados_produto[2]
            estoque = self.dados_produto[3]
        else:
            descricao = ''
            preco = ''
            estoque = ''

        #abrindo janela
        self.root2 = Toplevel()
        self.root2.title(acao)
        self.root2.configure(bg="#283d8f", highlightbackground="#283d8f", highlightthickness= 1, highlightcolor="#ffffff")
        w_root2 = 500
        self.root2.geometry(f"{w_root2}x{200}+{int(self.Init.monitor_w/2-w_root2/2)}+{100}")
        self.root2.resizable(False, False)
        self.root2.transient(self.Init.root)
        self.root2.focus_force()
        self.root2.grab_set()
        self.root2.iconbitmap(self.Init.pasta_app+"\\imagens\\logo2.ico")

        #definindo título
        self.label_titulo = Label(self.root2, text=f"{acao} Produto", font=tkFont.Font(family="Lucida Grande", size=15), bg="#283d8f", fg= "#ffffff")
        self.label_titulo.place(relx= 0, rely= 0, relwidth= 1, relheight= 0.13)

        #abrindo frame para os widgets
        self.f_widgets = Frame(self.root2, bd= 4, bg="#283d8f",  highlightbackground="#283d8f", highlightthickness= 1, highlightcolor="#ffffff")
        self.f_widgets.place(relx= 0, rely= 0.13, relwidth= 1, relheight= 0.7)

        #carregando widgets
        self.widgetsForm()

        #inserindo dados atuais no formulário de edição
        self.campo_descricao.insert(0, descricao)
        self.campo_preco.insert(0, preco)
        self.campo_estoque.insert(0, estoque)
        
        def callProdutoController():
            if acao=="Editar":
                ProdutoController.alterarProduto(self, self.Init)
            else:
                ProdutoController.cadastrarProduto(self, self.Init)
        self.btn_salvar = Button(self.root2, text="SALVAR", bg="#ffffff", fg= "#000000", command=lambda:[callProdutoController()])
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

        self.label_estoque = Label(self.f_widgets, text="Estoque", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_estoque.place(relx= 0.1, rely= 0.66, relwidth= 0.25, relheight= 0.3)
        self.campo_estoque = Entry(self.f_widgets, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_estoque.place(relx= 0.35, rely= 0.66, relwidth= 0.55, relheight= 0.3)

        #definindo label de mensagem
        self.label_msg = Label(self.root2)
