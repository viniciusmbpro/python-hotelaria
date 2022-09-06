#importando modelos
from ..Models.Servico import *
from tkinter import END

class ServicoController():
    @staticmethod
    def cadastrarServico(App, Init):
        if(len(App.campo_descricao.get())>2):
            servico = Servico()
            servico.descricao = App.campo_descricao.get()
            servico.preco = App.campo_preco.get()
            servico.status = App.campo_status.get()
            servico.cadastrar()

            Init.control.renderTela(App.tela_render)

            #acionando label sucesso após a renderização, puxando um novo
            if(App.tela_render!="AppInitAdmin"):
                Init.control.tela.label_msg.configure(text="cadastro realizado com sucesso", bg="green", fg="white")
                Init.control.tela.label_msg.place(relx= 0.1, rely= 0.75, relwidth= 0.8, relheight= 0.06)
            else:
                Init.control.tela.abas.select(Init.control.tela.abaServico)
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
    def alterarServico(App, Init):
        if(len(App.campo_descricao.get())>2):
            servico = Servico()
            servico.descricao = App.campo_descricao.get()
            servico.preco = App.campo_preco.get()
            servico.status = App.campo_status.get()
            servico.idservico = App.idservico
            servico.alterar()

            Init.control.renderTela(App.tela_render)

            #acionando label sucesso após a renderização, puxando um novo
            if(App.tela_render!="AppInitAdmin"):
                Init.control.tela.label_msg.configure(text="alteração realizada com sucesso", bg="green", fg="white")
                Init.control.tela.label_msg.place(relx= 0.1, rely= 0.75, relwidth= 0.8, relheight= 0.06)
            else:
                Init.control.tela.abas.select(Init.control.tela.abaServico)
                App.label_msg.configure(text="alteração realizada com sucesso", bg="green", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.75, relwidth= 0.8, relheight= 0.06)
        else:
            App.label_msg.configure(text="falha, pelo meno 3 caracteres em cada campo", bg="red", fg="white")
            App.label_msg.place(relx= 0.1, rely= 0.75, relwidth= 0.8, relheight= 0.06)

    @staticmethod
    def getInfoServico(idservico):
        servico = Servico()
        servico.idservico = idservico
        return servico.getInfoServico()
    
    @staticmethod
    def buscarServicos(App):
        servico = Servico()
        servico.descricao = App.campo_busca.get()
        App.rServicos = servico.buscar()
        App.listarServicos()
    
    @staticmethod
    def listarServicos():
        servico = Servico()
        return servico.listar()

    @staticmethod
    def deletarServico(idservico, Init):
        servico = Servico()
        servico.idservico = idservico
        servico.deletar()
        Init.control.renderTela('AppInitAdmin')
        Init.control.tela.abas.select(Init.control.tela.abaServico)
