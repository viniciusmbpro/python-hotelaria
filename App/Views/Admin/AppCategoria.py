from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font as tkFont
from tkcalendar import Calendar
import datetime
import math

#importando Controllers da aplicação
from ...Controllers.CategoriaController import *
from ...Controllers.ProdutoController import *
from .AppInitAdmin import *

class AppCategoria:
    def __init__(self, abaCategoria, Init):
        #definindo a tela de renderização
        self.tela_render = "AppInitAdmin"

        #recebendo o init dentro da classe para passar para a qualquer função
        self.Init = Init
        self.abaCategoria = abaCategoria

        #menu de funções
        self.frame_menu = Frame(self.abaCategoria, bg="#00767d")
        self.frame_menu.place(relx= 0.2, rely= 0.02, relwidth= 0.6, relheight= 0.05)

        self.btn_adicionar = Label(self.frame_menu, text="0       Adicionar       0",  bg="#0e6900", fg="#ffffff", font=tkFont.Font(family="Lucida Grande", size=13), border=2)
        self.btn_adicionar.place(relx= 0, rely= 0, relwidth= 0.15, relheight= 1)
        self.btn_adicionar.bind("<Button-1>", self.formularioCategoria)

        self.campo_busca = Entry(self.frame_menu, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_busca.place(relx= 0.15, rely= 0, relwidth= 0.65, relheight= 1)
        self.btn_busca = Button(self.frame_menu, text="BUSCAR", bg="#ffffff", fg= "#000000", command=lambda:[buscarCategorias()])
        self.btn_busca.place(relx= 0.8, rely= 0, relwidth= 0.2, relheight= 1)
        def buscarCategorias():
            CategoriaController.buscarCategorias(self)
        CategoriaController.buscarCategorias(self)
        

    def listarCategorias(self):
        #configuração da barra de rolagem
        self.f_base_scroll = Frame(self.abaCategoria)
        self.f_base_scroll.place(relx= 0, rely= 0.09, relwidth= 1, relheight= 0.95)
        self.j_categorias = Frame(self.f_base_scroll, bg="#00767d")
        self.canva_rol = Canvas(self.j_categorias, bg="#00767d")
        self.canva_rol.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        self.yscrollbar = ttk.Scrollbar(self.j_categorias, orient="vertical", command=self.canva_rol.yview)
        self.yscrollbar.place(relx= 0.98, rely= 0, relwidth= 0.02, relheight= 1)
        self.canva_rol.configure(yscrollcommand=self.yscrollbar.set)
        self.canva_rol.bind('<Configure>', lambda e: self.canva_rol.configure(scrollregion = self.canva_rol.bbox('all')))
        self.frame_rol = Frame(self.canva_rol, bg="#00767d")
        self.canva_rol.create_window((0,0), window=self.frame_rol, anchor="nw")
        self.j_categorias.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        
        #for para criar frames dos categorias
        indice = 0
        #definindo os quadros da grade
        quadros = 3
        pos_relx = []
        rel_width = 1/quadros-0.02
        for i in range(quadros):
            pos_relx.append((1/quadros)*i)

        #chamando editar hóspede
        def callDeletarCategoria(event):
            if(messagebox.askquestion("Confirmar","Você tem certeza que quer deletar esta categoria?")=="yes"):
                CategoriaController.deletarCategoria(event.widget["text"].split()[0],self.Init)
        #definindo treeview de produtos

        for row in range(math.ceil(len(self.rCategorias)/quadros)):
            quadros = len(self.rCategorias)%quadros if row==math.ceil(len(self.rCategorias)/quadros)-1 and len(self.rCategorias)%quadros!=0 == 0 else quadros
            self.estrutura = Frame(self.j_categorias, bg="#00767d")
            self.estrutura.pack(in_=self.frame_rol, side=TOP, ipadx=0.47*self.Init.monitor_w, ipady=120, padx=10, pady=20)

            for col in range(quadros):
                self.temp_frame = Frame(self.estrutura, bg="#ffffff")
                self.temp_frame.place(relx=pos_relx[col], rely=0, relwidth=rel_width, relheight=1)

                labels = ["Descrição", "Valor", "Produtos"]
                for i in range(len(labels)):
                    if i !=2:
                        Label(self.temp_frame, text=f"{labels[i]}: {str(self.rCategorias[indice][i+1])}", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=11)).place(relx=0.07, y=70/len(labels)*i+10, height=30)
                    if i == 2:
                        Label(self.temp_frame, text=f"{labels[i]}:", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=11)).place(relx=0.07, y=70/len(labels)*i+10, height=30)
                        
                        style = ttk.Style()
                        style.configure("Treeview.Heading", font=(None, 13))
                        style.configure("Treeview", font=(None, 12))
                        tree = ttk.Treeview(self.temp_frame, columns=('descricao', 'preco', 'estoque'), show='headings')
                        tree.heading('#1', text='Descrição')
                        tree.heading('#2', text='Preço')
                        tree.heading('#3', text='Estoque')
                        array = self.rCategorias[indice][3].split()
                        for idproduto in array:
                            values = list(ProdutoController.getInfoProduto(idproduto))
                            del(values[0])
                            tree.insert('', END, values=values)
                        tree.place(relx=0.07, y=80, width=300, height=130)
                        tree.column("#1", width=100)
                        tree.column("#2", width=100)
                        tree.column("#3", width=100)
                        scrollbar = ttk.Scrollbar(self.temp_frame, orient=VERTICAL, command=tree.yview)
                        tree.configure(yscroll=scrollbar.set)
                        scrollbar.place(relx=0.8, y=80, width=15, height=130)
    
                btn_editar = Label(self.temp_frame, text=f"{self.rCategorias[indice][0]}  Editar  {self.rCategorias[indice][0]}",  bg="blue", fg= "#ffffff", font=tkFont.Font(family="Lucida Grande", size=13))
                btn_editar.place(x= 5, rely= 0.86, width= 60, height= 30)
                btn_editar.bind("<Button-1>", self.formularioCategoria)

                btn_deletar = Label(self.temp_frame, text=f"{self.rCategorias[indice][0]}  Deletar  {self.rCategorias[indice][0]}",  bg="red", fg= "#ffffff", font=tkFont.Font(family="Lucida Grande", size=13))
                btn_deletar.place(x=70, rely= 0.86, width= 60, height= 30)
                btn_deletar.bind("<Button-1>", callDeletarCategoria)

                indice+=1

    def formularioCategoria(self, event):
        #puxando dados
        acao = event.widget["text"].split()[1]
        if acao=="Editar":
            self.idcategoria = event.widget["text"].split()[0]
            self.dados_categoria = CategoriaController.getInfoCategoria(self.idcategoria)
            descricao = self.dados_categoria[1]
            valor = self.dados_categoria[2]
            self.cprodutos = self.dados_categoria[3].split()
        else:
            descricao = ''
            valor = ''
            self.cprodutos = []

        #abrindo janela
        self.root2 = Toplevel()
        self.root2.title(acao)
        self.root2.configure(bg="#283d8f", highlightbackground="#283d8f", highlightthickness= 1, highlightcolor="#ffffff")
        self.w_root2 = 700
        self.root2.geometry(f"{self.w_root2}x{600}+{int(self.Init.monitor_w/2-self.w_root2/2)}+{100}")
        self.root2.resizable(False, False)
        self.root2.transient(self.Init.root)
        self.root2.focus_force()
        self.root2.grab_set()
        self.root2.iconbitmap(self.Init.pasta_app+"\\imagens\\logo2.ico")

        #definindo título
        self.label_titulo = Label(self.root2, text=f"{acao} Categoria", font=tkFont.Font(family="Lucida Grande", size=15), bg="#283d8f", fg= "#ffffff")
        self.label_titulo.place(relx= 0, rely= 0, relwidth= 1, relheight= 0.1)

        #abrindo frame para os widgets
        self.f_widgets = Frame(self.root2, bd= 4, bg="#283d8f",  highlightbackground="#283d8f", highlightthickness= 1, highlightcolor="#ffffff")
        self.f_widgets.place(relx= 0, rely= 0.1, relwidth= 1, relheight= 0.8)

        #carregando widgets
        self.widgetsForm()
        self.widgetsProdutos()

        #inserindo dados atuais no formulário de edição
        self.campo_descricao.insert(0, descricao)
        self.campo_valor.insert(0, valor)

        def callCategoriaController():
            self.preencherArrayProdutos()
            if acao=="Editar":
                CategoriaController.alterarCategoria(self, self.Init)
            else:
                CategoriaController.cadastrarCategoria(self, self.Init)

        self.btn_salvar = Button(self.root2, text="SALVAR", bg="#ffffff", fg= "#000000", command=lambda:[callCategoriaController()])
        self.btn_salvar.place(relx= 0.1, rely= 0.93, relwidth= 0.8, relheight= 0.05)

    def widgetsForm(self):

        self.label_descricao = Label(self.f_widgets, text="Descricao", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_descricao.place(relx= 0.1, rely= 0.02, relwidth= 0.25, relheight= 0.08)
        self.campo_descricao = Entry(self.f_widgets, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_descricao.place(relx= 0.35, rely= 0.02, relwidth= 0.55, relheight= 0.08)

        self.label_valor = Label(self.f_widgets, text="Valor", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_valor.place(relx= 0.1, rely= 0.12, relwidth= 0.25, relheight= 0.08)
        self.campo_valor = Entry(self.f_widgets, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_valor.place(relx= 0.35, rely= 0.12, relwidth= 0.55, relheight= 0.08)

        #definindo label de mensagem
        self.label_msg = Label(self.root2)

    def widgetsProdutos(self):
        self.label_titulo = Label(self.f_widgets, text="Produtos Relacionados", font=tkFont.Font(family="Lucida Grande", size=15), bg="#283d8f", fg= "#ffffff")
        self.label_titulo.place(relx= 0, rely= 0.22, relwidth= 1, relheight= 0.08)

        self.frame_menu = Frame(self.f_widgets, bg="#00767d")
        self.frame_menu.place(relx= 0.05, rely= 0.3, relwidth= 0.9, relheight= 0.08)

        self.campo_busca_produtos = Entry(self.frame_menu, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_busca_produtos.place(relx= 0, rely= 0, relwidth= 0.7, relheight= 1)
        self.btn_busca = Button(self.frame_menu, text="BUSCAR", bg="#ffffff", fg= "#000000", command=lambda:[self.preencherArrayProdutos(),buscarProdutos()])
        self.btn_busca.place(relx= 0.7, rely= 0, relwidth= 0.3, relheight= 1)
        #definindo array que vai armazenar os ckeckbox
        self.checks = []
        self.btn_checks = []
        def buscarProdutos():
            ProdutoController.buscarProdutos(self)
        ProdutoController.buscarProdutos(self)

    def listarProdutos(self):
        #configuração da barra de rolagem
        self.f_base_scroll = Frame(self.f_widgets)
        self.f_base_scroll.place(relx= 0, rely= 0.4, relwidth= 1, relheight= 0.6)
        self.j_produtos = Frame(self.f_base_scroll, bg="#00767d")
        self.canva_rol_produtos = Canvas(self.j_produtos, bg="#00767d")
        self.canva_rol_produtos.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        self.yscrollbar = ttk.Scrollbar(self.j_produtos, orient="vertical", command=self.canva_rol_produtos.yview)
        self.yscrollbar.place(relx= 0.95, rely= 0, relwidth= 0.08, relheight= 1)
        self.canva_rol_produtos.configure(yscrollcommand=self.yscrollbar.set)
        self.canva_rol_produtos.bind('<Configure>', lambda e: self.canva_rol_produtos.configure(scrollregion = self.canva_rol_produtos.bbox('all')))
        self.frame_rol_produtos = Frame(self.canva_rol_produtos, bg="#00767d")
        self.canva_rol_produtos.create_window((0,0), window=self.frame_rol_produtos, anchor="nw")
        self.j_produtos.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)

        #for para criar frames dos produtos
        indice = 0
        #definindo os quadros da grade
        quadros = 3
        pos_relx = []
        rel_width = 1/quadros-0.02
        for i in range(quadros):
            pos_relx.append((1/quadros)*i)

        for row in range(math.ceil(len(self.rProdutos)/quadros)):
            quadros = len(self.rProdutos)%quadros if row==math.ceil(len(self.rProdutos)/quadros)-1 and len(self.rProdutos)%quadros!=0 == 0 else quadros
            self.estrutura = Frame(self.j_produtos, bg="#00767d")
            self.estrutura.pack(in_=self.frame_rol_produtos, side=TOP, ipadx=0.46*self.w_root2, ipady=40, padx=10, pady=20)

            for col in range(quadros):
                self.temp_frame = Frame(self.estrutura, bg="#ffffff")
                self.temp_frame.place(relx=pos_relx[col], rely=0, relwidth=rel_width, relheight=1)

                labels = ["Descrição", "Preço", "Estoque"]
                for i in range(len(labels)):
                    Label(self.temp_frame, text=f"{labels[i]}: {str(self.rProdutos[indice][i+1])}", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=11)).place(relx=0.07, y=80/len(labels)*i, height=30)
                self.checks.append(IntVar())
                self.btn_checks.append(ttk.Checkbutton(self.temp_frame, variable=self.checks[indice], onvalue=self.rProdutos[indice][0], offvalue=0))
                self.btn_checks[indice].place(relx=0.8, y=20)
                if str(self.rProdutos[indice][0]) in self.cprodutos:
                    self.checks[indice].set(self.rProdutos[indice][0])

                indice+=1

    def preencherArrayProdutos(self):
        for i in range(len(self.checks)):
            if(self.checks[i].get()!=0 and str(self.checks[i].get()) not in self.cprodutos):
                self.cprodutos.append(str(self.checks[i].get()))
            if(self.checks[i].get()==0 and str(self.btn_checks[i]['onvalue']) in self.cprodutos):
                self.cprodutos.remove(str(self.btn_checks[i]['onvalue']))
