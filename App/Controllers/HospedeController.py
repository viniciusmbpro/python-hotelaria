#importando modelos
from tkinter import END
import datetime
import os
from PIL import Image, ImageTk
import hashlib

from ..Models import *

class HospedeController():
    @staticmethod
    def cadastrarHospede(App, Init):
        hospede = Hospede()
        hospede.email = App.campo_email.get()
        result = hospede.getHospedePorEmail()
        hospede.nome = App.campo_nome.get()
        hospede.rg = App.campo_rg.get()
        hospede.cpf = App.campo_cpf.get()
        hospede.senha = App.campo_senha.get()
        hospede.telefone = App.campo_telefone.get()
        hospede.data_nascimento = App.campo_data_nascimento.get()
        hospede.sexo = App.campo_sexo.get()

        # codificando o nome do hospede usando a hash md5 para usar como nome da imagem
        nomeImagem = hashlib.md5(hospede.nome.encode()).hexdigest()
        img = Image.open(App.imgPathFotoPerfil)
        img = img.resize((round(400), round((img.size[1]/img.size[0])*400)), Image.ANTIALIAS)
        img.save(f"{App.Init.pasta_app}\\imagens\\{nomeImagem}.png", format('png'))
        hospede.foto_perfil = f"{nomeImagem}.png"

        hospede.endereco = App.campo_endereco.get()
        hospede.dados_bancarios = App.campo_dados_bancarios.get()
        hospede.data_criacao = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        if(hospede.validarDados(["nome", "email", "rg", "cpf"], "Cadastrar")):
            hospede.cadastrar()

            Init.control.renderTela(App.tela_render)

            #acionando label sucesso após a renderização, puxando um novo
            if(App.tela_render!="AppInitAdmin"):
                Init.control.tela.label_msg.configure(text="cadastro realizado com sucesso", bg="green", fg="white")
                Init.control.tela.label_msg.place(relx= 0.1, rely= 0.8, relwidth= 0.8, relheight= 0.06)
            else:
                Init.control.tela.abas.select(Init.control.tela.abaHospede)
                App.label_msg.configure(text="cadastro realizado com sucesso", bg="green", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.8, relwidth= 0.8, relheight= 0.06)
        else:
            if(App.tela_render!="AppInitAdmin"):
                App.label_msg.configure(text="falha no cadastro, reveja suas informações", bg="red", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.8, relwidth= 0.8, relheight= 0.06)
            else:
                App.label_msg.configure(text="falha no cadastro, reveja suas informações", bg="red", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.8, relwidth= 0.8, relheight= 0.06)

    @staticmethod
    def alterarHospede(App, Init):
        hospede = Hospede()
        hospede.email = App.campo_email.get()
        result = hospede.getHospedePorEmail()
        hospede.nome = App.campo_nome.get()
        hospede.rg = App.campo_rg.get()
        hospede.cpf = App.campo_cpf.get()
        hospede.senha = App.campo_senha.get()
        hospede.telefone = App.campo_telefone.get()
        hospede.data_nascimento = App.campo_data_nascimento.get()
        hospede.sexo = App.campo_sexo.get()
        if App.__class__.__name__=="AppConfig":
            print(App.imgPathFotoPerfil)
            print(f"{Init.pasta_app}\\imagens\\{Init.session['foto_perfil']}")
            if App.imgPathFotoPerfil!=f"{Init.pasta_app}\\imagens\\{Init.session['foto_perfil']}":
                #apagando imagem antiga
                os.remove(f"{Init.pasta_app}\\imagens\\{Init.session['foto_perfil']}") 

                # codificando o nome do hospede usando a hash md5 para usar como nome da imagem
                nomeImagem = hashlib.md5(hospede.nome.encode()).hexdigest()
                img = Image.open(App.imgPathFotoPerfil)
                img = img.resize((round(400), round((img.size[1]/img.size[0])*400)), Image.ANTIALIAS)
                img.save(f"{App.Init.pasta_app}\\imagens\\{nomeImagem}.png", format('png'))
                hospede.foto_perfil = f"{nomeImagem}.png"
            else:
                hospede.foto_perfil = Init.session['foto_perfil']
        elif App.__class__.__name__=="AppHospede":
            #apagando imagem antiga
            os.remove(f"{App.Init.pasta_app}\\imagens\\{HospedeController.getInfoHospede(App.idhospede)[8]}") 

            # codificando o nome do hospede usando a hash md5 para usar como nome da imagem
            nomeImagem = hashlib.md5(hospede.nome.encode()).hexdigest()
            img = Image.open(App.imgPathFotoPerfil)
            img = img.resize((round(400), round((img.size[1]/img.size[0])*400)), Image.ANTIALIAS)
            img.save(f"{App.Init.pasta_app}\\imagens\\{nomeImagem}.png", format('png'))
            hospede.foto_perfil = f"{nomeImagem}.png"

        hospede.endereco = App.campo_endereco.get()
        hospede.dados_bancarios = App.campo_dados_bancarios.get()
        hospede.idhospede = App.idhospede
        if(hospede.validarDados(["nome", "email", "rg", "cpf"], "Alterar")):
            hospede.alterar()
            Init.control.renderTela(App.tela_render)

            #acionando label sucesso após a renderização, puxando um novo
            if(App.tela_render!="AppInitAdmin"):
                #atualializando session
                if hospede.idhospede == Init.session['idusuario']:
                    Init.session['nome'] = hospede.nome.split()
                    Init.session['foto_perfil'] = hospede.foto_perfil
                Init.control.tela.label_msg.configure(text="alteração realizada com sucesso", bg="green", fg="white")
                Init.control.tela.label_msg.place(relx= 0.1, rely= 0.8, relwidth= 0.8, relheight= 0.06)
            else:
                Init.control.tela.abas.select(Init.control.tela.abaHospede)
                App.label_msg.configure(text="alteração realizada com sucesso", bg="green", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.8, relwidth= 0.8, relheight= 0.06)
        else:
            if(App.tela_render!="AppInitAdmin"):
                App.label_msg.configure(text="falha no cadastro, reveja suas informações", bg="red", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.8, relwidth= 0.8, relheight= 0.06)
            else:
                App.label_msg.configure(text="falha no cadastro, reveja suas informações", bg="red", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.8, relwidth= 0.8, relheight= 0.06)

    @staticmethod
    def getInfoHospede(idhospede):
        hospede = Hospede()
        hospede.idhospede = idhospede
        return hospede.getInfoHospede()

    @staticmethod
    def getHospedePorNome(nome):
        hospede = Hospede()
        hospede.nome = nome
        return hospede.getHospedePorNome()
    
    @staticmethod
    def buscarHospedes(App):
        hospede = Hospede()
        hospede.nome = App.campo_busca.get()
        App.rHospedes = hospede.buscar()
        App.listarHospedes()

    @staticmethod
    def listarHospedes():
        hospede = Hospede()
        return hospede.listar()

    @staticmethod
    def deletarHospede(idhospede, Init):
        hospede = Hospede()
        hospede.idhospede = idhospede
        hospede.deletar()
        Init.control.renderTela('AppInitAdmin')
        Init.control.tela.abas.select(Init.control.tela.abaHospede)
