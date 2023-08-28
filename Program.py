from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import Data 


# VARIABLES
txt_url = Data.get_url()
txt_Titulo = Data.get_TitlePage(txt_url)
Txt_AnimeImagen = Data.get_AnimeImage(txt_url)
Txt_AnimeTitulo = Data.get_AnimeTitle(txt_url)

# ************************************ Create App ************************************************
root = Tk()
root.title = "Recomendaciones Personalizadas"
root.geometry("1080x720")

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


count = 0
image_labels = []
for DivsTitulos, imagen in zip(Txt_AnimeTitulo, Txt_AnimeImagen) :
    count = count + 1
    if count > 2:
        # ********************** Nombre Del Anime **********************
        LblTexto = tk.Label(Second_frame, text=DivsTitulos, font=("Arial", 8))
        LblTexto.pack(pady=20)
        
        # ********************** Imagen **********************
        #Descargar la imagen desde la URL
        response = requests.get(imagen)
        image_data = BytesIO(response.content)
        image = Image.open(image_data)

        #Convertir la imagen a un formato que Tkinter pueda manejar
        tk_image = ImageTk.PhotoImage(image)

        #Mostrar la imagen en un widget Label
        image_label = tk.Label(Second_frame, image=tk_image)
        image_label.pack()
        
        # Agregar la instancia de Label a la lista
        image_labels.append(image_label)
    


root.mainloop()

