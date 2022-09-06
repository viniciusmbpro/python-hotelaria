from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import font as tkFont
from PIL import Image, ImageTk

#importando Views do do hospede
from .AppHome import *
from .AppMinhasReservas import *

class AppInitHospede:
    def __init__(self, Init):
        self.Init = Init

        #criando o frame
        self.framePrincipal = Frame(self.Init.root, bd= 4, bg="#002e4f",highlightbackground="#ffffff", highlightthickness= 1)
        self.framePrincipal.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        
        #menu logado
        self.menu_logado = Frame(self.framePrincipal, bd= 4, bg="#004170")
        self.menu_logado.place(relx= 0.64, rely= 0.025, relwidth= 0.3, relheight= 0.05)
        self.label_nome_logado = Label(self.menu_logado, text=(Init.session['nome'][0]), font=tkFont.Font(family="Lucida Grande", size=14), bg="#004170", fg= "white")
        self.label_nome_logado.place(relx= 0, rely= 0, relwidth= 0.4, relheight= 1)
        self.btn_sair = Button(self.menu_logado, text="SAIR", 
                                font= tkFont.Font(size=10), bg="red", 
                                fg= "#ffffff", command=lambda:[Init.control.sair()])
        self.btn_sair.place(relx= 0.8, rely= 0, relwidth= 0.2, relheight= 1)
        self.btn_configuracoes = Button(self.menu_logado, text="CONFIGURAÇÕES", 
                                font= tkFont.Font(size=10), bg="#00767d", 
                                fg= "#ffffff", command=lambda:[Init.control.renderTela('AppConfig')])
        self.btn_configuracoes.place(relx= 0.4, rely= 0, relwidth= 0.4, relheight= 1)

        #imagem do perfil
        self.img_foto_perfil = PhotoImage(file=f"{self.Init.pasta_app}\\imagens\\{Init.session['foto_perfil']}")
        self.img_foto_perfil = self.img_foto_perfil.subsample(6,6)
        self.label_foto_perfil = Label(self.framePrincipal, image=self.img_foto_perfil, bd=2, bg="#002e4f", highlightbackground="#004170", highlightthickness= 5)
        self.label_foto_perfil.place(relx= 0.6, rely= 0.005, relwidth= 0.06, relheight= 0.09)

        #definindo título
        self.label_titulo = Label(self.framePrincipal, text="Bem vindo ao Hotel Beija-Flor", font=tkFont.Font(family="Lucida Grande", size=20), bg="#002e4f", fg= "#ffffff")
        self.label_titulo.place(relx= 0, rely= 0, relwidth= 0.4, relheight= 0.1)

        #abas para os quartos
        self.abas = ttk.Notebook(self.framePrincipal)
        self.abaHome = Frame(self.abas)
        self.abaMinhasReservas = Frame(self.abas)
        self.abaRelaxe = Frame(self.abas)

        self.abaHome.configure(bg="#00767d")
        self.abaMinhasReservas.configure(bg="#00767d")
        self.abaRelaxe.configure(bg="#00767d")

        self.abas.add(self.abaHome, text="Reservar Acomodação")
        self.abas.add(self.abaMinhasReservas, text="Minhas Reservas")
        self.abas.add(self.abaRelaxe, text="Relaxe ;)")

        self.abas.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)
        self.abas.select(self.abaMinhasReservas)

        #chamando as views
        AppHome(self.abaHome, Init)
        AppMinhasReservas(self.abaMinhasReservas, Init)
        self.telaAbaRelaxe()
    
    def telaAbaRelaxe(self):
        def paint( event ): 
            x1, y1, x2, y2 = ( event.x - 10 ), ( event.y - 10 ), ( event.x + 10 ), ( event.y + 10 )
            C.create_oval(x1, y1, x2, y2, fill = 'black')

        C = Canvas(self.abaRelaxe)
        img = Image.open(self.Init.pasta_app+"\\imagens\\bg_login_3.gif")
        img = img.resize((round(1366), round(700)), Image.ANTIALIAS)
        img.save(self.Init.pasta_app+"\\imagens\\bg_login_3.gif", format('gif'))
        _image = ImageTk.PhotoImage(file=self.Init.pasta_app+"\\imagens\\bg_login_3.gif")
        C.create_image((0,0), image = _image, anchor=NW)
        C.bind( "<B1-Motion>", paint )
        C.place(relwidth=1, relheight=1)
        C.image = _image