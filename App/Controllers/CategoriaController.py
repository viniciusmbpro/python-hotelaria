#importando modelos
from ..Models.Categoria import *
from tkinter import END

class CategoriaController():
    @staticmethod
    def cadastrarCategoria(App, Init):
        if(len(App.campo_descricao.get())>2):
            categoria = Categoria()
            categoria.descricao = App.campo_descricao.get()
            categoria.valor = App.campo_valor.get()
            categoria.produtos = " ".join(App.cprodutos)
            categoria.cadastrar()

            Init.control.renderTela(App.tela_render)

            #acionando label sucesso após a renderização, puxando um novo
            if(App.tela_render!="AppInitAdmin"):
                Init.control.tela.label_msg.configure(text="cadastro realizado com sucesso", bg="green", fg="white")
                Init.control.tela.label_msg.place(relx= 0.1, rely= 0.7, relwidth= 0.8, relheight= 0.06)
            else:
                Init.control.tela.abas.select(Init.control.tela.abaCategoria)
                App.label_msg.configure(text="cadastro realizado com sucesso", bg="green", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.7, relwidth= 0.8, relheight= 0.06)
        else:
            if(App.tela_render!="AppInitAdmin"):
                App.label_msg.configure(text="falha no cadastro, reveja suas informações", bg="red", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.7, relwidth= 0.8, relheight= 0.06)
            else:
                App.label_msg.configure(text="falha no cadastro, reveja suas informações", bg="red", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.7, relwidth= 0.8, relheight= 0.06)

    @staticmethod
    def alterarCategoria(App, Init):
        if(len(App.campo_descricao.get())>2):
            categoria = Categoria()
            categoria.descricao = App.campo_descricao.get()
            categoria.valor = App.campo_valor.get()
            categoria.produtos = " ".join(App.cprodutos)
            categoria.idcategoria = App.idcategoria
            categoria.alterar()

            Init.control.renderTela(App.tela_render)

            #acionando label sucesso após a renderização, puxando um novo
            if(App.tela_render!="AppInitAdmin"):
                Init.control.tela.label_msg.configure(text="alteração realizada com sucesso", bg="green", fg="white")
                Init.control.tela.label_msg.place(relx= 0.1, rely= 0.7, relwidth= 0.8, relheight= 0.06)
            else:
                Init.control.tela.abas.select(Init.control.tela.abaCategoria)
                App.label_msg.configure(text="alteração realizada com sucesso", bg="green", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.7, relwidth= 0.8, relheight= 0.06)
        else:
            App.label_msg.configure(text="falha, pelo meno 3 caracteres em cada campo", bg="red", fg="white")
            App.label_msg.place(relx= 0.1, rely= 0.7, relwidth= 0.8, relheight= 0.06)

    @staticmethod
    def getInfoCategoria(idcategoria):
        categoria = Categoria()
        categoria.idcategoria = idcategoria
        return categoria.getInfoCategoria()

    @staticmethod
    def getCategoriaPorDescricao(descricao):
        categoria = Categoria()
        categoria.descricao = descricao
        return categoria.getCategoriaPorDescricao()
    
    @staticmethod
    def buscarCategorias(App):
        categoria = Categoria()
        categoria.descricao = App.campo_busca.get()
        App.rCategorias = categoria.buscar()
        App.listarCategorias()
    
    @staticmethod
    def listarCategorias():
        categoria = Categoria()
        return categoria.listar()

    @staticmethod
    def deletarCategoria(idcategoria, Init):
        categoria = Categoria()
        categoria.idcategoria = idcategoria
        categoria.deletar()
        Init.control.renderTela('AppInitAdmin')
        Init.control.tela.abas.select(Init.control.tela.abaCategoria)