from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import font as tkFont
import math
import time

#importando Controllers da aplicação
from ...Controllers.HospedeController import *
from ...Controllers.ServicoController import *
from ...Controllers.ProdutoController import *
from ...Controllers.ReservaController import *

class AppLojasAdmin():
    def __init__(self, App):
        self.Init = App.Init
        self.idreserva = App.idreserva

        #abrindo janela
        self.root2 = Toplevel()
        self.root2.title("Loja")
        self.root2.configure(bg="#002e4f")
        self.w_root2 = 1000
        self.root2.geometry(f"{self.w_root2}x600+{int(self.Init.monitor_w/2-self.w_root2/2)}+{100}")
        self.root2.resizable(False, False)
        self.root2.transient(self.Init.root)
        self.root2.focus_force()
        # self.root2.grab_set()
        # self.root2.iconbitmap(self.Init.pasta_app+"/imagens/logo2.ico")

        #definindo título
        self.label_titulo = Label(self.root2, text="Loja de produtos e serviços", font=tkFont.Font(family="Lucida Grande", size=20), bg="#002e4f", fg= "#ffffff")
        self.label_titulo.place(relx= 0, rely= 0, relwidth= 0.4, relheight= 0.1)

        #menu logado
        self.menu_logado = Frame(self.root2, bg="#002e4f")
        self.menu_logado.place(relx= 0.64, rely= 0, relwidth= 0.3, relheight=0.1)

        self.carrinho_produtos = []
        self.carrinho_servicos = []

        self.renderCarrinho()

        #abas para os quartos
        self.abas = ttk.Notebook(self.root2)
        self.abaServico = Frame(self.abas)
        self.abaProduto = Frame(self.abas)

        self.abaServico.configure(bg="#00767d")
        self.abaProduto.configure(bg="#00767d")
        
        self.abas.add(self.abaServico, text="Serviços")
        self.abas.add(self.abaProduto, text="Produtos")

        self.abas.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

        self.lojaProdutos()
        self.lojaServicos()

    def lojaProdutos(self):
        #menu de funções
        self.frame_menu = Frame(self.abaProduto, bg="#00767d")
        self.frame_menu.place(relx= 0.2, rely= 0.02, relwidth= 0.6, relheight= 0.05)

        self.campo_busca_produtos = Entry(self.frame_menu, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_busca_produtos.place(relx= 0.15, rely= 0, relwidth= 0.65, relheight= 1)
        self.btn_busca = Button(self.frame_menu, text="BUSCAR", bg="#ffffff", fg= "#000000", command=lambda:[buscarProdutos()])
        self.btn_busca.place(relx= 0.8, rely= 0, relwidth= 0.2, relheight= 1)
        
        #array para armazenar a quantidade de cada produto
        self.qtd_produto = []
        def buscarProdutos():
            ProdutoController.buscarProdutos(self)
        ProdutoController.buscarProdutos(self)

    def listarProdutos(self):
        #configuração da barra de rolagem
        self.f_base_scroll = Frame(self.abaProduto)
        self.f_base_scroll.place(relx= 0, rely= 0.1, relwidth= 1, relheight= 0.9)
        self.j_produtos = Frame(self.f_base_scroll, bg="#00767d")
        self.canva_rol_p = Canvas(self.j_produtos, bg="#00767d")
        self.canva_rol_p.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        self.yscrollbar = ttk.Scrollbar(self.j_produtos, orient="vertical", command=self.canva_rol_p.yview)
        self.yscrollbar.place(relx= 0.98, rely= 0, relwidth= 0.02, relheight= 1)
        self.canva_rol_p.configure(yscrollcommand=self.yscrollbar.set)
        self.canva_rol_p.bind('<Configure>', lambda e: self.canva_rol_p.configure(scrollregion = self.canva_rol_p.bbox('all')))
        self.frame_rol = Frame(self.canva_rol_p, bg="#00767d")
        self.canva_rol_p.create_window((0,0), window=self.frame_rol, anchor="nw")
        self.j_produtos.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        
        #for para criar frames dos produtos
        indice = 0
        #definindo os quadros da grade
        quadros = 4
        pos_relx = []
        rel_width = 1/quadros-0.02
        for i in range(quadros):
            pos_relx.append((1/quadros)*i)

        def atualizaQtdProduto(event):
            indiceProd = int(event.widget["text"].split()[0])
            acao = event.widget["text"].split()[1]
            if acao=="+" and int(self.qtd_produto[indiceProd].get())<self.rProdutos[indiceProd][3]:
                self.qtd_produto[indiceProd].set(int(self.qtd_produto[indiceProd].get())+1)
            if acao=="-" and int(self.qtd_produto[indiceProd].get())>0:
                self.qtd_produto[indiceProd].set(int(self.qtd_produto[indiceProd].get())-1)

        for row in range(math.ceil(len(self.rProdutos)/quadros)):
            quadros = len(self.rProdutos)%quadros if row==math.ceil(len(self.rProdutos)/quadros)-1 and len(self.rProdutos)%quadros!=0 == 0 else quadros
            self.estrutura = Frame(self.j_produtos, bg="#00767d")
            self.estrutura.pack(in_=self.frame_rol, side=TOP, ipadx=0.47*self.w_root2, ipady=70, padx=10, pady=20)

            for col in range(quadros):
                self.temp_frame = Frame(self.estrutura, bg="#ffffff")
                self.temp_frame.place(relx=pos_relx[col], rely=0, relwidth=rel_width, relheight=1)

                labels = ["Descrição", "Preço", "Estoque"]
                for i in range(len(labels)):
                    Label(self.temp_frame, text=f"{labels[i]}: {str(self.rProdutos[indice][i+1])}", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=11)).place(relx=0.07, y=80/len(labels)*i+10, height=30)
                
                cond = False
                for prod_carrinho in self.carrinho_produtos:
                    if str(self.rProdutos[indice][0])==prod_carrinho.split(";")[0]:
                        cond = True

                if cond:
                    self.nome_item = 'Produto'
                    btn_rem_carrinho = Label(self.temp_frame, text=f"{indice} p {self.rProdutos[indice][0]}  Remover do Carrinho  {self.rProdutos[indice][0]} p {indice}",  bg="red", fg= "#ffffff", font=tkFont.Font(family="Lucida Grande", size=10))
                    btn_rem_carrinho.place(x= 5, rely= 0.7, width= 130, height= 30)
                    btn_rem_carrinho.bind("<Button-1>", self.atualizaCarrinho)
                else:
                    self.nome_item = 'Produto'
                    btn_add_carrinho = Label(self.temp_frame, text=f"{indice} p {self.rProdutos[indice][0]}  Adicionar ao Carrinho  {self.rProdutos[indice][0]} p {indice}",  bg="green", fg= "#ffffff", font=tkFont.Font(family="Lucida Grande", size=10))
                    btn_add_carrinho.place(x= 5, rely= 0.7, width= 130, height= 30)
                    btn_add_carrinho.bind("<Button-1>", self.atualizaCarrinho)
                    
                    self.qtd_produto.append(StringVar())
                    self.qtd_produto[indice].set(1)
                    campo_qtd_produto = Entry(self.temp_frame, textvariable=self.qtd_produto[indice], font=tkFont.Font(family="Lucida Grande", size=10), state="readonly", bd=2)
                    campo_qtd_produto.place(x= 165, rely= 0.7, width= 30, height= 30)

                    btn_add_produto = Button(self.temp_frame, text=f"{indice}  +  {indice}", font=tkFont.Font(family="Lucida Grande", size=14))
                    btn_add_produto.place(x= 145, rely= 0.7, width= 20, height= 30)
                    btn_add_produto.bind("<Button-1>", atualizaQtdProduto)
                    
                    btn_sub_produto = Button(self.temp_frame, text=f"{indice}  -  {indice}", font=tkFont.Font(family="Lucida Grande", size=16))
                    btn_sub_produto.place(x= 195, rely= 0.7, width= 20, height= 30)
                    btn_sub_produto.bind("<Button-1>", atualizaQtdProduto)

                indice+=1

    def lojaServicos(self):
        #menu de funções
        self.frame_menu = Frame(self.abaServico, bg="#00767d")
        self.frame_menu.place(relx= 0.2, rely= 0.02, relwidth= 0.6, relheight= 0.05)

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
        self.f_base_scroll.place(relx= 0, rely= 0.1, relwidth= 1, relheight= 0.9)
        self.j_servicos = Frame(self.f_base_scroll, bg="#00767d")
        self.canva_rol_s = Canvas(self.j_servicos, bg="#00767d")
        self.canva_rol_s.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        self.yscrollbar = ttk.Scrollbar(self.j_servicos, orient="vertical", command=self.canva_rol_s.yview)
        self.yscrollbar.place(relx= 0.98, rely= 0, relwidth= 0.02, relheight= 1)
        self.canva_rol_s.configure(yscrollcommand=self.yscrollbar.set)
        self.canva_rol_s.bind('<Configure>', lambda e: self.canva_rol_s.configure(scrollregion = self.canva_rol_s.bbox('all')))
        self.frame_rol = Frame(self.canva_rol_s, bg="#00767d")
        self.canva_rol_s.create_window((0,0), window=self.frame_rol, anchor="nw")
        self.j_servicos.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)

        #for para criar frames dos serviços
        indice = 0
        #definindo os quadros da grade
        quadros = 4
        pos_relx = []
        rel_width = 1/quadros-0.02
        for i in range(quadros):
            pos_relx.append((1/quadros)*i)

        for row in range(math.ceil(len(self.rServicos)/quadros)):
            quadros = len(self.rServicos)%quadros if row==math.ceil(len(self.rServicos)/quadros)-1 and len(self.rServicos)%quadros!=0 == 0 else quadros
            self.estrutura = Frame(self.j_servicos, bg="#00767d")
            self.estrutura.pack(in_=self.frame_rol, side=TOP, ipadx=0.47*self.w_root2, ipady=70, padx=10, pady=20)

            for col in range(quadros):
                self.temp_frame = Frame(self.estrutura, bg="#ffffff")
                self.temp_frame.place(relx=pos_relx[col], rely=0, relwidth=rel_width, relheight=1)

                labels = ["Descrição", "Preço", "Status"]
                for i in range(len(labels)):
                    Label(self.temp_frame, text=f"{labels[i]}: {str(self.rServicos[indice][i+1])}", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=11)).place(relx=0.07, y=80/len(labels)*i+10, height=30)
                
                if str(self.rServicos[indice][0]) in self.carrinho_servicos:
                    btn_rem_carrinho = Label(self.temp_frame, text=f"s {self.rServicos[indice][0]}  Remover do Carrinho  {self.rServicos[indice][0]} s",  bg="red", fg= "#ffffff", font=tkFont.Font(family="Lucida Grande", size=10))
                    btn_rem_carrinho.place(x= 5, rely= 0.7, width= 130, height= 30)
                    btn_rem_carrinho.bind("<Button-1>", self.atualizaCarrinho)
                else:
                    btn_add_carrinho = Label(self.temp_frame, text=f"s {self.rServicos[indice][0]}  Adicionar ao Carrinho  {self.rServicos[indice][0]} s",  bg="green", fg= "#ffffff", font=tkFont.Font(family="Lucida Grande", size=10))
                    btn_add_carrinho.place(x= 5, rely= 0.7, width= 130, height= 30)
                    btn_add_carrinho.bind("<Button-1>", self.atualizaCarrinho)

                indice+=1

    def atualizaCarrinho(self, event):
        if event.widget["text"].split()[1]=="p":
            indiceProd = int(event.widget["text"].split()[0])
            self.iditem = event.widget["text"].split()[2]
            if event.widget["text"].split()[3]=="Adicionar":
                self.carrinho_produtos.append(f"{self.iditem};{self.qtd_produto[indiceProd].get()}")
            elif event.widget["text"].split()[3]=="Remover":
                self.carrinho_produtos.remove(f"{self.iditem};{self.qtd_produto[indiceProd].get()}")
            self.listarProdutos()
        elif event.widget["text"].split()[0]=="s":
            self.iditem = event.widget["text"].split()[1]
            if event.widget["text"].split()[2]=="Adicionar":
                self.carrinho_servicos.append(self.iditem)
            elif event.widget["text"].split()[2]=="Remover":
                self.carrinho_servicos.remove(self.iditem)
            self.listarServicos()
        self.renderCarrinho()

    def renderCarrinho(self):
        #imagem do carrinho
        self.img_foto_carrinho = PhotoImage(file=f"{self.Init.pasta_app}/imagens/cart.png")
        self.img_foto_carrinho = self.img_foto_carrinho.subsample(2,2)
        self.label_foto_carrinho = Label(self.menu_logado, image=self.img_foto_carrinho, bg="#0e3d54")
        self.label_foto_carrinho.place(relx= 0, rely= 0, relwidth= 0.3, relheight= 1)
        
        #calculando total de itens no carrinho
        qtd_total_carrinho = 0
        for i in self.carrinho_produtos:
            qtd_total_carrinho += int(i.split(";")[1])
        qtd_total_carrinho += len(self.carrinho_servicos)

        self.label_qtd_itens = Label(self.menu_logado, text=f"{qtd_total_carrinho}", bg="red", fg="white", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_qtd_itens.place(relx= 0.2, rely= 0.06, relwidth= 0.07, relheight= 0.25)
        self.label_foto_carrinho.bind("<Button-1>", self.abrirCarrinho)
    
    def abrirCarrinho(self, event):
        #abrindo janela
        self.root3 = Toplevel()
        self.root3.title('Carrinho')
        self.root3.configure(bg="#002e4f")
        self.w_root3 = 400
        self.root3.geometry(f"{self.w_root3}x{400}+{int(self.Init.monitor_w/2-self.w_root3/2)}+{100}")
        self.root3.resizable(False, False)
        self.root3.transient(self.Init.root)
        self.root3.focus_force()
        self.root3.grab_set()
        self.root3.iconbitmap(self.Init.pasta_app+"/imagens/logo2.ico")

        #definindo título
        self.label_titulo = Label(self.root3, text="Carrinho de Compras", font=tkFont.Font(family="Lucida Grande", size=20), bg="#002e4f", fg= "#ffffff")
        self.label_titulo.place(relx= 0, rely= 0, relwidth= 1, relheight= 0.1)

        self.total_carrinho = 0

        self.tree_prod = Frame(self.root3)
        self.tree_prod.place(relx= 0, rely= 0.15, relwidth= 1, relheight=0.4)
        self.label_titulo = Label(self.tree_prod, text="Produtos", font=tkFont.Font(family="Lucida Grande", size=13), bg="#245953", fg= "#ffffff")
        self.label_titulo.place(relx= 0, rely= 0, relwidth= 1, relheight= 0.15)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 13))
        style.configure("Treeview", font=(None, 12))
        tree = ttk.Treeview(self.tree_prod, columns=('Descricao', 'Preço', 'Quantidade', 'SubTotal'), show='headings')
        tree.heading('#1', text='Descricao')
        tree.heading('#2', text='Preço')
        tree.heading('#3', text='Quantidade')
        tree.heading('#4', text='SubTotal')
        for dados in self.carrinho_produtos:
            aux = dados.split(";")
            values = list(ProdutoController.getInfoProduto(int(aux[0])))
            del(values[0])
            del(values[2])
            values.append(int(aux[1]))
            values.append(values[1]*int(aux[1]))
            self.total_carrinho += values[1]*int(aux[1])
            tree.insert('', END, values=values)
        tree.place(relx=0, rely=0.15, width=400, relheight=0.85)
        tree.column("#1", width=100)
        tree.column("#2", width=100)
        tree.column("#3", width=100)
        tree.column("#4", width=100)
        scrollbar = ttk.Scrollbar(self.tree_prod, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.place(relx=0.96, rely=0.15, relwidth=0.04, relheight=0.85)

        self.tree_serv = Frame(self.root3)
        self.tree_serv.place(relx= 0, rely= 0.6, relwidth= 1, relheight=0.3)
        self.label_titulo = Label(self.tree_serv, text="Serviços", font=tkFont.Font(family="Lucida Grande", size=13), bg="#245953", fg= "#ffffff")
        self.label_titulo.place(relx= 0, rely= 0, relwidth= 1, relheight= 0.2)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 13))
        style.configure("Treeview", font=(None, 12))
        tree = ttk.Treeview(self.tree_serv, columns=('Descricao', 'Preço', 'Quantidade', 'SubTotal'), show='headings')
        tree.heading('#1', text='Descricao')
        tree.heading('#2', text='Preço')
        tree.heading('#3', text='Quantidade')
        tree.heading('#4', text='SubTotal')
        for idserv in self.carrinho_servicos:
            values = list(ServicoController.getInfoServico(idserv))
            del(values[0])
            del(values[2])
            values.append(1)
            values.append(values[1])
            self.total_carrinho += values[1]
            tree.insert('', END, values=values)
        tree.place(relx=0, rely=0.2, width=400, relheight=0.8)
        tree.column("#1", width=100)
        tree.column("#2", width=100)
        tree.column("#3", width=100)
        tree.column("#4", width=100)
        scrollbar = ttk.Scrollbar(self.tree_serv, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.place(relx=0.96, rely=0.2, relwidth=0.04, relheight=0.8)

        self.label_total_carrinho = Label(self.root3, text=f"Valor Total: {self.total_carrinho}", bg="#1b5218", fg= "#ffffff", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_total_carrinho.place(relx=0, rely=0.92, relwidth=0.5, height=30)

        self.btn_confirmar_compra = Button(self.root3, text="Confirmar Comprar", command=lambda:[ReservaController.alterarConsumo(self)], font=tkFont.Font(family="Lucida Grande", size=13))
        self.btn_confirmar_compra.place(relx=0.5, rely=0.92, relwidth=0.5, height=30)
