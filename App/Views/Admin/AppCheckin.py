from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font as tkFont
from tkcalendar import Calendar
import datetime
import math

#importando Controllers da aplicação
from ...Controllers.CheckinController import *
from ...Controllers.AcomodacaoController import *
from .AppInitAdmin import *

class AppCheckin:
    def __init__(self, abaCheckin, Init):
        #definindo a tela de renderização
        self.tela_render = "AppInitAdmin"
        
        #recebendo o init dentro da classe para passar para a qualquer função
        self.Init = Init
        self.abaCheckin = abaCheckin

        #menu de funções
        self.frame_menu = Frame(self.abaCheckin, bg="#00767d")
        self.frame_menu.place(relx= 0.2, rely= 0.02, relwidth= 0.6, relheight= 0.05)

        self.btn_adicionar = Label(self.frame_menu, text="0       Adicionar       0",  bg="#0e6900", fg="#ffffff", font=tkFont.Font(family="Lucida Grande", size=13), border=2)
        self.btn_adicionar.place(relx= 0, rely= 0, relwidth= 0.15, relheight= 1)
        self.btn_adicionar.bind("<Button-1>", self.formularioCheckin)

        self.campo_busca = Entry(self.frame_menu, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_busca.place(relx= 0.15, rely= 0, relwidth= 0.65, relheight= 1)
        self.btn_busca = Button(self.frame_menu, text="BUSCAR", bg="#ffffff", fg= "#000000", command=lambda:[buscarCheckins()])
        self.btn_busca.place(relx= 0.8, rely= 0, relwidth= 0.2, relheight= 1)
        def buscarCheckins():
            CheckinController.buscarCheckins(self)
        CheckinController.buscarCheckins(self)

    def listarCheckins(self):
        #configuração da barra de rolagem
        self.f_base_scroll = Frame(self.abaCheckin)
        self.f_base_scroll.place(relx= 0, rely= 0.09, relwidth= 1, relheight= 0.95)
        self.j_checkins = Frame(self.f_base_scroll, bg="#00767d")
        self.canva_rol = Canvas(self.j_checkins, bg="#00767d")
        self.canva_rol.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        self.yscrollbar = ttk.Scrollbar(self.j_checkins, orient="vertical", command=self.canva_rol.yview)
        self.yscrollbar.place(relx= 0.98, rely= 0, relwidth= 0.02, relheight= 1)
        self.canva_rol.configure(yscrollcommand=self.yscrollbar.set)
        self.canva_rol.bind('<Configure>', lambda e: self.canva_rol.configure(scrollregion = self.canva_rol.bbox('all')))
        self.frame_rol = Frame(self.canva_rol, bg="#00767d")
        self.canva_rol.create_window((0,0), window=self.frame_rol, anchor="nw")
        self.j_checkins.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        
        #for para criar frames dos checkins
        indice = 0
        #definindo os quadros da grade
        quadros = 4
        pos_relx = []
        rel_width = 1/quadros
        for i in range(quadros):
            pos_relx.append((1/quadros)*i)

        #chamando deletar hóspede
        def callDeletarCheckin(event):
            if(messagebox.askquestion("Confirmar","Você tem certeza que quer deletar este checkin?")=="yes"):
                CheckinController.deletarCheckin(event.widget["text"].split()[0],self.Init)

        for row in range(len(self.rCheckins)):
            self.estrutura = Frame(self.j_checkins, bg="white")
            self.estrutura.pack(in_=self.frame_rol, side=TOP, ipadx=0.47*self.Init.monitor_w, ipady=240, padx=10, pady=20)

            Label(self.estrutura, text=f"Data do Check-in: {self.rCheckins[indice][1]}", bg="#606060", fg= "white", font=tkFont.Font(family="Lucida Grande", size=15)).place(relx=0.1, rely=0.92, height=30)
            
            btn_editar = Label(self.estrutura, text=f"{self.rCheckins[indice][0]}  Editar  {self.rCheckins[indice][0]}",  bg="blue", fg= "#ffffff", font=tkFont.Font(family="Lucida Grande", size=13))
            btn_editar.place(x= 5, rely= 0.92, width= 60, height= 30)
            btn_editar.bind("<Button-1>", self.formularioCheckin)

            btn_deletar = Label(self.estrutura, text=f"{self.rCheckins[indice][0]}  Deletar  {self.rCheckins[indice][0]}",  bg="red", fg= "#ffffff", font=tkFont.Font(family="Lucida Grande", size=13))
            btn_deletar.place(x=70, rely= 0.92, width= 60, height= 30)
            btn_deletar.bind("<Button-1>", callDeletarCheckin)

            #pegando dados complementares
            self.rDados = []
            self.rDados.append(ReservaController.getInfoReserva(self.rCheckins[indice][2]))
            self.rDados.append(HospedeController.getInfoHospede(self.rCheckins[indice][3]))
            self.rDados.append(FuncionarioController.getInfoFuncionario(self.rCheckins[indice][4]))
            self.rDados.append(AcomodacaoController.getInfoAcomodacao(self.rCheckins[indice][5]))

            labels = [
                ["Quantidade de Hóspedes", "Antecipação", "Entrada Prevista", "Saída Prevista", "Data de Criação", "Hóspede"],
                ["Nome", "Cpf", "Rg", "Email", "Senha", "Telefone", "Data de Nascimento", "Sexo", "Foto_perfil", "Endereço", "Dados Bancários", "Data de Criação"],
                ["Nome", "Cpf", "Rg", "Email", "Senha", "Telefone", "Data de Nascimento", "Sexo", "Foto_perfil", "Endereço", "Dados Bancários", "Data de Criação", "Matrícula", "Cargo", "Nível de acesso", "Data de Admissão"],
                ["Descrição", "Andar", "Capacidade", "Observações", "Status", "Categoria", "Valor"]
                ]
            titulos = ["Dados da Reserva", "Dados do Hóspede", "Dados do Funcionário", "Dados da Acomodação"]
            for col in range(quadros):
                self.temp_frame = Frame(self.estrutura, bg="#ffffff")
                self.temp_frame.place(relx=pos_relx[col], rely=0, relwidth=rel_width, relheight=0.9)
                Label(self.temp_frame, text=f"{titulos[col]}", bg="#606060", fg= "white", font=tkFont.Font(family="Lucida Grande", size=13, weight="bold")).place(relx=0, y=0, relwidth=1,height=30)

                for i in range(len(labels[col])):
                    Label(self.temp_frame, text=f"{labels[col][i]}: {str(self.rDados[col][i])}", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=12)).place(relx=0.07, y=100/len(labels)*i+30, height=30)

            indice+=1

    def formularioCheckin(self, event):
        #puxando dados
        acao = event.widget["text"].split()[1]
        if acao=="Editar":
            self.idcheckin = event.widget["text"].split()[0]
            self.dados_checkin = CheckinController.getInfoCheckin(self.idcheckin)
            data_criacao = self.dados_checkin[0]
            idreserva = self.dados_checkin[2]
            idhospede = self.dados_checkin[3]
            idfuncionario = self.dados_checkin[4]
        else:
            data_criacao = ''
            idreserva = ''
            idhospede = ''
            idfuncionario = ''

        #abrindo janela
        self.root2 = Toplevel()
        self.root2.title(acao)
        self.root2.configure(bg="#283d8f")
        w_root2 = 500
        self.root2.geometry(f"{w_root2}x300+{int(self.Init.monitor_w/2-w_root2/2)}+{100}")
        self.root2.resizable(False, False)
        self.root2.transient(self.Init.root)
        self.root2.focus_force()
        self.root2.grab_set()
        self.root2.iconbitmap(self.Init.pasta_app+"\\imagens\\logo2.ico")

        #definindo título
        self.label_titulo = Label(self.root2, text=f"{acao} Checkin", font=tkFont.Font(family="Lucida Grande", size=15), bg="#283d8f", fg= "#ffffff")
        self.label_titulo.place(relx= 0, rely= 0, relwidth= 1, relheight= 0.13)

        #abrindo frame para os widgets
        self.f_widgets = Frame(self.root2, bd= 4, bg="#283d8f")
        self.f_widgets.place(relx= 0, rely= 0.1, relwidth= 1, relheight= 0.8)

        #buscando todas os hospedes 
        self.hospedes = []
        for row in HospedeController.listarHospedes():
            self.hospedes.append(row[0])
        #buscando todas os funcionario 
        self.funcionarios = []
        for row in FuncionarioController.listarFuncionarios():
            self.funcionarios.append(row[0])
        #buscando todas as reservas
        self.reservas = []
        for row in ReservaController.listarReservas():
            if row[3]=="Confirmada":
                self.reservas.append(row[6])

        #carregando widgets
        self.widgetsForm()

        def callListarReservas(event):
            #buscando todas as reservas
            fk_idhospede = HospedeController.getHospedePorNome(self.campo_hospede.get())[0]
            self.reservas = []
            for row in ReservaController.listarAllToHospede(fk_idhospede):
                if row[3]=="Confirmada":
                    self.reservas.append(row[6])
            self.campo_reserva['values'] = self.reservas
            self.campo_reserva.set('')
        self.campo_hospede.bind("<<ComboboxSelected>>", callListarReservas)
        def callSelecionarHospede(event):
            #buscando todas as reservas
            nome_hospede = ReservaController.getHospedePorDataReserva(self.campo_reserva.get())[0]
            self.campo_hospede.set(nome_hospede)
        self.campo_reserva.bind("<<ComboboxSelected>>", callSelecionarHospede)

        #inserindo dados atuais no formulário de edição
        try:
            reserva = ReservaController.getInfoReserva(idreserva)[4]
            hospede = HospedeController.getInfoHospede(idhospede)[0]
            funcionario = FuncionarioController.getInfoFuncionario(idfuncionario)[0]
            self.campo_hospede.set(hospede)
            self.campo_reserva.set(reserva)
            self.campo_funcionario.set(funcionario)
        except:
            pass

        #executando ações do controlador
        def callCheckinController():
            if acao=="Editar":
                CheckinController.alterarCheckin(self, self.Init)
            else:
                CheckinController.cadastrarCheckin(self, self.Init)
        self.btn_salvar = Button(self.root2, text="SALVAR", bg="#ffffff", fg= "#000000", command=lambda:[callCheckinController()])
        self.btn_salvar.place(relx= 0.1, rely= 0.8, relwidth= 0.8, relheight= 0.1)

    def widgetsForm(self):

        self.label_hospede = Label(self.f_widgets, text="Hóspede", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_hospede.place(relx= 0.1, rely= 0.05, relwidth= 0.25, relheight= 0.2)
        self.campo_hospede = ttk.Combobox(self.f_widgets, values=self.hospedes, state="readonly", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_hospede.place(relx= 0.35, rely= 0.05, relwidth= 0.55, relheight= 0.2)

        self.label_reserva = Label(self.f_widgets, text="Reserva", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_reserva.place(relx= 0.1, rely= 0.3, relwidth= 0.25, relheight= 0.2)
        self.campo_reserva = ttk.Combobox(self.f_widgets, values=self.reservas, state="readonly", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_reserva.place(relx= 0.35, rely= 0.3, relwidth= 0.55, relheight= 0.2)

        self.label_funcionario = Label(self.f_widgets, text="Funcionario", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_funcionario.place(relx= 0.1, rely= 0.55, relwidth= 0.25, relheight= 0.2)
        self.campo_funcionario = ttk.Combobox(self.f_widgets, values=self.funcionarios, state="readonly", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_funcionario.place(relx= 0.35, rely= 0.55, relwidth= 0.55, relheight= 0.2)

        #definindo label de mensagem
        self.label_msg = Label(self.root2)
