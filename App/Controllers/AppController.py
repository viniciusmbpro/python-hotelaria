from ..Views import *
from ..Models.Hospede import *
from ..Models.Funcionario import *

class AppController():
    def __init__(self, telaInicial):
        self.Init = globals()["AppInit"](self)
        self.Init.session = {'idusuario':0, 'nome':['','',''], 'foto_perfil':''}
        self.tela = globals()[telaInicial](self.Init)
        self.Init.loop()
        
    def renderTela(self, tela_alvo):
        self.tela.framePrincipal.destroy()
        self.tela = globals()[tela_alvo](self.Init)

    def autenticar(self, App, Init):
        hospede = Hospede()
        hospede.email = App.campo_email.get()
        hospede.senha = App.campo_senha.get()
        result = hospede.autenticar()
        if result:
            nome = result[0].split()
            idusuario = result[1]
            foto_perfil = result[2]
            Init.session = {'idusuario':idusuario, 'nome':nome, 'foto_perfil':foto_perfil}
            self.renderTela('AppInitHospede')
        elif not result:
            funcionario = Funcionario()
            funcionario.email = App.campo_email.get()
            funcionario.senha = App.campo_senha.get()
            result = funcionario.autenticar()
            if result :
                nome = result[0].split()
                idusuario = result[1]
                foto_perfil = result[2]
                Init.session = {'idusuario':idusuario, 'nome':nome, 'foto_perfil':foto_perfil}
                self.renderTela('AppInitAdmin')
            else:
                App.label_erro.place(relx= 0.1, rely= 0.6, relwidth= 0.8, relheight= 0.06)
        else:
            App.label_erro.place(relx= 0.1, rely= 0.6, relwidth= 0.8, relheight= 0.06)

    def sair(self):
        self.Init.session = {'idusuario':'', 'nome':['','',''], 'foto_perfil':''}
        self.renderTela('AppLogin')
