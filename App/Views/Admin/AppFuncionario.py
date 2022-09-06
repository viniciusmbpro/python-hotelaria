from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font as tkFont
from tkcalendar import Calendar
import datetime
import math

#importando Controllers da aplicação
from ...Controllers.FuncionarioController import *
from .AppInitAdmin import *

class AppFuncionario:
    def __init__(self, abaFuncionario, Init):
        #definindo a tela de renderização
        self.tela_render = "AppInitAdmin"

        #recebendo o init dentro da classe para passar para a qualquer função
        self.Init = Init
        self.abaFuncionario = abaFuncionario

        #menu de funções
        self.frame_menu = Frame(self.abaFuncionario, bg="#00767d")
        self.frame_menu.place(relx= 0.2, rely= 0.02, relwidth= 0.6, relheight= 0.05)

        self.btn_adicionar = Label(self.frame_menu, text="0       Adicionar       0",  bg="#0e6900", fg="#ffffff", font=tkFont.Font(family="Lucida Grande", size=13), border=2)
        self.btn_adicionar.place(relx= 0, rely= 0, relwidth= 0.15, relheight= 1)
        self.btn_adicionar.bind("<Button-1>", self.formularioFuncionario)

        self.campo_busca = Entry(self.frame_menu, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_busca.place(relx= 0.15, rely= 0, relwidth= 0.65, relheight= 1)
        self.btn_busca = Button(self.frame_menu, text="BUSCAR", bg="#ffffff", fg= "#000000", command=lambda:[buscarFuncionarios()])
        self.btn_busca.place(relx= 0.8, rely= 0, relwidth= 0.2, relheight= 1)
        def buscarFuncionarios():
            FuncionarioController.buscarFuncionarios(self)
        FuncionarioController.buscarFuncionarios(self)

    def listarFuncionarios(self):
        #configuração da barra de rolagem
        self.f_base_scroll = Frame(self.abaFuncionario)
        self.f_base_scroll.place(relx= 0, rely= 0.09, relwidth= 1, relheight= 0.95)
        self.j_Funcionarios = Frame(self.f_base_scroll, bg="#00767d")
        self.canva_rol = Canvas(self.j_Funcionarios, bg="#00767d")
        self.canva_rol.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        self.yscrollbar = ttk.Scrollbar(self.j_Funcionarios, orient="vertical", command=self.canva_rol.yview)
        self.yscrollbar.place(relx= 0.98, rely= 0, relwidth= 0.02, relheight= 1)
        self.canva_rol.configure(yscrollcommand=self.yscrollbar.set)
        self.canva_rol.bind('<Configure>', lambda e: self.canva_rol.configure(scrollregion = self.canva_rol.bbox('all')))
        self.frame_rol = Frame(self.canva_rol, bg="#00767d")
        self.canva_rol.create_window((0,0), window=self.frame_rol, anchor="nw")
        self.j_Funcionarios.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        
        #for para criar frames dos Funcionarios
        indice = 0
        #definindo os quadros da grade
        quadros = 3
        pos_relx = []
        rel_width = 1/quadros-0.02
        for i in range(quadros):
            pos_relx.append((1/quadros)*i)

        #chamando editar funcionario
        def callDeletarFuncionario(event):
            if(messagebox.askquestion("Confirmar","Você tem certeza que quer deletar este usuário?")=="yes"):
                FuncionarioController.deletarFuncionario(event.widget["text"].split()[0],self.Init)
        
        self.img_funcionario = []

        for row in range(math.ceil(len(self.rFuncionarios)/quadros)):
            quadros = len(self.rFuncionarios)%quadros if row==math.ceil(len(self.rFuncionarios)/quadros)-1 and len(self.rFuncionarios)%quadros!=0 == 0 else quadros
            self.estrutura = Frame(self.j_Funcionarios, bg="#00767d")
            self.estrutura.pack(in_=self.frame_rol, side=TOP, ipadx=0.47*self.Init.monitor_w, ipady=220, padx=10, pady=20)

            for col in range(quadros):
                self.temp_frame = Frame(self.estrutura, bg="#ffffff")
                self.temp_frame.place(relx=pos_relx[col], rely=0, relwidth=rel_width, relheight=1)

                self.img_funcionario.append(PhotoImage(file=f"{self.Init.pasta_app}\\imagens\\{self.rFuncionarios[indice][9]}"))
                self.img_funcionario[indice] = self.img_funcionario[indice].subsample(3,3)
                self.label_img_funcionario = Label(self.temp_frame, image=self.img_funcionario[indice], bg="#002e4f", highlightbackground="#004170", highlightthickness= 2)
                self.label_img_funcionario.place(relx= 0.68, rely= 0.02, relwidth= 0.3, relheight= 0.3)

                labels = ["Nome", "Cpf", "Rg", "Email", "Senha", "Telefone", "Data de Nascimento", "Sexo", "Foto_perfil", "Endereço", "Dados Bancários", "Data de Criação", "Matrícula", "Cargo", "Nível de acesso", "Data de Admissão"]
                for i in range(len(labels)):
                    Label(self.temp_frame, text=f"{labels[i]}: {str(self.rFuncionarios[indice][i+1])}", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=11)).place(relx=0.07, y=380/len(labels)*i+10, height=30)
                
                btn_editar = Label(self.temp_frame, text=f"{self.rFuncionarios[indice][0]}  Editar  {self.rFuncionarios[indice][0]}",  bg="blue", fg= "#ffffff", font=tkFont.Font(family="Lucida Grande", size=13))
                btn_editar.place(x= 5, rely= 0.9, width= 60, height= 30)
                btn_editar.bind("<Button-1>", self.formularioFuncionario)

                btn_deletar = Label(self.temp_frame, text=f"{self.rFuncionarios[indice][0]}  Deletar  {self.rFuncionarios[indice][0]}",  bg="red", fg= "#ffffff", font=tkFont.Font(family="Lucida Grande", size=13))
                btn_deletar.place(x=70, rely= 0.9, width= 60, height= 30)
                btn_deletar.bind("<Button-1>", callDeletarFuncionario)

                indice+=1

    def formularioFuncionario(self, event):
        #puxando dados
        acao = event.widget["text"].split()[1]
        if acao=="Editar":
            self.idfuncionario = event.widget["text"].split()[0]
            self.dados_funcionario = FuncionarioController.getInfoFuncionario(self.idfuncionario)
            nome = self.dados_funcionario[0]
            rg = self.dados_funcionario[1]
            cpf = self.dados_funcionario[2]
            email = self.dados_funcionario[3]
            senha = self.dados_funcionario[4]
            telefone = self.dados_funcionario[5]
            data_nascimento = self.dados_funcionario[6]
            sexo = self.dados_funcionario[7]
            self.foto_perfil = self.dados_funcionario[8]
            endereco = self.dados_funcionario[9]
            dados_bancarios = self.dados_funcionario[10]
            data_criacao = self.dados_funcionario[11]
            matricula = self.dados_funcionario[12]
            cargo = self.dados_funcionario[13]
            nivel_acesso = self.dados_funcionario[14]
            data_admissao = self.dados_funcionario[15]
        else:
            nome = ''
            rg = ''
            cpf = ''
            email = ''
            senha = ''
            telefone = ''
            data_nascimento = ''
            sexo = ''
            self.foto_perfil = 'clique_aqui.png'
            endereco = ''
            dados_bancarios = ''
            data_criacao = ''
            matricula = ''
            cargo = ''
            nivel_acesso = ''
            data_admissao = ''

        #abrindo janela
        self.root2 = Toplevel()
        self.root2.title(acao)
        self.root2.configure(bg="#283d8f", highlightbackground="#283d8f", highlightthickness= 1, highlightcolor="#ffffff")
        w_root2 = 800
        self.root2.geometry(f"{w_root2}x550+{int(self.Init.monitor_w/2-w_root2/2)}+{100}")
        self.root2.resizable(False, False)
        self.root2.transient(self.Init.root)
        self.root2.focus_force()
        self.root2.grab_set()
        self.root2.iconbitmap(self.Init.pasta_app+"\\imagens\\logo2.ico")

        #definindo título
        self.label_titulo = Label(self.root2, text=f"{acao} Funcionário", font=tkFont.Font(family="Lucida Grande", size=15), bg="#283d8f", fg= "#ffffff")
        self.label_titulo.place(relx= 0, rely= 0, relwidth= 1, relheight= 0.1)

        #lados do form
        self.f_esquerda = Frame(self.root2, bd= 4, bg="#283d8f",  highlightbackground="#283d8f", highlightthickness= 1, highlightcolor="#ffffff")
        self.f_esquerda.place(relx= 0, rely= 0.1, relwidth= 0.5, relheight= 0.8)
        self.f_direita = Frame(self.root2, bd= 4, bg="#283d8f",  highlightbackground="#283d8f", highlightthickness= 1, highlightcolor="#ffffff")
        self.f_direita.place(relx= 0.5, rely= 0.1, relwidth= 0.5, relheight= 0.8)
        
        #carregando widgets
        self.widgetsForm()

        #inserindo dados atuais no formulário de edição
        self.campo_nome.insert(0, nome)
        self.campo_rg.insert(0, rg)
        self.campo_cpf.insert(0, cpf)
        self.campo_email.insert(0, email)
        self.campo_senha.insert(0, senha)
        self.campo_telefone.insert(0, telefone)
        self.campo_data_nascimento.insert(0, data_nascimento)
        c=0
        if sexo == "Feminino": c=1
        elif sexo == "Não declarar": c=2
        self.campo_sexo.current(c)
        self.campo_endereco.insert(0, endereco)
        self.campo_dados_bancarios.insert(0, dados_bancarios)
        self.campo_matricula.insert(0, matricula)
        self.campo_cargo.insert(0, cargo)
        nv=0
        if nivel_acesso == "Leitura": nv=1
        elif nivel_acesso == "Admin": nv=2
        self.campo_nivel_acesso.current(nv)
        self.campo_data_admissao.insert(0, data_admissao)

        def callFuncionarioController():
            if acao=="Editar":
                FuncionarioController.alterarFuncionario(self, self.Init)
            else:
                FuncionarioController.cadastrarFuncionario(self, self.Init)
        self.btn_salvar = Button(self.root2, text="SALVAR", bg="#ffffff", fg= "#000000", command=lambda:[callFuncionarioController()])
        self.btn_salvar.place(relx= 0.1, rely= 0.93, relwidth= 0.8, relheight= 0.07)
    
    def widgetsForm(self):

        self.label_nome = Label(self.f_esquerda, text="Nome", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_nome.place(relx= 0.1, rely= 0.02, relwidth= 0.2, relheight= 0.1)
        self.campo_nome = Entry(self.f_esquerda, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_nome.place(relx= 0.3, rely= 0.02, relwidth= 0.6, relheight= 0.1)

        self.label_rg = Label(self.f_esquerda, text="RG", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_rg.place(relx= 0.1, rely= 0.14, relwidth= 0.2, relheight= 0.1)
        self.campo_rg = Entry(self.f_esquerda, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_rg.place(relx= 0.3, rely= 0.14, relwidth= 0.6, relheight= 0.1)

        self.label_cpf = Label(self.f_esquerda, text="CPF", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_cpf.place(relx= 0.1, rely= 0.26, relwidth= 0.2, relheight= 0.1)
        self.campo_cpf = Entry(self.f_esquerda, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_cpf.place(relx= 0.3, rely= 0.26, relwidth= 0.6, relheight= 0.1)

        self.label_email = Label(self.f_esquerda, text="Email", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_email.place(relx= 0.1, rely= 0.38, relwidth= 0.2, relheight= 0.1)
        self.campo_email = Entry(self.f_esquerda, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_email.place(relx= 0.3, rely= 0.38, relwidth= 0.6, relheight= 0.1)

        self.label_telefone = Label(self.f_esquerda, text="telefone", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_telefone.place(relx= 0.1, rely= 0.5, relwidth= 0.2, relheight= 0.1)
        self.campo_telefone = Entry(self.f_esquerda, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_telefone.place(relx= 0.3, rely= 0.5, relwidth= 0.6, relheight= 0.1)

        def inserir_data():
            data = self.calendario.get_date()
            self.calendario.destroy()
            self.campo_data_nascimento.delete(0, END)
            self.campo_data_nascimento.insert(0, data)
        def calendario():
            self.calendario = Calendar(self.f_esquerda, bg="white", fg="black", locale="pt_br")
            self.calendario.place(relx=0.3, rely=0.2)
            self.btn_inserir_data = Button(self.calendario, text="inserir", bg="#ffffff", fg= "black", command=lambda:[inserir_data()])
            self.btn_inserir_data.place(relx= 0.5, rely= 0)
        self.label_data_nascimento = Label(self.f_esquerda, text="data_nascimento", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_data_nascimento.place(relx= 0.1, rely= 0.62, relwidth= 0.4, relheight= 0.1)
        self.campo_data_nascimento = Entry(self.f_esquerda, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_data_nascimento.place(relx= 0.5, rely= 0.62, relwidth= 0.3, relheight= 0.1)
        self.btn_calendario = Button(self.f_esquerda, text="+", bg="#ffffff", fg= "#000000", command=lambda:[calendario()], font=("Arial", 25))
        self.btn_calendario.place(relx= 0.8, rely= 0.62, relwidth= 0.1, relheight= 0.1)

        self.label_senha = Label(self.f_esquerda, text="Senha", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_senha.place(relx= 0.1, rely= 0.74, relwidth= 0.2, relheight= 0.1)
        self.campo_senha = Entry(self.f_esquerda, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_senha.place(relx= 0.3, rely= 0.74, relwidth= 0.6, relheight= 0.1)

        self.label_sexo = Label(self.f_esquerda, text="sexo", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_sexo.place(relx= 0.1, rely= 0.86, relwidth= 0.2, relheight= 0.1)
        self.campo_sexo = ttk.Combobox(self.f_esquerda, values=["Masculino", "Feminino", "Não declarar"], state="readonly", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_sexo.place(relx= 0.3, rely= 0.86, relwidth= 0.6, relheight= 0.1)

        def select_file(event):
            filetypes = ( ('image files', '*.jpg, .png .gif'), ('All files', '*.*') )
            filename = fd.askopenfilename( title='Open a file', initialdir='/', filetypes=filetypes )
            loadPreView(filename)
        def loadPreView(imgPath):
            self.imgPathFotoPerfil = imgPath
            img = Image.open(imgPath)
            img = img.resize((round(400), round((img.size[1]/img.size[0])*400)), Image.ANTIALIAS)
            os.remove(self.Init.pasta_app+"\\imagens\\img_temp.png") 
            img.save(self.Init.pasta_app+"\\imagens\\img_temp.png", format('png'))
            _image = PhotoImage(file=self.Init.pasta_app+"\\imagens\\img_temp.png")
            _image = _image.subsample(2,2)
            self.campo_preView.configure(image=_image)
        self.label_foto_perfil = Label(self.f_direita, text="Foto Perfil", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_foto_perfil.place(relx= 0.1, rely= 0.02, relwidth= 0.8, relheight= 0.1)
        self.campo_preView = Label(self.f_direita, bg="white")
        self.campo_preView.place(relx= 0.1, rely= 0.12, relwidth= 0.8, relheight= 0.1)
        self.campo_preView.bind("<Button-1>", select_file)
        loadPreView(f"{self.Init.pasta_app}\\imagens\\{self.foto_perfil}")

        self.label_endereco = Label(self.f_direita, text="Endereço", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_endereco.place(relx= 0.1, rely= 0.24, relwidth= 0.2, relheight= 0.1)
        self.campo_endereco = Entry(self.f_direita, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_endereco.place(relx= 0.3, rely= 0.24, relwidth= 0.6, relheight= 0.1)

        self.label_dados_bancarios = Label(self.f_direita, text="Dados Bancários", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_dados_bancarios.place(relx= 0.1, rely= 0.36, relwidth= 0.4, relheight= 0.1)
        self.campo_dados_bancarios = Entry(self.f_direita, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_dados_bancarios.place(relx= 0.5, rely= 0.36, relwidth= 0.4, relheight= 0.1)

        self.label_matricula = Label(self.f_direita, text="Matrícula", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_matricula.place(relx= 0.1, rely= 0.5, relwidth= 0.2, relheight= 0.1)
        self.campo_matricula = Entry(self.f_direita, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_matricula.place(relx= 0.3, rely= 0.5, relwidth= 0.6, relheight= 0.1)

        self.label_cargo = Label(self.f_direita, text="Cargo", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_cargo.place(relx= 0.1, rely= 0.62, relwidth= 0.2, relheight= 0.1)
        self.campo_cargo = Entry(self.f_direita, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_cargo.place(relx= 0.3, rely= 0.62, relwidth= 0.6, relheight= 0.1)

        self.label_nivel_acesso = Label(self.f_direita, text="Nível de acesso", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_nivel_acesso.place(relx= 0.1, rely= 0.74, relwidth= 0.4, relheight= 0.1)
        self.campo_nivel_acesso = ttk.Combobox(self.f_direita, values=["Leitura", "Editor", "Admin"], state="readonly", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_nivel_acesso.place(relx= 0.5, rely= 0.74, relwidth= 0.4, relheight= 0.1)

        def inserir_data_admissao():
            data = self.calendario.get_date()
            self.calendario.destroy()
            self.campo_data_admissao.delete(0, END)
            self.campo_data_admissao.insert(0, data)
        def calendario_admissao():
            self.calendario = Calendar(self.f_direita, bg="white", fg="black", locale="pt_br")
            self.calendario.place(relx=0.3, rely=0.4)
            self.btn_inserir_data_admissao = Button(self.calendario, text="inserir", bg="#ffffff", fg= "black", command=lambda:[inserir_data_admissao()])
            self.btn_inserir_data_admissao.place(relx= 0.5, rely= 0)
        self.label_data_admissao = Label(self.f_direita, text="Data de admissão", bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.label_data_admissao.place(relx= 0.1, rely= 0.86, relwidth= 0.4, relheight= 0.1)
        self.campo_data_admissao = Entry(self.f_direita, bg="#ffffff", fg= "#000000", font=tkFont.Font(family="Lucida Grande", size=13))
        self.campo_data_admissao.place(relx= 0.5, rely= 0.86, relwidth= 0.3, relheight= 0.1)
        self.btn_calendario = Button(self.f_direita, text="+", bg="#ffffff", fg= "#000000", command=lambda:[calendario_admissao()], font=("Arial", 25))
        self.btn_calendario.place(relx= 0.8, rely= 0.86, relwidth= 0.1, relheight= 0.1)

        #definindo label de mensagem
        self.label_msg = Label(self.root2)
