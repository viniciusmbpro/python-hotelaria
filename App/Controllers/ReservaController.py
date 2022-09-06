#importando modelos
from tkinter import END
import datetime

from ..Models.Reserva import *
from ..Models.Acomodacao import *

from .HospedeController import *
from .AcomodacaoController import *
from .ServicoController import *
from .ProdutoController import *

class ReservaController():
    @staticmethod
    def cadastrarReserva(App, Init):
        if(len(App.campo_saida_prevista.get())>2):
            reserva = Reserva()
            reserva.qtd_hospedes = App.campo_qtd_hospedes.get()
            reserva.hospedes = ''
            reserva.antecipacao = App.campo_antecipacao.get()
            reserva.entrada_prevista = App.campo_entrada_prevista.get()
            reserva.saida_prevista = App.campo_saida_prevista.get()
            reserva.data_criacao = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            reserva.status = 'Confirmada'
            reserva.valor = AcomodacaoController.getAcomodacaoPorDescricao(App.campo_acomodacao.get())[7]
            reserva.servicos = ''
            reserva.produtos = ''
            try:
                reserva.fk_idhospede = HospedeController.getHospedePorNome(App.campo_hospede.get())[0]
                reserva.fk_idacomodacao = AcomodacaoController.getAcomodacaoPorDescricao(App.campo_acomodacao.get())[0]
            except:
                reserva.fk_idhospede = App.idhospede
                reserva.fk_idacomodacao = App.idacomodacao
            reserva.cadastrar()

            acomodacao = Acomodacao()
            try:
                acomodacao.idacomodacao = AcomodacaoController.getAcomodacaoPorDescricao(App.campo_acomodacao.get())[0]
            except:
                acomodacao.idacomodacao = App.idacomodacao
            acomodacao.ocupar()

            Init.control.renderTela(App.tela_render)

            #acionando label sucesso após a renderização, puxando um novo
            if(App.tela_render!="AppInitAdmin"):
                App.root2.destroy()
                Init.control.tela.abas.select(Init.control.tela.abaMinhasReservas)
            else:
                Init.control.tela.abas.select(Init.control.tela.abaReserva)
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
    def alterarReserva(App, Init):
        if(len(App.campo_saida_prevista.get())>2):
            reserva = Reserva()
            reserva.qtd_hospedes = App.campo_qtd_hospedes.get()
            reserva.hospedes = ''
            reserva.antecipacao = App.campo_antecipacao.get()
            reserva.entrada_prevista = App.campo_entrada_prevista.get()
            reserva.saida_prevista = App.campo_saida_prevista.get()
            reserva.data_criacao = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            reserva.status = 'Confirmada'
            reserva.valor = AcomodacaoController.getAcomodacaoPorDescricao(App.campo_acomodacao.get())[7]
            reserva.servicos = ''
            reserva.produtos = ''
            try:
                reserva.fk_idhospede = HospedeController.getHospedePorNome(App.campo_hospede.get())[0]
                reserva.fk_idacomodacao = AcomodacaoController.getAcomodacaoPorDescricao(App.campo_acomodacao.get())[0]
            except:
                reserva.fk_idhospede = App.idhospede
                reserva.fk_idacomodacao = App.idacomodacao
            reserva.alterar()

            acomodacao = Acomodacao()
            try:
                acomodacao.idacomodacao = AcomodacaoController.getAcomodacaoPorDescricao(App.campo_acomodacao.get())[0]
            except:
                acomodacao.idacomodacao = App.idacomodacao
            reserva.alterar()

            Init.control.renderTela(App.tela_render)

            #acionando label sucesso após a renderização, puxando um novo
            if(App.tela_render!="AppInitAdmin"):
                pass
            else:
                Init.control.tela.abas.select(Init.control.tela.abaReserva)
                App.label_msg.configure(text="alteração realizada com sucesso", bg="green", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.87, relwidth= 0.8, relheight= 0.06)
        else:
            App.label_msg.configure(text="falha, pelo meno 3 caracteres em cada campo", bg="red", fg="white")
            App.label_msg.place(relx= 0.1, rely= 0.87, relwidth= 0.8, relheight= 0.06)

    @staticmethod
    def alterarConsumo(App):
        reserva = Reserva()
        reserva.idreserva = App.idreserva
        dados = reserva.getInfoReserva()
        reserva.servicos = " ".join(App.carrinho_servicos)+" "+dados[8]
        reserva.produtos = " ".join(App.carrinho_produtos)+" "+dados[9]
        reserva.alterarConsumo()

        #alterando estoque dos produtos consumidos
        for dado in App.carrinho_produtos:
            estoque_atual = ProdutoController.getInfoProduto(dado.split(";")[0])[3]
            ProdutoController.alterarEstoque(int(dado.split(";")[0]), estoque_atual-int(dado.split(";")[1]))

        App.root3.destroy()
        App.root2.destroy()
        reserva.fk_idhospede = App.Init.session['idusuario']
        reserva.data_criacao = ''
        App.rReservas = reserva.getAllToHospede()
        App.listarReservas()

    @staticmethod
    def cancelar(idreserva):
        reserva = Reserva()
        reserva.idreserva = idreserva
        reserva.status = 'Cancelada'
        reserva.alterarStatus()

    @staticmethod
    def getInfoReserva(idreserva):
        reserva = Reserva()
        reserva.idreserva = idreserva
        return reserva.getInfoReserva()

    @staticmethod
    def getAllToHospede(fk_idhospede, App):
        reserva = Reserva()
        reserva.fk_idhospede = fk_idhospede
        reserva.data_criacao = App.campo_busca.get()
        App.rReservas = reserva.getAllToHospede()
        App.listarReservas()

    @staticmethod
    def getAllToAcomodacao(fk_idacomodacao):
        reserva = Reserva()
        reserva.fk_idacomodacao = fk_idacomodacao
        return reserva.getAllToAcomodacao()

    @staticmethod
    def getHospedePorDataReserva(data):
        reserva = Reserva()
        reserva.data_criacao = data
        return reserva.getHospedePorDataReserva()

    @staticmethod
    def getReservaPorData_criacao(data):
        reserva = Reserva()
        reserva.data_criacao = data
        return reserva.getReservaPorData_criacao()

    @staticmethod
    def listarAllToHospede(fk_idhospede):
        reserva = Reserva()
        reserva.fk_idhospede = fk_idhospede
        reserva.data_criacao = ""
        return reserva.getAllToHospede()
    
    @staticmethod
    def buscarReservas(App):
        reserva = Reserva()
        reserva.data_criacao = App.campo_busca.get()
        App.rReservas = reserva.buscar()
        App.listarReservas()
    
    @staticmethod
    def listarReservas():
        reserva = Reserva()
        return reserva.listar()

    @staticmethod
    def calcularConsumo(idreserva):
        gastos = []
        reserva = Reserva()
        reserva.idreserva = idreserva
        dados = reserva.getInfoReserva()

        #calcular total serviços
        total_servicos = 0
        for idservico in dados[8].split():
            total_servicos += ServicoController.getInfoServico(idservico)[2]
        gastos.append(total_servicos)

        #calcular total produtos
        total_produtos = 0
        for dadosProd in dados[9].split():
            aux = dadosProd.split(";")
            total_produtos += int(aux[1])*ProdutoController.getInfoProduto(int(aux[0]))[2]
        gastos.append(total_produtos)

        #calcular valor reserva
        gastos.append(dados[7])

        #calcular valor consumo
        gastos.append(total_servicos+total_produtos)

        #calcular valor total
        gastos.append(total_servicos+total_produtos+dados[7])

        return gastos

    @staticmethod
    def deletarReserva(idreserva, Init):
        reserva = Reserva()
        reserva.idreserva = idreserva
        reserva.deletar()
        Init.control.renderTela('AppInitAdmin')
        Init.control.tela.abas.select(Init.control.tela.abaReserva)
