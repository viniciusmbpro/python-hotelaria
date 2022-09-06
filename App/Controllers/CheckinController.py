#importando modelos
from ..Models.Checkin import *
from ..Models.Acomodacao import *
from tkinter import END
import datetime

from .ReservaController import *
from .FuncionarioController import *

class CheckinController():
    @staticmethod
    def cadastrarCheckin(App, Init):
        try:
            if(1):
                checkin = Checkin()
                checkin.data_criacao = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                checkin.fk_idfuncionario = FuncionarioController.getFuncionarioPorNome(App.campo_funcionario.get())[0]
                checkin.fk_idreserva = ReservaController.getReservaPorData_criacao(App.campo_reserva.get())[0]
                checkin.cadastrar()

                reserva = Reserva()
                reserva.idreserva = checkin.fk_idreserva
                reserva.status = 'Checked-in'
                reserva.alterarStatus()

                Init.control.renderTela(App.tela_render)

                #acionando label sucesso após a renderização, puxando um novo
                if(App.tela_render!="AppInitAdmin"):
                    App.root2.destroy()
                else:
                    App.root2.destroy()
                    Init.control.tela.abas.select(Init.control.tela.abaCheckin)
                    App.label_msg.configure(text="cadastro realizado com sucesso", bg="green", fg="white")
                    App.label_msg.place(relx= 0.1, rely= 0.72, relwidth= 0.8, relheight= 0.06)
        except:
            if(App.tela_render!="AppInitAdmin"):
                App.label_msg.configure(text="falha no cadastro, reveja suas informações", bg="red", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.72, relwidth= 0.8, relheight= 0.06)
            else:
                App.label_msg.configure(text="falha no cadastro, reveja suas informações", bg="red", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.72, relwidth= 0.8, relheight= 0.06)

    @staticmethod
    def alterarCheckin(App, Init):
        try:
            if(1):
                checkin = Checkin()
                checkin.fk_idfuncionario = FuncionarioController.getFuncionarioPorNome(App.campo_funcionario.get())[0]
                checkin.fk_idreserva = ReservaController.getReservaPorData_criacao(App.campo_reserva.get())[0]
                checkin.idcheckin = App.idcheckin
                checkin.alterar()

                Init.control.renderTela(App.tela_render)

                #acionando label sucesso após a renderização, puxando um novo
                if(App.tela_render!="AppInitAdmin"):
                    pass
                else:
                    App.root2.destroy()
                    Init.control.tela.abas.select(Init.control.tela.abaCheckin)
                    App.label_msg.configure(text="alteração realizada com sucesso", bg="green", fg="white")
                    App.label_msg.place(relx= 0.1, rely= 0.72, relwidth= 0.8, relheight= 0.06)
        except:
            App.label_msg.configure(text="falha, reveja as informações", bg="red", fg="white")
            App.label_msg.place(relx= 0.1, rely= 0.72, relwidth= 0.8, relheight= 0.06)

    @staticmethod
    def getInfoCheckin(idcheckin):
        checkin = Checkin()
        checkin.idcheckin = idcheckin
        return checkin.getInfoCheckin()

    @staticmethod
    def getAllToHospede(fk_idreserva, App):
        checkin = Checkin()
        checkin.fk_idreserva = fk_idreserva
        checkin.data_criacao = App.campo_busca.get()
        App.rCheckins = checkin.getAllToHospede()
        App.listarCheckins()
    
    @staticmethod
    def buscarCheckins(App):
        checkin = Checkin()
        checkin.data_criacao = App.campo_busca.get()
        App.rCheckins = checkin.buscar()
        App.listarCheckins()

    @staticmethod
    def deletarCheckin(idcheckin, Init):
        checkin = Checkin()
        checkin.idcheckin = idcheckin
        checkin.deletar()
        Init.control.renderTela('AppInitAdmin')
        Init.control.tela.abas.select(Init.control.tela.abaCheckin)
