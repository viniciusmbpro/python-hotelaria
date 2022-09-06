#importando modelos
from ..Models.Checkout import *
from ..Models.Acomodacao import *
from tkinter import END
import datetime

from .ReservaController import *
from .FuncionarioController import *
from .ServicoController import *
from .ProdutoController import *

class CheckoutController():
    @staticmethod
    def cadastrarCheckout(App, Init):
        if(1):
            checkout = Checkout()
            checkout.valor_pago = App.campo_valor_pago.get()
            checkout.nota_fiscal = App.campo_nota_fiscal.get()
            checkout.data_criacao = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            checkout.fk_idfuncionario = FuncionarioController.getFuncionarioPorNome(App.campo_funcionario.get())[0]
            checkout.fk_idreserva = ReservaController.getReservaPorData_criacao(App.campo_reserva.get())[0]
            checkout.valor_consumo = ReservaController.calcularConsumo(checkout.fk_idreserva)[3]
            checkout.cadastrar()

            reserva = Reserva()
            reserva.idreserva = checkout.fk_idreserva
            reserva.status = 'Checked-out'
            reserva.alterarStatus()

            acomodacao = Acomodacao()
            acomodacao.idacomodacao = reserva.getInfoReserva()[10]
            acomodacao.desocupar()

            Init.control.renderTela(App.tela_render)

            #acionando label sucesso após a renderização, puxando um novo
            if(App.tela_render!="AppInitAdmin"):
                App.root2.destroy()
            else:
                App.root2.destroy()
                Init.control.tela.abas.select(Init.control.tela.abaCheckout)
        else:
            if(App.tela_render!="AppInitAdmin"):
                App.label_msg.configure(text="falha no cadastro, reveja suas informações", bg="red", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.72, relwidth= 0.8, relheight= 0.06)
            else:
                App.label_msg.configure(text="falha no cadastro, reveja suas informações", bg="red", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.72, relwidth= 0.8, relheight= 0.06)

    @staticmethod
    def alterarCheckout(App, Init):
        try:
            if(1):
                checkout = Checkout()
                checkout.valor_pago = App.campo_valor_pago.get()
                checkout.nota_fiscal = App.campo_nota_fiscal.get()
                checkout.fk_idfuncionario = FuncionarioController.getFuncionarioPorNome(App.campo_funcionario.get())[0]
                checkout.fk_idreserva = ReservaController.getReservaPorData_criacao(App.campo_reserva.get())[0]
                checkout.valor_consumo = ReservaController.calcularConsumo(checkout.fk_idreserva)[3]
                checkout.idcheckout = App.idcheckout
                checkout.alterar()

                Init.control.renderTela(App.tela_render)

                #acionando label sucesso após a renderização, puxando um novo
                if(App.tela_render!="AppInitAdmin"):
                    pass
                else:
                    Init.control.tela.abas.select(Init.control.tela.abaCheckout)
                    App.label_msg.configure(text="alteração realizada com sucesso", bg="green", fg="white")
                    App.label_msg.place(relx= 0.1, rely= 0.72, relwidth= 0.8, relheight= 0.06)
        except:
            App.label_msg.configure(text="falha, reveja as informações", bg="red", fg="white")
            App.label_msg.place(relx= 0.1, rely= 0.72, relwidth= 0.8, relheight= 0.06)

    @staticmethod
    def getInfoCheckout(idcheckout):
        checkout = Checkout()
        checkout.idcheckout = idcheckout
        return checkout.getInfoCheckout()

    @staticmethod
    def getAllToHospede(fk_idreserva, App):
        checkout = Checkout()
        checkout.fk_idreserva = fk_idreserva
        checkout.data_criacao = App.campo_busca.get()
        App.rCheckouts = checkout.getAllToHospede()
        App.listarCheckouts()
    
    @staticmethod
    def buscarCheckouts(App):
        checkout = Checkout()
        checkout.data_criacao = App.campo_busca.get()
        App.rCheckouts = checkout.buscar()
        App.listarCheckouts()

    @staticmethod
    def deletarCheckout(idcheckout, Init):
        checkout = Checkout()
        checkout.idcheckout = idcheckout
        checkout.deletar()
        Init.control.renderTela('AppInitAdmin')
        Init.control.tela.abas.select(Init.control.tela.abaCheckout)
