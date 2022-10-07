from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font as tkFont
from tkcalendar import Calendar
import datetime
import math

#importando Controllers da aplicação
from ...Controllers.ReservaController import *
from ...Controllers.AcomodacaoController import *
from .AppInitAdmin import *
from .AppLojasAdmin import *

class AppReserva:
    def __init__(self, abaReserva, Init):
        #definindo a tela de renderização
        self.tela_render = "AppInitAdmin"
        
        #recebendo o init dentro da classe para passar para a qualquer função
        self.Init = Init
        self.abaReserva = abaReserva

        #menu de funções
        self.frame_menu = Frame(self.abaReserva, bg="#00767d")
        self.frame_menu.place(relx= 0.2, rely= 0.02, relwidth= 0.6, relheight= 0.05)

        self.btn_adicionar = Label(self.frame_menu, text="0       Adicionar       0",  bg="#0e6900", fg="#ffffff", font=tkFont.Font(family="Lucida Grande", size=13), border=2)
        self.btn_adicionar.place(relx= 0, rely= 0, relwidth= 0.15, relheight= 1)
        self.btn_adicionar.bind("<Button-1>", self.formularioReserva)

        self.campo_busca = Entry(self.frame_menu, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_busca.place(relx= 0.15, rely= 0, relwidth= 0.65, relheight= 1)
        self.btn_busca = Button(self.frame_menu, text="BUSCAR", bg="#ffffff", fg= "#000000", command=lambda:[buscarReservas()])
        self.btn_busca.place(relx= 0.8, rely= 0, relwidth= 0.2, relheight= 1)
        def buscarReservas():
            ReservaController.buscarReservas(self)
        ReservaController.buscarReservas(self)

    def listarReservas(self):
        #configuração da barra de rolagem
        self.f_base_scroll = Frame(self.abaReserva)
        self.f_base_scroll.place(relx= 0, rely= 0.09, relwidth= 1, relheight= 0.95)
        self.j_reservas = Frame(self.f_base_scroll, bg="#00767d")
        self.canva_rol = Canvas(self.j_reservas, bg="#00767d")
        self.canva_rol.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        self.yscrollbar = ttk.Scrollbar(self.j_reservas, orient="vertical", command=self.canva_rol.yview)
        self.yscrollbar.place(relx= 0.98, rely= 0, relwidth= 0.02, relheight= 1)
        self.canva_rol.configure(yscrollcommand=self.yscrollbar.set)
        self.canva_rol.bind('<Configure>', lambda e: self.canva_rol.configure(scrollregion = self.canva_rol.bbox('all')))
        self.frame_rol = Frame(self.canva_rol, bg="#00767d")
        self.canva_rol.create_window((0,0), window=self.frame_rol, anchor="nw")
        self.j_reservas.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        
        #for para criar frames dos reservas
        indice = 0
        #definindo os quadros da grade
        quadros = 3
        pos_relx = []
        rel_width = 1/quadros-0.02
        for i in range(quadros):
            pos_relx.append((1/quadros)*i)

        #chamando deletar hóspede
        def callDeletarReserva(event):
            if(messagebox.askquestion("Confirmar","Você tem certeza que quer deletar esta reserva?")=="yes"):
                ReservaController.deletarReserva(event.widget["text"].split()[0],self.Init)
        
        #chamando lojas
        def callLojasAdmin(event):
            self.idreserva = int(event.widget['text'].split()[0])
            AppLojasAdmin(self)

        for row in range(math.ceil(len(self.rReservas)/quadros)):
            quadros = len(self.rReservas)%quadros if row==math.ceil(len(self.rReservas)/quadros)-1 and len(self.rReservas)%quadros!=0 == 0 else quadros
            self.estrutura = Frame(self.j_reservas, bg="#00767d")
            self.estrutura.pack(in_=self.frame_rol, side=TOP, ipadx=0.47*self.Init.monitor_w, ipady=140, padx=10, pady=20)

            for col in range(quadros):
                self.temp_frame = Frame(self.estrutura, bg="#ffffff")
                self.temp_frame.place(relx=pos_relx[col], rely=0, relwidth=rel_width, relheight=1)

                labels = ["Quantidade de Hóspedes", "Antecipação", "Entrada Prevista", "Saída Prevista", "Data de Criação", "Hóspede", "Acomodação", "Valor", "Status"]
                for i in range(len(labels)):
                    Label(self.temp_frame, text=f"{labels[i]}: {str(self.rReservas[indice][i+1])}", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=12)).place(relx=0.07, y=220/len(labels)*i+10, height=30)
                
                btn_editar = Label(self.temp_frame, text=f"{self.rReservas[indice][0]}  Editar  {self.rReservas[indice][0]}",  bg="blue", fg= "#ffffff", font=tkFont.Font(family="Lucida Grande", size=13))
                btn_editar.place(x= 5, rely= 0.86, width= 60, height= 30)
                btn_editar.bind("<Button-1>", self.formularioReserva)

                btn_deletar = Label(self.temp_frame, text=f"{self.rReservas[indice][0]}  Deletar  {self.rReservas[indice][0]}",  bg="red", fg= "#ffffff", font=tkFont.Font(family="Lucida Grande", size=13))
                btn_deletar.place(x=70, rely= 0.86, width= 60, height= 30)
                btn_deletar.bind("<Button-1>", callDeletarReserva)

                if self.rReservas[indice][9] == "Checked-in":
                    btn_consumir = Label(self.temp_frame, text=f"{self.rReservas[indice][0]}  Consumir  {self.rReservas[indice][0]}",  bg="green", fg= "#ffffff", font=tkFont.Font(family="Lucida Grande", size=13))
                    btn_consumir.place(x=135, rely= 0.86, width= 80, height= 30)
                    btn_consumir.bind("<Button-1>", callLojasAdmin)

                indice+=1

    def formularioReserva(self, event):
        #puxando dados
        acao = event.widget["text"].split()[1]
        if acao=="Editar":
            self.idreserva = event.widget["text"].split()[0]
            self.dados_reserva = ReservaController.getInfoReserva(self.idreserva)
            qtd_hospedes = self.dados_reserva[0]
            antecipacao = self.dados_reserva[1]
            entrada_prevista = self.dados_reserva[2]
            saida_prevista = self.dados_reserva[3]
            hospede = self.dados_reserva[5]
            acomodacao = self.dados_reserva[6]
        else:
            qtd_hospedes = ''
            antecipacao = ''
            entrada_prevista = ''
            saida_prevista = ''
            hospede = ''
            acomodacao = ''

        #abrindo janela
        self.root2 = Toplevel()
        self.root2.title(acao)
        self.root2.configure(bg="#283d8f")
        w_root2 = 500
        self.root2.geometry(f"{w_root2}x400+{int(self.Init.monitor_w/2-w_root2/2)}+{100}")
        self.root2.resizable(False, False)
        self.root2.transient(self.Init.root)
        self.root2.focus_force()
        # self.root2.grab_set()
        # self.root2.iconbitmap(self.Init.pasta_app+"/imagens/logo2.ico")

        #definindo título
        self.label_titulo = Label(self.root2, text=f"{acao} Reserva", font=tkFont.Font(family="Lucida Grande", size=15), bg="#283d8f", fg= "#ffffff")
        self.label_titulo.place(relx= 0, rely= 0, relwidth= 1, relheight= 0.13)

        #abrindo frame para os widgets
        self.f_widgets = Frame(self.root2, bd= 4, bg="#283d8f")
        self.f_widgets.place(relx= 0, rely= 0.1, relwidth= 1, relheight= 0.8)

        #buscando todas as acomodacoes 
        self.acomodacoes = []
        for row in AcomodacaoController.listarAcomodacoes():
            self.acomodacoes.append(row[1])
        #buscando todas os hospedes 
        self.hospedes = []
        for row in HospedeController.listarHospedes():
            self.hospedes.append(row[0])

        #carregando widgets
        self.widgetsForm()

        #inserindo dados atuais no formulário de edição
        self.campo_qtd_hospedes.insert(0, qtd_hospedes)
        self.campo_antecipacao.insert(0, antecipacao)
        self.campo_entrada_prevista.insert(0, entrada_prevista)
        self.campo_saida_prevista.insert(0, saida_prevista)
        self.campo_acomodacao.set(acomodacao)
        self.campo_hospede.set(hospede)

        #executando ações do controlador
        def callReservaController():
            if acao=="Editar":
                ReservaController.alterarReserva(self, self.Init)
            else:
                ReservaController.cadastrarReserva(self, self.Init)
        self.btn_salvar = Button(self.root2, text="SALVAR", bg="#ffffff", fg= "#000000", command=lambda:[callReservaController()])
        self.btn_salvar.place(relx= 0.1, rely= 0.93, relwidth= 0.8, relheight= 0.07)
  
    def widgetsForm(self):

        self.label_qtd_hospedes = Label(self.f_widgets, text="Quantidade de Hóspedes", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_qtd_hospedes.place(relx= 0.1, rely= 0.02, relwidth= 0.45, relheight= 0.13)
        self.campo_qtd_hospedes = Entry(self.f_widgets, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_qtd_hospedes.place(relx= 0.55, rely= 0.02, relwidth= 0.35, relheight= 0.13)

        self.label_antecipacao = Label(self.f_widgets, text="Antecipação", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_antecipacao.place(relx= 0.1, rely= 0.17, relwidth= 0.25, relheight= 0.13)
        self.campo_antecipacao = Entry(self.f_widgets, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_antecipacao.place(relx= 0.35, rely= 0.17, relwidth= 0.55, relheight= 0.13)

        def inserir_entrada_prevista():
            data = self.calendario.get_date()
            self.calendario.destroy()
            self.campo_entrada_prevista.delete(0, END)
            self.campo_entrada_prevista.insert(0, data)
        def calendario_entrada_prevista():
            self.calendario = Calendar(self.f_widgets, bg="white", fg="black", locale="pt_br")
            self.calendario.place(relx=0.3, rely=0.4)
            self.btn_inserir_entrada_prevista = Button(self.calendario, text="inserir", bg="#ffffff", fg= "black", command=lambda:[inserir_entrada_prevista()])
            self.btn_inserir_entrada_prevista.place(relx= 0.5, rely= 0)
        self.label_entrada_prevista = Label(self.f_widgets, text="Entrada Prevista", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_entrada_prevista.place(relx= 0.1, rely= 0.32, relwidth= 0.4, relheight= 0.13)
        self.campo_entrada_prevista = Entry(self.f_widgets, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_entrada_prevista.place(relx= 0.5, rely= 0.32, relwidth= 0.3, relheight= 0.13)
        self.btn_calendario = Button(self.f_widgets, text="+", bg="#ffffff", fg= "#000000", command=lambda:[calendario_entrada_prevista()], font=("Arial", 25))
        self.btn_calendario.place(relx= 0.8, rely= 0.32, relwidth= 0.1, relheight= 0.13)

        def inserir_saida_prevista():
            data = self.calendario.get_date()
            self.calendario.destroy()
            self.campo_saida_prevista.delete(0, END)
            self.campo_saida_prevista.insert(0, data)
        def calendario_saida_prevista():
            self.calendario = Calendar(self.f_widgets, bg="white", fg="black", locale="pt_br")
            self.calendario.place(relx=0.3, rely=0.4)
            self.btn_inserir_saida_prevista = Button(self.calendario, text="inserir", bg="#ffffff", fg= "black", command=lambda:[inserir_saida_prevista()])
            self.btn_inserir_saida_prevista.place(relx= 0.5, rely= 0)
        self.label_saida_prevista = Label(self.f_widgets, text="Saída Prevista", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_saida_prevista.place(relx= 0.1, rely= 0.47, relwidth= 0.4, relheight= 0.13)
        self.campo_saida_prevista = Entry(self.f_widgets, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_saida_prevista.place(relx= 0.5, rely= 0.47, relwidth= 0.3, relheight= 0.13)
        self.btn_calendario = Button(self.f_widgets, text="+", bg="#ffffff", fg= "#000000", command=lambda:[calendario_saida_prevista()], font=("Arial", 25))
        self.btn_calendario.place(relx= 0.8, rely= 0.47, relwidth= 0.1, relheight= 0.13)

        self.label_acomodacao = Label(self.f_widgets, text="Acomodação", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_acomodacao.place(relx= 0.1, rely= 0.62, relwidth= 0.25, relheight= 0.13)
        self.campo_acomodacao = ttk.Combobox(self.f_widgets, values=self.acomodacoes, state="readonly", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_acomodacao.place(relx= 0.35, rely= 0.62, relwidth= 0.55, relheight= 0.13)

        self.label_hospede = Label(self.f_widgets, text="Hóspede", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_hospede.place(relx= 0.1, rely= 0.77, relwidth= 0.25, relheight= 0.13)
        self.campo_hospede = ttk.Combobox(self.f_widgets, values=self.hospedes, state="readonly", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_hospede.place(relx= 0.35, rely= 0.77, relwidth= 0.55, relheight= 0.13)

        #definindo label de mensagem
        self.label_msg = Label(self.root2)
