from io import BytesIO
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import PytonBeautifulSoup.Data as Data
import requests

# VARIABLES
root = Tk()
root.title = "Recomendaciones Personalizadas"
root.geometry("1080x720")

txt_url = Data.get_url()
txt_Titulo = Data.get_TitlePage(txt_url)

# Create A Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)
# Create A Canvas
My_Canvas = Canvas(main_frame)
My_Canvas.pack(side=LEFT,fill=BOTH, expand=1)

# Add A ScrollBar To the Canvas
My_Scollbar = ttk.Scrollbar(main_frame, orient=VERTICAL,command=My_Canvas.yview)
My_Scollbar.pack(side=RIGHT, fill=Y)
    
# Configure The Canvas
My_Canvas.configure(yscrollcommand=My_Scollbar.set)
My_Canvas.bind("<Configure>",lambda e:My_Canvas.configure(scrollregion= My_Canvas.bbox("all")))

# Create Another Freme Inside The Canvas
Second_frame = Frame(My_Canvas)

# Add that New Freame to a Window In The Canvas
My_Canvas.create_window((0,0),window=Second_frame, anchor="nw")

# ************************************ Titulo ************************************************

Titulo = tk.Label(Second_frame, text=txt_Titulo, font=("Arial", 32))
Titulo.pack(pady=20)

# ************************************ Imagen y Nombre del Anime ************************************************

Txt_AnimeImagen = Data.get_AnimeImage(txt_url)
Txt_AnimeTitulo = Data.get_AnimeTitle(txt_url)

for imagen in Txt_AnimeImagen:

    for DivsTitulos in Txt_AnimeTitulo:

        # ********************** Imagen **********************
        UrlImagen = Data.get_url()
        UrlImagen = UrlImagen + imagen
        lblImagen = tk.Label(Second_frame, text=UrlImagen, font=("Arial", 8))
        lblImagen.pack(pady=20)
        # ********************** Nombre Del Anime **********************
        LblTexto = tk.Label(Second_frame, text=DivsTitulos, font=("Arial", 8))
        LblTexto.pack(pady=20)


root.mainloop()

