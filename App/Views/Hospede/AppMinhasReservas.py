from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import font as tkFont
from PIL import Image, ImageTk
from tkcalendar import Calendar
from tkinter import messagebox
import math

#importando views
from .AppLojas import *

#importando Controllers da aplicação
from ...Controllers.HospedeController import *
from ...Controllers.ReservaController import *
from ...Controllers.CategoriaController import *
from ...Controllers.ProdutoController import *
from ...Controllers.ReservaController import *

class AppMinhasReservas:
    def __init__(self, abaMinhasReservas, Init):
        #definindo variáveis padrão
        self.tela_render = "AppInitHospede"
        self.Init = Init
        self.abaMinhasReservas = abaMinhasReservas

        #menu de funções
        self.frame_menu = Frame(self.abaMinhasReservas, bg="#00767d")
        self.frame_menu.place(relx= 0.2, rely= 0.02, relwidth= 0.6, relheight= 0.05)

        self.campo_busca = Entry(self.frame_menu, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_busca.place(relx= 0, rely= 0, relwidth= 0.7, relheight= 1)
        self.btn_busca = Button(self.frame_menu, text="BUSCAR", bg="#ffffff", fg= "#000000", command=lambda:[buscarReservas()])
        self.btn_busca.place(relx= 0.7, rely= 0, relwidth= 0.3, relheight= 1)
        def buscarReservas():
            ReservaController.getAllToHospede(self.Init.session['idusuario'], self)
        ReservaController.getAllToHospede(self.Init.session['idusuario'], self)

    def listarReservas(self):
        #configuração da barra de rolagem
        self.f_base_scroll = Frame(self.abaMinhasReservas)
        self.f_base_scroll.place(relx= 0, rely= 0.08, relwidth= 1, relheight= 0.92)
        self.j_acomodacoes = Frame(self.f_base_scroll, bg="#00767d")
        self.canva_rol = Canvas(self.j_acomodacoes, bg="#00767d")
        self.canva_rol.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        self.yscrollbar = ttk.Scrollbar(self.j_acomodacoes, orient="vertical", command=self.canva_rol.yview)
        self.yscrollbar.place(relx= 0.98, rely= 0, relwidth= 0.02, relheight= 1)
        self.canva_rol.configure(yscrollcommand=self.yscrollbar.set)
        self.canva_rol.bind('<Configure>', lambda e: self.canva_rol.configure(scrollregion = self.canva_rol.bbox('all')))
        self.frame_rol = Frame(self.canva_rol, bg="#00767d")
        self.canva_rol.create_window((0,0), window=self.frame_rol, anchor="nw")
        self.j_acomodacoes.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)

        #renderizando a tela de lojas
        def callRenderTela(event):
            self.idreserva = event.widget["text"].split()[0]
            AppLojas(self)
        #chamando cancelar reserva
        def callCancelarReserva(event):
            if(messagebox.askquestion("Confirmar","Você tem certeza que quer CANCELAR esta reserva?")=="yes"):
                ReservaController.cancelar(int(event.widget['text'].split()[0]))
                ReservaController.getAllToHospede(self.Init.session['idusuario'], self)
        
        #for para criar frames dos acomodacoes
        indice = 0
        #definindo os quadros da grade
        quadros = 1
        pos_relx = []
        rel_width = 1/quadros-0.02
        for i in range(quadros):
            pos_relx.append((1/quadros)*i)

        if len(self.rReservas)==0:
            Label(self.abaMinhasReservas, text="Você não tem reservas", bg="#6e1916", fg="white", font=tkFont.Font(family="Lucida Grande", size=20)).place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.1)

        for row in range(math.ceil(len(self.rReservas)/quadros)):
            quadros = len(self.rReservas)%quadros if row==math.ceil(len(self.rReservas)/quadros)-1 and len(self.rReservas)%quadros!=0 == 0 else quadros
            self.estrutura = Frame(self.j_acomodacoes, bg="#00767d")
            self.estrutura.pack(in_=self.frame_rol, side=TOP, ipadx=0.47*self.Init.monitor_w, ipady=120, padx=10, pady=20)

            for col in range(quadros):
                self.temp_frame = Frame(self.estrutura, bg="#002e4f")
                self.temp_frame.place(relx=pos_relx[col], rely=0, relwidth=rel_width, relheight=1)

                Label(self.temp_frame, text=f"Entrada Prevista: {self.rReservas[indice][4]} | Saída Prevista: {self.rReservas[indice][5]}", bg="#004170", fg= "white", anchor="w", bd=50, font=tkFont.Font(family="Lucida Grande", size=15)).place(relx= 0, rely= 0.05, relwidth=0.49, relheight= 0.2)
                consumo = ReservaController.calcularConsumo(self.rReservas[indice][0])
                Label(self.temp_frame, text=f"Gasto de Consumo: {consumo[3]} | Gasto total: {consumo[4]}", bg="#004170", fg= "white", anchor="w", bd=50, font=tkFont.Font(family="Lucida Grande", size=14)).place(relx= 0.51, rely= 0.05, relwidth=0.49, relheight= 0.2)

                self.dados_1 = Frame(self.temp_frame, bg="#004170")
                self.dados_1.place(relx= 0.05, rely= 0.3, relwidth=0.35, relheight= 0.6)

                Label(self.dados_1, text=f"Data Criação: {str(self.rReservas[indice][6])}", bg="#004170", fg= "white", anchor="w", bd=50, font=tkFont.Font(family="Lucida Grande", size=14)).place(relx= 0, rely=0, relwidth=1, relheight= 0.25)

                Label(self.dados_1, text=f"Quantidade de pessoas: {str(self.rReservas[indice][1])}", bg="#004170", fg= "white", anchor="w", bd=50, font=tkFont.Font(family="Lucida Grande", size=14)).place(relx= 0, rely=0.25, relwidth=1, relheight= 0.25)

                Label(self.dados_1, text=f"Status: {str(self.rReservas[indice][3])}", bg="#004170", fg= "white", anchor="w", bd=50, font=tkFont.Font(family="Lucida Grande", size=14), highlightbackground="white", highlightthickness= 1).place(relx= 0, rely=0.5, relwidth=1, relheight= 0.25)

                Label(self.dados_1, text=f"Antecipação: {str(self.rReservas[indice][2])}", bg="#1a6142", fg= "white", anchor="w", bd=50, font=tkFont.Font(family="Lucida Grande", size=13)).place(relx= 0, rely=0.75, relwidth=1, relheight= 0.25)

                self.dados_2 = Frame(self.temp_frame, bg="#004170")
                self.dados_2.place(relx= 0.42, rely= 0.3, relwidth=0.35, relheight= 0.6)

                Label(self.dados_2, text=f"Quarto: {str(self.rReservas[indice][7])}", bg="#004170", fg= "white", anchor="w", bd=50, font=tkFont.Font(family="Lucida Grande", size=14)).place(relx= 0, rely=0, relwidth=1, relheight= 0.25)

                Label(self.dados_2, text=f"Andar: {str(self.rReservas[indice][8])}", bg="#004170", fg= "white", anchor="w", bd=50, font=tkFont.Font(family="Lucida Grande", size=14)).place(relx= 0, rely=0.25, relwidth=1, relheight= 0.25)

                Label(self.dados_2, text=f"Categoria: {str(self.rReservas[indice][10])}", bg="#004170", fg= "white", anchor="w", bd=50, font=tkFont.Font(family="Lucida Grande", size=14)).place(relx= 0, rely=0.5, relwidth=1, relheight= 0.25)

                Label(self.dados_2, text=f"Valor: {str(self.rReservas[indice][11])}", bg="#1a5361", fg= "white", anchor="w", bd=50, font=tkFont.Font(family="Lucida Grande", size=13)).place(relx= 0, rely=0.75, relwidth=1, relheight= 0.25)
                
                if str(self.rReservas[indice][3])=="Checked-in":
                    btn_loja = Button(self.temp_frame, text=f"{self.rReservas[indice][0]}                           Consumir                           {self.rReservas[indice][0]}",  bg="#257025", fg= "#ffffff", font=tkFont.Font(family="Lucida Grande", size=12))
                    btn_loja.place(relx= 0.79, rely= 0.8, relwidth= 0.2, relheight= 0.15)
                    btn_loja.bind("<Button-1>", callRenderTela)
                if str(self.rReservas[indice][3])=="Confirmada":
                    btn_loja = Button(self.temp_frame, text=f"{self.rReservas[indice][0]}                           Cancelar                           {self.rReservas[indice][0]}",  bg="red", fg= "#ffffff", font=tkFont.Font(family="Lucida Grande", size=12))
                    btn_loja.place(relx= 0.79, rely= 0.8, relwidth= 0.2, relheight= 0.15)
                    btn_loja.bind("<Button-1>", callCancelarReserva)

                indice+=1

    def formularioReserva(self, event):
        #puxando dados
        self.idacomodacao = event.widget["text"].split()[0]
        self.idhospede = self.Init.session['idusuario']
        self.dados_acomodacao = ReservaController.getInfoReserva(self.idacomodacao)
        descricao = self.dados_acomodacao[0]
        andar = self.dados_acomodacao[1]
        capacidade = self.dados_acomodacao[2]
        observacoes = self.dados_acomodacao[3]
        status = self.dados_acomodacao[4]
        categoria = self.dados_acomodacao[5]
        valor = self.dados_acomodacao[6]

        #abrindo janela
        self.root2 = Toplevel()
        self.root2.title("Efetuar Reserva")
        self.root2.configure(bg="#002e4f")
        w_root2 = 500
        self.root2.geometry(f"{w_root2}x400+{int(self.Init.monitor_w/2-w_root2/2)}+{100}")
        self.root2.resizable(False, False)
        self.root2.transient(self.Init.root)
        self.root2.focus_force()
        # self.root2.grab_set()
        # self.root2.iconbitmap(self.Init.pasta_app+"/imagens/logo2.ico")

        #definindo título
        self.label_titulo = Label(self.root2, text=f"Reservar {descricao}", font=tkFont.Font(family="Lucida Grande", size=15), bg="#002e4f", fg= "#ffffff")
        self.label_titulo.place(relx= 0, rely= 0, relwidth= 1, relheight= 0.13)

        #abrindo frame para os widgets
        self.f_widgets = Frame(self.root2, bd= 4, bg="#002e4f")
        self.f_widgets.place(relx= 0, rely= 0.1, relwidth= 1, relheight= 0.8)

        #configurando dados dos widgets
        self.qtd_hospedess = []
        for i in range(capacidade):
            self.qtd_hospedess.append(i+1)
        self.stringVarReserva = StringVar()
        self.stringVarValor = StringVar()
        self.stringVarHospede = StringVar()

        #carregando widgets
        self.widgetsForm()

        #inserindo dados atuais no formulário de edição
        self.campo_qtd_hospedes.current(0)
        self.campo_antecipacao.insert(0, 0)
        # self.campo_entrada_prevista.insert(0, 'entrada_prevista')
        # self.campo_saida_prevista.insert(0, 'saida_prevista')
        self.stringVarReserva.set(descricao)
        self.stringVarValor.set(valor)
        self.stringVarHospede.set(HospedeController.getInfoHospede(self.idhospede)[1])

        self.btn_salvar = Button(self.root2, text="Confirmar Reserva", bg="#257025", fg= "#ffffff", font=tkFont.Font(family="Lucida Grande", size=13), command=lambda:[ReservaController.cadastrarReserva(self, self.Init)])
        self.btn_salvar.place(relx= 0.1, rely= 0.9, relwidth= 0.8, relheight= 0.07)

    def widgetsForm(self):

        self.label_qtd_hospedes = Label(self.f_widgets, text="Quantidade de Hóspedes", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_qtd_hospedes.place(relx= 0.1, rely= 0.02, relwidth= 0.45, relheight= 0.13)
        self.campo_qtd_hospedes = ttk.Combobox(self.f_widgets, values=self.qtd_hospedess, state="readonly", font=tkFont.Font(family="Lucida Grande", size=13))
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
            self.calendario.place(relx=0.05, rely=0.1)
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
            self.calendario.place(relx=0.05, rely=0.2)
            self.btn_inserir_saida_prevista = Button(self.calendario, text="inserir", bg="#ffffff", fg= "black", command=lambda:[inserir_saida_prevista()])
            self.btn_inserir_saida_prevista.place(relx= 0.5, rely= 0)
        self.label_saida_prevista = Label(self.f_widgets, text="Saída Prevista", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_saida_prevista.place(relx= 0.1, rely= 0.47, relwidth= 0.4, relheight= 0.13)
        self.campo_saida_prevista = Entry(self.f_widgets, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_saida_prevista.place(relx= 0.5, rely= 0.47, relwidth= 0.3, relheight= 0.13)
        self.btn_calendario = Button(self.f_widgets, text="+", bg="#ffffff", fg= "#000000", command=lambda:[calendario_saida_prevista()], font=("Arial", 25))
        self.btn_calendario.place(relx= 0.8, rely= 0.47, relwidth= 0.1, relheight= 0.13)

        self.campo_acomodacao = Entry(self.f_widgets, textvariable=self.stringVarReserva)

        self.label_valor = Label(self.f_widgets, text="Valor da Diária:", bg="#257048", fg= "white", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_valor.place(relx= 0.1, rely= 0.62, relwidth= 0.25, relheight= 0.13)
        self.campo_valor = Entry(self.f_widgets, textvariable=self.stringVarValor, state="readonly",  font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_valor.place(relx= 0.35, rely= 0.62, relwidth= 0.55, relheight= 0.13)

        self.label_hospede = Label(self.f_widgets, text="Hóspede", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_hospede.place(relx= 0.1, rely= 0.77, relwidth= 0.25, relheight= 0.13)
        self.campo_hospede = Entry(self.f_widgets, textvariable=self.stringVarHospede, state="readonly",  font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_hospede.place(relx= 0.35, rely= 0.77, relwidth= 0.55, relheight= 0.13)

        #definindo label de mensagem
        self.label_msg = Label(self.root2)
