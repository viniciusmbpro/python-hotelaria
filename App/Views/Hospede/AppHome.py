from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import font as tkFont
from PIL import Image, ImageTk
from tkcalendar import Calendar
import math
import datetime

#importando Controllers da aplicação
from ...Controllers.HospedeController import *
from ...Controllers.AcomodacaoController import *
from ...Controllers.CategoriaController import *
from ...Controllers.ProdutoController import *
from ...Controllers.ReservaController import *

class AppHome:
    def __init__(self, abaHome, Init):
        #definindo variáveis padrão
        self.tela_render = "AppInitHospede"
        self.Init = Init
        self.abaHome = abaHome

        #menu de funções
        self.frame_menu = Frame(self.abaHome, bg="#00767d")
        self.frame_menu.place(relx= 0.1, rely= 0.02, relwidth= 0.8, relheight= 0.05)
        
        #botões dos calendários
        self.img_btn_in = PhotoImage(file=self.Init.pasta_app+"/imagens/calendar_btn_azul.png")
        self.img_btn_in = self.img_btn_in.subsample(9,9)
        self.img_btn_out = PhotoImage(file=self.Init.pasta_app+"/imagens/calendar_btn_laranja.png")
        self.img_btn_out = self.img_btn_out.subsample(9,9)

        #função para garantir que a data de início seja menor do que a data de saída
        def garantirLogicaDatas(acao):
            hoje = datetime.date.today().strftime("%d/%m/%Y")
            v_hoje = hoje.split('/')
            v_hoje = datetime.datetime(int(v_hoje[2]), int(v_hoje[1]), int(v_hoje[0]))

            if self.campo_entrada_prevista.get()!='':
                dt_inicio = self.campo_entrada_prevista.get().split('/')
            else:
                dt_inicio = hoje.split('/')
            if self.campo_saida_prevista.get()!='':
                dt_fim = self.campo_saida_prevista.get().split('/')
            else:
                dt_fim = hoje.split('/')
            date_strt, date_end = datetime.datetime(int(dt_inicio[2]), int(dt_inicio[1]), int(dt_inicio[0])), datetime.datetime(int(dt_fim[2]), int(dt_fim[1]), int(dt_fim[0]))
            if acao=='in':
                if date_strt<v_hoje:
                    date_strt = v_hoje
                    self.stringVarEntradaPrevista.set(hoje)
                if date_strt>date_end:
                    data = f"{dt_inicio[0]}/{dt_inicio[1]}/{dt_inicio[2]}"
                    self.stringVarSaidaPrevista.set(data)
            elif acao=='out':
                if date_end<v_hoje:
                    date_end = v_hoje
                    self.stringVarSaidaPrevista.set(hoje)
                if date_strt>date_end:
                    data = f"{dt_fim[0]}/{dt_fim[1]}/{dt_fim[2]}"
                    self.stringVarEntradaPrevista.set(data)

        self.stringVarEntradaPrevista = StringVar()
        def inserir_entrada_prevista():
            data = self.calendario.get_date()
            self.calendario.destroy()
            self.stringVarEntradaPrevista.set(data)
            garantirLogicaDatas('in')
        def calendario_entrada_prevista():
            self.calendario = Calendar(self.abaHome, locale="pt_br")
            self.calendario.place(relx=0.2, rely=0.08)
            self.calendario.grab_set()
            self.btn_inserir_entrada_prevista = Button(self.calendario, text="inserir", bg="#ffffff", fg= "black", command=lambda:[inserir_entrada_prevista()])
            self.btn_inserir_entrada_prevista.place(relx= 0.5, rely= 0)
        self.label_entrada_prevista = Label(self.frame_menu, text="Entrada Prevista", bg="#034c5e", fg= "white", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_entrada_prevista.place(relx= 0, rely= 0, relwidth= 0.12, relheight= 1)
        self.campo_entrada_prevista = Entry(self.frame_menu, font=tkFont.Font(family="Lucida Grande", size=13), state="readonly", textvariable=self.stringVarEntradaPrevista)
        self.campo_entrada_prevista.place(relx= 0.12, rely= 0, relwidth= 0.08, relheight= 1)
        self.btn_calendario1 = Button(self.frame_menu, image=self.img_btn_in, bd=0, command=lambda:[calendario_entrada_prevista()])
        self.btn_calendario1.place(relx= 0.2, rely= 0, relwidth= 0.03, relheight= 1)

        self.stringVarSaidaPrevista = StringVar()
        def inserir_saida_prevista():
            data = self.calendario.get_date()
            self.calendario.destroy()
            self.stringVarSaidaPrevista.set(data)
            garantirLogicaDatas('out')
        def calendario_saida_prevista():
            self.calendario = Calendar(self.abaHome, locale="pt_br")
            self.calendario.place(relx=0.3, rely=0.08)
            self.calendario.grab_set()
            self.btn_inserir_saida_prevista = Button(self.calendario, text="inserir", bg="#ffffff", fg= "black", command=lambda:[inserir_saida_prevista()])
            self.btn_inserir_saida_prevista.place(relx= 0.5, rely= 0)
        self.label_saida_prevista = Label(self.frame_menu, text="Saída Prevista", bg="#a64800", fg= "white", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_saida_prevista.place(relx= 0.23, rely= 0, relwidth= 0.12, relheight= 1)
        self.campo_saida_prevista = Entry(self.frame_menu, font=tkFont.Font(family="Lucida Grande", size=13), state="readonly", textvariable=self.stringVarSaidaPrevista)
        self.campo_saida_prevista.place(relx= 0.35, rely= 0, relwidth= 0.08, relheight= 1)
        self.btn_calendario = Button(self.frame_menu, image=self.img_btn_out, bd=0,command=lambda:[calendario_saida_prevista()], font=("Arial", 25))
        self.btn_calendario.place(relx= 0.43, rely= 0, relwidth= 0.03, relheight= 1)

        self.campo_busca = Entry(self.frame_menu, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_busca.place(relx= 0.46, rely= 0, relwidth= 0.44, relheight= 1)
        self.btn_busca = Button(self.frame_menu, text="BUSCAR", bg="#ffffff", fg= "#000000", command=lambda:[buscarAcomodacoes()])
        self.btn_busca.place(relx= 0.9, rely= 0, relwidth= 0.1, relheight= 1)
        def buscarAcomodacoes():
            AcomodacaoController.buscarAcomodacoes(self)
        Label(self.abaHome, text="Defina as datas de entrada e saída para ver as acomodações", bg="#197539", fg="white", font=tkFont.Font(family="Lucida Grande", size=20)).place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.1)

    def listarAcomodacoes(self):
        self.filtrarAcomodacaoes()

        #configuração da barra de rolagem
        self.f_base_scroll = Frame(self.abaHome)
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
        
        #for para criar frames dos acomodacoes
        indice = 0
        #definindo os quadros da grade
        quadros = 1
        pos_relx = []
        rel_width = 1/quadros-0.02
        for i in range(quadros):
            pos_relx.append((1/quadros)*i)

        #pegando imagem padrão
        img = Image.open(self.Init.pasta_app+"/imagens/bg_quarto_1.png")
        img = img.resize((round(350), round(240)), Image.ANTIALIAS)
        img.save(self.Init.pasta_app+"/imagens/bg_quarto_1.png", format('png'))
        _image = ImageTk.PhotoImage(file=self.Init.pasta_app+"/imagens/bg_quarto_1.png")

        #definindo efeito da imagem
        def efeitoImagem(event):
            event.widget.place(relx=0.72, rely=0.04, relwidth=0.28, relheight=0.58)
        def reverteEfeitoImagem(event):
            event.widget.place(relx=0.73, rely=0.05, relwidth=0.26, relheight=0.5)

        if len(self.rAcomodacoes)==0:
            Label(self.abaHome, text="Não há acomodações disponíveis", bg="#6e1916", fg="white", font=tkFont.Font(family="Lucida Grande", size=20)).place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.1)

        for row in range(math.ceil(len(self.rAcomodacoes)/quadros)):
            quadros = len(self.rAcomodacoes)%quadros if row==math.ceil(len(self.rAcomodacoes)/quadros)-1 and len(self.rAcomodacoes)%quadros!=0 == 0 else quadros
            self.estrutura = Frame(self.j_acomodacoes, bg="#00767d")
            self.estrutura.pack(in_=self.frame_rol, side=TOP, ipadx=0.47*self.Init.monitor_w, ipady=120, padx=10, pady=20)

            for col in range(quadros):
                self.temp_frame = Frame(self.estrutura, bg="#002e4f")
                self.temp_frame.place(relx=pos_relx[col], rely=0, relwidth=rel_width, relheight=1)

                Label(self.temp_frame, text=f"{str(self.rAcomodacoes[indice][1])}", bg="#004170", fg= "white", anchor="e", bd=50, font=tkFont.Font(family="Lucida Grande", size=20)).place(relx= 0, rely= 0.05, relwidth=0.4, relheight= 0.2)

                Label(self.temp_frame, text=f"Andar: {str(self.rAcomodacoes[indice][2])}", bg="#004170", fg= "white", anchor="w", bd=50, font=tkFont.Font(family="Lucida Grande", size=14)).place(relx= 0.05, rely= 0.3, relwidth=0.35, relheight= 0.15)

                Label(self.temp_frame, text=f"Máximo de Pessoas: {str(self.rAcomodacoes[indice][3])}", bg="#004170", fg= "white", anchor="w", bd=50, font=tkFont.Font(family="Lucida Grande", size=14)).place(relx= 0.05, rely= 0.45, relwidth=0.35, relheight= 0.15)

                Label(self.temp_frame, text=f"Categoria: {str(self.rAcomodacoes[indice][6])}", bg="#004170", fg= "white", anchor="w", bd=50, font=tkFont.Font(family="Lucida Grande", size=14)).place(relx= 0.05, rely= 0.6, relwidth=0.35, relheight= 0.15)

                Label(self.temp_frame, text=f"Observações: {str(self.rAcomodacoes[indice][4])}", bg="#004170", fg= "white", anchor="w", bd=50, font=tkFont.Font(family="Lucida Grande", size=13)).place(relx= 0.05, rely= 0.75, relwidth=0.35, relheight= 0.15)

                #frame do frigobar
                self.f_frigobar = Frame(self.temp_frame, bg="#004170")
                self.f_frigobar.place(relx= 0.42, rely= 0.05, relwidth=0.3, relheight= 0.9)

                Label(self.f_frigobar, text="Itens do Frigobar:", bg="#004170", fg= "white", anchor="w", bd=50, font=tkFont.Font(family="Lucida Grande", size=15)).place(relx= 0, rely= 0, relwidth=1, relheight= 0.15)

                style = ttk.Style()
                style.configure("Treeview.Heading", font=(None, 13))
                style.configure("Treeview", font=(None, 12))

                tree = ttk.Treeview(self.f_frigobar, columns=('descricao', 'preco'), show='headings')
                tree.heading('#1', text='Descrição')
                tree.heading('#2', text='Preço')
                rCategoria = CategoriaController.getCategoriaPorDescricao(self.rAcomodacoes[indice][6])
                array = rCategoria[3].split()
                for idproduto in array:
                    values = list(ProdutoController.getInfoProduto(idproduto))
                    del(values[0])
                    del(values[2])
                    tree.insert('', END, values=values)
                tree.place(relx=0, rely=0.15, relwidth=1, relheight=0.85)
                tree.column("#1", width=130)
                tree.column("#2", width=130)
                scrollbar = ttk.Scrollbar(self.f_frigobar, orient=VERTICAL, command=tree.yview)
                tree.configure(yscroll=scrollbar.set)
                scrollbar.place(relx=0.94, rely=0.15, relwidth=0.06, relheight=0.85)

                C = Canvas(self.temp_frame)
                C.create_image((0,-70), image = _image, anchor=NW)
                C.place(relx=0.73, rely=0.05, relwidth=0.26, relheight=0.5)
                C.image = _image
                C.bind("<Enter>", efeitoImagem)
                C.bind("<Leave>", reverteEfeitoImagem)

                Label(self.temp_frame, text=f"Valor da diária: {rCategoria[2]}", bg="#257048", fg= "white", anchor="w", bd=10, font=tkFont.Font(family="Lucida Grande", size=15)).place(relx= 0.75, rely= 0.6, relwidth=0.2, relheight= 0.15)
                
                btn_reservar = Button(self.temp_frame, text=f"{self.rAcomodacoes[indice][0]}                           Reservar agora                           {self.rAcomodacoes[indice][0]}",  bg="#257025", fg= "#ffffff", font=tkFont.Font(family="Lucida Grande", size=12), command=lambda:[self.formularioReserva])
                btn_reservar.place(relx= 0.75, rely= 0.8, relwidth= 0.2, relheight= 0.15)
                btn_reservar.bind("<Button-1>", self.formularioReserva)

                indice+=1

    def formularioReserva(self, event):
        #puxando dados
        self.idacomodacao = event.widget["text"].split()[0]
        self.idhospede = self.Init.session['idusuario']
        self.dados_acomodacao = AcomodacaoController.getInfoAcomodacao(self.idacomodacao)
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
        self.stringVarAcomodacao = StringVar()
        self.stringVarValor = StringVar()
        self.stringVarHospede = StringVar()

        #carregando widgets
        self.widgetsForm()

        #inserindo dados atuais no formulário de edição
        self.campo_qtd_hospedes.current(0)
        self.campo_antecipacao.insert(0, 0)
        # self.campo_entrada_prevista.insert(0, 'entrada_prevista')
        # self.campo_saida_prevista.insert(0, 'saida_prevista')
        self.stringVarAcomodacao.set(descricao)
        self.stringVarValor.set(valor)
        self.stringVarHospede.set(HospedeController.getInfoHospede(self.idhospede)[0])

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

        self.label_entrada_prevista = Label(self.f_widgets, text="Entrada Prevista", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_entrada_prevista.place(relx= 0.1, rely= 0.32, relwidth= 0.4, relheight= 0.13)
        self.campo_entrada_prevista = Entry(self.f_widgets, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13), state="readonly", textvariable=self.stringVarEntradaPrevista)
        self.campo_entrada_prevista.place(relx= 0.5, rely= 0.32, relwidth= 0.3, relheight= 0.13)

        self.label_saida_prevista = Label(self.f_widgets, text="Saída Prevista", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_saida_prevista.place(relx= 0.1, rely= 0.47, relwidth= 0.4, relheight= 0.13)
        self.campo_saida_prevista = Entry(self.f_widgets, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13), state="readonly", textvariable=self.stringVarSaidaPrevista)
        self.campo_saida_prevista.place(relx= 0.5, rely= 0.47, relwidth= 0.3, relheight= 0.13)

        self.campo_acomodacao = Entry(self.f_widgets, textvariable=self.stringVarAcomodacao)

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

    def filtrarAcomodacaoes(self):
        #removendo acomodacões indisponíveis
        def verificarDatas(fk_idacomodacao):
            #lista escolhida
            test_list = []
            for dados in ReservaController.getAllToAcomodacao(fk_idacomodacao):
                if dados[2]!="Cancelada":
                    vetor_aux = dados[0].split('/')
                    test_list.append(datetime.datetime(int(vetor_aux[2]), int(vetor_aux[1]), int(vetor_aux[0])))
                    vetor_aux = dados[1].split('/')
                    test_list.append(datetime.datetime(int(vetor_aux[2]), int(vetor_aux[1]), int(vetor_aux[0])))

            dt_inicio = self.campo_entrada_prevista.get().split('/')
            dt_fim = self.campo_saida_prevista.get().split('/')
            #lista fixa
            date_strt, date_end = datetime.datetime(int(dt_inicio[2]), int(dt_inicio[1]), int(dt_inicio[0])), datetime.datetime(int(dt_fim[2]), int(dt_fim[1]), int(dt_fim[0]))
            
            res = False
            for ele in test_list:
                if ele >= date_strt and ele <= date_end:
                    return True

        acomodacoes_indisponiveis = []
        for i in range(len(self.rAcomodacoes)):
            if(self.rAcomodacoes[i][5]=="Em manutenção" or verificarDatas(self.rAcomodacoes[i][0])):
                acomodacoes_indisponiveis.append(self.rAcomodacoes[i])
        for i in range(len(acomodacoes_indisponiveis)):
            self.rAcomodacoes.remove(acomodacoes_indisponiveis[i])