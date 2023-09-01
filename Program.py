from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import Data

# ************************************* VARIABLES ************************************************
txt_url = Data.get_url()
txt_Titulo = Data.get_TitlePage(txt_url)
Txt_AnimeTitulo = Data.get_AnimeTitle(txt_url)
# ************************************ Create App ************************************************
root = Tk()
root.title("Anime FLV")
root.geometry("1080x720")
root.iconbitmap(
    "C:\\Users\\tiago\\Desktop\\Proyectos\\PYTHON\\Prog3\\PytonBeautifulSoup\\Icono.ico"
)
image = (
    "C:\\Users\\tiago\\Desktop\\Proyectos\\PYTHON\\Prog3\\PytonBeautifulSoup\\Fondo.png"
)
# Create A Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)
# Create A Canvas
My_Canvas = Canvas(main_frame)
My_Canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add A ScrollBar To the Canvas
My_Scollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=My_Canvas.yview)
My_Scollbar.pack(side=RIGHT, fill=Y)

# Configure The Canvas
My_Canvas.configure(yscrollcommand=My_Scollbar.set)
My_Canvas.bind(
    "<Configure>", lambda e: My_Canvas.configure(scrollregion=My_Canvas.bbox("all"))
)
# Create Another Freme Inside The Canvas
Second_frame = Frame(My_Canvas)
# Add that New Freame to a Window In The Canvas
My_Canvas.create_window((0, 0), window=Second_frame, anchor="nw")

# ************************************ Funciones ************************************************
loading_label = ""
TextosFiltrado = []
image_labels = []
textos_labels = []
Titulos = []


def mostrar_alerta_cargando():
    loading_label = tk.Label(
        Second_frame, text="Cargando...", font=("Arial", 12, "bold")
    )
    loading_label.pack(pady=20)
    Second_frame.update()
    return loading_label


def eliminar_resultados_anteriores():
    for label in image_labels:
        label.destroy()
    for label in textos_labels:
        label.destroy()
    for label in Titulos:
        label.destroy()
    image_labels.clear()
    textos_labels.clear()


def BuscarAnimeTop20():
    Txt_AnimeImagen = Data.get_AnimeImage(txt_url, 20)
    eliminar_resultados_anteriores()
    loading_label = mostrar_alerta_cargando()
    count = 0
    for Textos in Txt_AnimeTitulo:
        count = count + 1
        if count > 2:
            TextosFiltrado.append(Textos)

    Titulo = tk.Label(Second_frame, text=txt_Titulo, font=("Arial", 32))
    Titulo.pack(pady=20)
    Titulos.append(Titulo)

    for DivsTitulos, imagen in zip(TextosFiltrado, Txt_AnimeImagen):
        print(DivsTitulos, imagen)
        # Descargar la imagen desde la URL
        LblTexto = tk.Label(Second_frame, text=DivsTitulos, font=("Arial", 8))
        LblTexto.pack(pady=20)
        response = requests.get(imagen)
        if response.status_code == 200:
            image_data = BytesIO(response.content)
            image = Image.open(image_data)
            # Convertir la imagen a un formato que Tkinter pueda manejar
            tk_image = ImageTk.PhotoImage(image)
            # Crear Label de imagen y mostrarla

            image_label = tk.Label(Second_frame, image=tk_image)
            image_label.image = (
                tk_image  # Importante para evitar que la imagen se borre
            )
            image_label.pack(pady=20)
            image_labels.append(image_label)
            textos_labels.append(LblTexto)

    loading_label.destroy()
    Second_frame.update()


def BuscarAnimeTop5():
    Txt_AnimeImagen = Data.get_AnimeImage(txt_url, 5)
    eliminar_resultados_anteriores()
    loading_label = mostrar_alerta_cargando()
    count = 0
    for Textos in Txt_AnimeTitulo:
        count = count + 1
        if count > 2:
            TextosFiltrado.append(Textos)

    Titulo = tk.Label(Second_frame, text=txt_Titulo, font=("Arial", 32))
    Titulo.pack(pady=20)
    Titulos.append(Titulo)
    for DivsTitulos, imagen in zip(TextosFiltrado, Txt_AnimeImagen):
        print(DivsTitulos, imagen)
        # Descargar la imagen desde la URL
        LblTexto = tk.Label(Second_frame, text=DivsTitulos, font=("Arial", 8))
        LblTexto.pack(pady=20)
        response = requests.get(imagen)
        if response.status_code == 200:
            image_data = BytesIO(response.content)
            image = Image.open(image_data)
            # Convertir la imagen a un formato que Tkinter pueda manejar
            tk_image = ImageTk.PhotoImage(image)
            # Crear Label de imagen y mostrarla

            image_label = tk.Label(Second_frame, image=tk_image)
            image_label.image = (
                tk_image  # Importante para evitar que la imagen se borre
            )
            image_label.pack(pady=20)
            image_labels.append(image_label)
            textos_labels.append(LblTexto)

    loading_label.destroy()
    Second_frame.update()


# ************************************ Botones ************************************************

lblBoton = "Buscar Los ultimos 5 anime"
BottonTK = tk.Button(
    main_frame,
    text=lblBoton,
    command=BuscarAnimeTop5,
)
BottonTK.pack(side=tk.TOP, pady=10)

lblBoton = "Buscar Los ultimos 20 anime"
BottonTK = tk.Button(
    main_frame,
    text=lblBoton,
    command=BuscarAnimeTop20,
)
BottonTK.pack(side=tk.TOP, pady=10)

lblBoton = "Eliminar resultados"
BottonTK = tk.Button(
    main_frame,
    text=lblBoton,
    command=eliminar_resultados_anteriores,
)
BottonTK.pack(side=tk.TOP, pady=10)

root.mainloop()
