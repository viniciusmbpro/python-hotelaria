#importando modelos
from tkinter import END
import os
from PIL import Image, ImageTk
import hashlib
import datetime

from ..Models.Funcionario import *

class FuncionarioController():
    @staticmethod
    def cadastrarFuncionario(App, Init):
        funcionario = Funcionario()
        funcionario.email = App.campo_email.get()
        result = funcionario.getFuncionarioPorEmail()
        funcionario.nome = App.campo_nome.get()
        funcionario.rg = App.campo_rg.get()
        funcionario.cpf = App.campo_cpf.get()
        funcionario.senha = App.campo_senha.get()
        funcionario.telefone = App.campo_telefone.get()
        funcionario.data_nascimento = App.campo_data_nascimento.get()
        funcionario.sexo = App.campo_sexo.get()

        # codificando o nome do funcionario usando a hash md5 para usar como nome da imagem
        nomeImagem = hashlib.md5(funcionario.nome.encode()).hexdigest()
        img = Image.open(App.imgPathFotoPerfil)
        img = img.resize((round(400), round((img.size[1]/img.size[0])*400)), Image.ANTIALIAS)
        img.save(f"{App.Init.pasta_app}\\imagens\\{nomeImagem}.png", format('png'))
        funcionario.foto_perfil = f"{nomeImagem}.png"

        funcionario.endereco = App.campo_endereco.get()
        funcionario.dados_bancarios = App.campo_dados_bancarios.get()
        funcionario.data_criacao = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        funcionario.matricula = App.campo_matricula.get()
        funcionario.cargo = App.campo_cargo.get()
        funcionario.nivel_acesso = App.campo_nivel_acesso.get()
        funcionario.data_admissao = App.campo_data_admissao.get()

        if(funcionario.validarDados(["nome", "email", "rg", "cpf"], "Cadastrar")):
            funcionario.cadastrar()

            Init.control.renderTela(App.tela_render)

            #acionando label sucesso após a renderização, puxando um novo
            if(App.tela_render!="AppInitAdmin"):
                Init.control.tela.label_msg.configure(text="cadastro realizado com sucesso", bg="green", fg="white")
                Init.control.tela.label_msg.place(relx= 0.1, rely= 0.87, relwidth= 0.8, relheight= 0.06)
            else:
                Init.control.tela.abas.select(Init.control.tela.abaFuncionario)
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
    def alterarFuncionario(App, Init):
        funcionario = Funcionario()
        funcionario.email = App.campo_email.get()
        funcionario.nome = App.campo_nome.get()
        funcionario.rg = App.campo_rg.get()
        funcionario.cpf = App.campo_cpf.get()
        funcionario.senha = App.campo_senha.get()
        funcionario.telefone = App.campo_telefone.get()
        funcionario.data_nascimento = App.campo_data_nascimento.get()
        funcionario.sexo = App.campo_sexo.get()

        if App.__class__.__name__=="AppConfigAdmin":
            if App.imgPathFotoPerfil!=f"{Init.pasta_app}\\imagens\\{Init.session['foto_perfil']}":
                #apagando imagem antiga
                os.remove(f"{Init.pasta_app}\\imagens\\{Init.session['foto_perfil']}") 

                # codificando o nome do funcionario usando a hash md5 para usar como nome da imagem
                nomeImagem = hashlib.md5(funcionario.nome.encode()).hexdigest()
                img = Image.open(App.imgPathFotoPerfil)
                img = img.resize((round(400), round((img.size[1]/img.size[0])*400)), Image.ANTIALIAS)
                img.save(f"{App.Init.pasta_app}\\imagens\\{nomeImagem}.png", format('png'))
                funcionario.foto_perfil = f"{nomeImagem}.png"
            else:
                funcionario.foto_perfil = Init.session['foto_perfil']
        elif App.__class__.__name__=="AppFuncionario":
            #apagando imagem antiga
            os.remove(f"{App.Init.pasta_app}\\imagens\\{FuncionarioController.getInfoFuncionario(App.idfuncionario)[8]}") 

            # codificando o nome do funcionario usando a hash md5 para usar como nome da imagem
            nomeImagem = hashlib.md5(funcionario.nome.encode()).hexdigest()
            img = Image.open(App.imgPathFotoPerfil)
            img = img.resize((round(400), round((img.size[1]/img.size[0])*400)), Image.ANTIALIAS)
            img.save(f"{App.Init.pasta_app}\\imagens\\{nomeImagem}.png", format('png'))
            funcionario.foto_perfil = f"{nomeImagem}.png"

        funcionario.endereco = App.campo_endereco.get()
        funcionario.dados_bancarios = App.campo_dados_bancarios.get()
        funcionario.matricula = App.campo_matricula.get()
        funcionario.cargo = App.campo_cargo.get()
        funcionario.nivel_acesso = App.campo_nivel_acesso.get()
        funcionario.data_admissao = App.campo_data_admissao.get()
        funcionario.idfuncionario = App.idfuncionario
        if(funcionario.validarDados(["nome", "email", "rg", "cpf"], "Alterar")):
            funcionario.alterar()

            Init.control.renderTela(App.tela_render)

            #atualializando session
            if funcionario.idfuncionario == Init.session['idusuario']:
                Init.session['nome'] = funcionario.nome.split()
                Init.session['foto_perfil'] = funcionario.foto_perfil

            #acionando label sucesso após a renderização, puxando um novo
            if(App.tela_render!="AppInitAdmin"):
                Init.control.tela.label_msg.configure(text="alteração realizada com sucesso", bg="green", fg="white")
                Init.control.tela.label_msg.place(relx= 0.1, rely= 0.87, relwidth= 0.8, relheight= 0.06)
            else:
                Init.control.tela.abas.select(Init.control.tela.abaFuncionario)
                App.label_msg.configure(text="alteração realizada com sucesso", bg="green", fg="white")
                App.label_msg.place(relx= 0.1, rely= 0.87, relwidth= 0.8, relheight= 0.06)
        else:
            App.label_msg.configure(text="falha, pelo meno 3 caracteres em cada campo", bg="red", fg="white")
            App.label_msg.place(relx= 0.1, rely= 0.87, relwidth= 0.8, relheight= 0.06)

    @staticmethod
    def getInfoFuncionario(idfuncionario):
        funcionario = Funcionario()
        funcionario.idfuncionario = idfuncionario
        return funcionario.getInfoFuncionario()

    @staticmethod
    def buscarFuncionarios(App):
        funcionario = Funcionario()
        funcionario.nome = App.campo_busca.get()
        App.rFuncionarios = funcionario.buscar()
        App.listarFuncionarios()

    @staticmethod
    def getFuncionarioPorNome(nome):
        funcionario = Funcionario()
        funcionario.nome = nome
        return funcionario.getFuncionarioPorNome()
    
    @staticmethod
    def listarFuncionarios():
        funcionario = Funcionario()
        return funcionario.listar()

    @staticmethod
    def deletarFuncionario(idfuncionario, Init):
        funcionario = Funcionario()
        funcionario.idfuncionario = idfuncionario
        funcionario.deletar()
        Init.control.renderTela('AppInitAdmin')
        Init.control.tela.abas.select(Init.control.tela.abaFuncionario)
