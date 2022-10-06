#importando dependências da aplicação
from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import font as tkFont
# import awesometkinter as atk
import os
from PIL import Image

#importando Controllers da aplicação
from ..Controllers import *

#definindo janela padrão
root = tix.Tk()

# esta é a branch de desenvolvimento para linux

#definindo constantes
PASTA_APP = os.path.dirname(__file__)
MONITOR_H = root.winfo_screenheight()
MONITOR_W = root.winfo_screenwidth()
#definindo o tamanho da imagem
img = Image.open(PASTA_APP+"\\imagens\\bg_login_3.gif")
img = img.resize((round(MONITOR_W), round(MONITOR_H)), Image.ANTIALIAS)
img.save(PASTA_APP+"\\imagens\\bg_login_3.gif", format('gif'))
#definindo imagem de fundo
imgFundo = PhotoImage(file= PASTA_APP+"\\imagens\\bg_login_3.gif")

class AppInit():
    def __init__(self, control):
        self.control = control
        self.root = root
        self.config_janela()
        self.config_estilos()

    def config_janela(self):
        self.root.title("Hotelaria")
        self.root.configure(bg= "white")
        self.w_tela = 1000
        self.monitor_w = MONITOR_W
        self.pasta_app = PASTA_APP
        # self.root.geometry(f"{1000}x{600}+{int(MONITOR_W/2-1000/2)}+{20}")
        self.root.attributes('-fullscreen', True)
        self.root.resizable(False, False)
        # self.root.maxsize(width= 700, height= 500)
        # self.root.minsize(width= 700, height= 500)
        # root.attributes('-alpha',0.5)
        #menu simples
        menubar = Menu(self.root)
        menubar.add_command(label="SAIR", command=self.root.quit)
        menubar.configure(font= tkFont.Font(family="Lucida Grande", size=15))
        self.root.config(menu=menubar)

    def config_estilos(self):
        #atribuindo logo e fundo
        self.imgfundo = imgFundo
        self.root.iconbitmap(PASTA_APP+"\\imagens\\logo2.ico") 
        self.label_imgfundo = Label(self.root, text="Clique no botão para exibir os hóspedes", image= imgFundo).place(relx= 0, rely= 0, relwidth= 1, relheight= 1)

        #estilização de notebooks
        self.cor_pd = "#ffffff"
        self.cor_sld = "#00767d"
        self.style_notebook = ttk.Style()
        self.style_notebook.theme_create( "hotel", parent="alt", settings={
                "TNotebook": {"configure": {"tabmargins": [220, 5, 2, 0] } },
                "TNotebook.Tab": {
                    "configure": {"padding": [5, 1], "background": self.cor_pd, "foreground": "#00767d", "font":('Lucida Grande','13','bold')},
                    "map":       {"background": [("selected", self.cor_sld)], "foreground": [("selected", "#ffffff")],
                                "expand": [("selected", [0, 5, 0, 0])] } } } )
        self.style_notebook.theme_use("hotel")

        #estilização da scrollbar
        self.style_scrollbar = ttk.Style()
        self.style_scrollbar.theme_use('hotel')
        self.style_scrollbar.configure("Vertical.TScrollbar", background="#00767d", troughcolor="white", bordercolor="#00767d", arrowcolor="white")
    
    def loop(self):
        self.root.mainloop()
