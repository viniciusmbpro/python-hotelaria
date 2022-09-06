#importando modelos
from ..Models.Produto import *
from tkinter import END

class ProdutoController():
    @staticmethod
    def cadastrarProduto(App, Init):
        if(len(App.campo_descricao.get())>2):
            produto = Produto()
            produto.descricao = App.campo_descricao.get()
            produto.preco = App.campo_preco.get()
            produto.estoque = App.campo_estoque.get()
            produto.cadastrar()

            Init.control.renderTela(App.tela_render)

            #acionando label sucesso após a renderização, puxando um novo
            if(App.tela_render!="AppInitAdmin"):
                Init.control.tela.label_msg.configure(text="cadastro realizado com sucesso", bg="green", fg="white")
                Init.control.tela.label_msg.place(relx= 0.1, rely= 0.75, relwidth= 0.8, relheight= 0.06)
            else:
                Init.control.tela.abas.select(Init.control.tela.abaProduto)
                App.label_msg.configure(text="cadastro realizado com sucesso", bg="green", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.75, relwidth= 0.8, relheight= 0.06)
        else:
            if(App.tela_render!="AppInitAdmin"):
                App.label_msg.configure(text="falha no cadastro, reveja suas informações", bg="red", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.75, relwidth= 0.8, relheight= 0.06)
            else:
                App.label_msg.configure(text="falha no cadastro, reveja suas informações", bg="red", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.75, relwidth= 0.8, relheight= 0.06)

    @staticmethod
    def alterarProduto(App, Init):
        if(len(App.campo_descricao.get())>2):
            produto = Produto()
            produto.descricao = App.campo_descricao.get()
            produto.preco = App.campo_preco.get()
            produto.estoque = App.campo_estoque.get()
            produto.idproduto = App.idproduto
            produto.alterar()

            Init.control.renderTela(App.tela_render)

            #acionando label sucesso após a renderização, puxando um novo
            if(App.tela_render!="AppInitAdmin"):
                Init.control.tela.label_msg.configure(text="alteração realizada com sucesso", bg="green", fg="white")
                Init.control.tela.label_msg.place(relx= 0.1, rely= 0.75, relwidth= 0.8, relheight= 0.06)
            else:
                Init.control.tela.abas.select(Init.control.tela.abaProduto)
                App.label_msg.configure(text="alteração realizada com sucesso", bg="green", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.75, relwidth= 0.8, relheight= 0.06)
        else:
            App.label_msg.configure(text="falha, pelo meno 3 caracteres em cada campo", bg="red", fg="white")
            App.label_msg.place(relx= 0.1, rely= 0.75, relwidth= 0.8, relheight= 0.06)

    @staticmethod
    def getInfoProduto(idproduto):
        produto = Produto()
        produto.idproduto = idproduto
        return produto.getInfoProduto()
    
    @staticmethod
    def buscarProdutos(App):
        produto = Produto()
        produto.descricao = App.campo_busca_produtos.get()
        App.rProdutos = produto.buscar()
        App.listarProdutos()
    
    @staticmethod
    def alterarEstoque(idproduto, estoque):
        produto = Produto()
        produto.estoque = estoque
        produto.idproduto = idproduto
        produto.alterarEstoque()

    @staticmethod
    def listarProdutos():
        produto = Produto()
        return produto.listar()
 
    @staticmethod
    def deletarProduto(idproduto, Init):
        produto = Produto()
        produto.idproduto = idproduto
        produto.deletar()
        Init.control.renderTela('AppInitAdmin')
        Init.control.tela.abas.select(Init.control.tela.abaProduto)
