#importando modelos
from ..Models.Acomodacao import *
from tkinter import END

class AcomodacaoController():
    @staticmethod
    def cadastrarAcomodacao(App, Init):
        if(len(App.campo_descricao.get())>2):
            acomodacao = Acomodacao()
            acomodacao.descricao = App.campo_descricao.get()
            acomodacao.andar = App.campo_andar.get()
            acomodacao.capacidade = App.campo_capacidade.get()
            acomodacao.observacoes = App.campo_observacoes.get()
            acomodacao.status = App.campo_status.get()
            acomodacao.fk_idcategoria = App.campo_categoria.current()+1
            acomodacao.cadastrar()

            Init.control.renderTela(App.tela_render)

            #acionando label sucesso após a renderização, puxando um novo
            if(App.tela_render!="AppInitAdmin"):
                Init.control.tela.label_msg.configure(text="cadastro realizado com sucesso", bg="green", fg="white")
                Init.control.tela.label_msg.place(relx= 0.1, rely= 0.87, relwidth= 0.8, relheight= 0.06)
            else:
                Init.control.tela.abas.select(Init.control.tela.abaAcomodacao)
                App.label_msg.configure(text="cadastro realizado com sucesso", bg="green", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.87, relwidth= 0.8, relheight= 0.06)
        else:
            if(App.tela_render!="AppInitAdmin"):
                App.label_msg.configure(text="falha no cadastro, reveja suas informações", bg="red", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.87, relwidth= 0.8, relheight= 0.06)
            else:
                App.label_msg.configure(text="falha no cadastro, reveja suas informações", bg="red", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.87, relwidth= 0.8, relheight= 0.06)

    @staticmethod
    def alterarAcomodacao(App, Init):
        if(len(App.campo_descricao.get())>2):
            acomodacao = Acomodacao()
            acomodacao.descricao = App.campo_descricao.get()
            acomodacao.andar = App.campo_andar.get()
            acomodacao.capacidade = App.campo_capacidade.get()
            acomodacao.observacoes = App.campo_observacoes.get()
            acomodacao.status = App.campo_status.get()
            acomodacao.fk_idcategoria = App.campo_categoria.current()+1
            acomodacao.idacomodacao = App.idacomodacao
            acomodacao.alterar()

            Init.control.renderTela(App.tela_render)

            #acionando label sucesso após a renderização, puxando um novo
            if(App.tela_render!="AppInitAdmin"):
                Init.control.tela.label_msg.configure(text="alteração realizada com sucesso", bg="green", fg="white")
                Init.control.tela.label_msg.place(relx= 0.1, rely= 0.87, relwidth= 0.8, relheight= 0.06)
            else:
                Init.control.tela.abas.select(Init.control.tela.abaAcomodacao)
                App.label_msg.configure(text="alteração realizada com sucesso", bg="green", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.87, relwidth= 0.8, relheight= 0.06)
        else:
            App.label_msg.configure(text="falha, pelo meno 3 caracteres em cada campo", bg="red", fg="white")
            App.label_msg.place(relx= 0.1, rely= 0.87, relwidth= 0.8, relheight= 0.06)

    @staticmethod
    def getInfoAcomodacao(idacomodacao):
        acomodacao = Acomodacao()
        acomodacao.idacomodacao = idacomodacao
        return acomodacao.getInfoAcomodacao()
    
    @staticmethod
    def buscarAcomodacoes(App):
        acomodacao = Acomodacao()
        acomodacao.descricao = App.campo_busca.get()
        App.rAcomodacoes = acomodacao.buscar()
        App.listarAcomodacoes()

    @staticmethod
    def getAcomodacaoPorDescricao(descricao):
        acomodacao = Acomodacao()
        acomodacao.descricao = descricao
        return acomodacao.getAcomodacaoPorDescricao()
        
    @staticmethod
    def listarAcomodacoes():
        acomodacao = Acomodacao()
        return acomodacao.listar()

    @staticmethod
    def deletarAcomodacao(idacomodacao, Init):
        acomodacao = Acomodacao()
        acomodacao.idacomodacao = idacomodacao
        acomodacao.deletar()
        Init.control.renderTela('AppInitAdmin')
        Init.control.tela.abas.select(Init.control.tela.abaAcomodacao)
