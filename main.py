# Calculadora RGB con interfaz gráfica 

"""
@Author: Sebastian Sanchez Bentolila
GitHub: https://github.com/Sebastian-Sanchez-Bentolila
Intagram: @sebas.code_crypto
"""

# Módulos
from tkinter import *
import os
import tkinter.messagebox as messagebox
import pyperclip
import random
import webbrowser

# Función para convertir RGB a hexadecimal
def rgb_to_hex(rgb_tuple):
    r, g, b = [max(0, min(255, val)) for val in rgb_tuple]
    hex_r = hex(r)[2:].zfill(2)
    hex_g = hex(g)[2:].zfill(2)
    hex_b = hex(b)[2:].zfill(2)
    hex_color = "#" + hex_r + hex_g + hex_b
    return hex_color

# Clase principal
class Panel_Principal:
    def __init__(self):
        # Configuración de la ventana
        self.ventana = Tk()
        self.ventana.geometry('400x350') 
        self.ventana.title('Calculadora RGB')
        
        self.Ruta_Trabajo = os.getcwd()
        self.ventana.iconbitmap('{}\\archivos\\icon\\circuloRGB.ico'.format(self.Ruta_Trabajo))
        self.ventana.resizable(0, 0)
        self.ventana.config(bg='black', cursor='tcross')
        self.Widgets()
        
    # Controles  
    def Widgets(self):
        # Rojo
        self.red_label = Label(text="Red:", fg="white", bg="black")
        self.red_label.place(x=50, y=50)

        self.red_slider = Scale(from_=0, to=255, length=200, orient=HORIZONTAL, bg="#FF0000", troughcolor="black")
        self.red_slider.set(0)
        self.red_slider.place(x=100, y=30)
        
        # Verde
        self.green_label = Label(text="Green:", fg="white", bg="black")
        self.green_label.place(x=50, y=90)

        self.green_slider = Scale(from_=0, to=255, length=200, orient=HORIZONTAL, bg="#00FF00", troughcolor="black")
        self.green_slider.set(0)
        self.green_slider.place(x=100, y=70)
        
        # Azul
        self.blue_label = Label(text="Blue:", fg="white", bg="black")
        self.blue_label.place(x=50, y=130)

        self.blue_slider = Scale(from_=0, to=255, length=200, orient=HORIZONTAL, bg="#0000FF", troughcolor="black")
        self.blue_slider.set(0)
        self.blue_slider.place(x=100, y=110)
        
        # Resultado
        self.rgb_value = StringVar()  # Variable para almacenar el valor RGB
        self.hex_value = StringVar()  # Variable para almacenar el valor hexadecimal

        self.rgb_label = Entry(textvariable=self.rgb_value, state="readonly", fg="black", bg="white", width=15)
        self.rgb_label.place(x=55, y=170)

        self.hex_label = Entry(textvariable=self.hex_value, state="readonly", fg="black", bg="white", width=15)
        self.hex_label.place(x=210, y=170)
        
        # Canvas para mostrar el color
        self.color_canvas = Canvas(self.ventana, width=250, height=100, bg='black')
        self.color_canvas.place(x=55, y=200)
        
        # Botón de copiar
        self.BotonCopiar = Button(self.ventana, text="Copiar", bg="gray", fg="white", command=self.copiar_hex)
        self.BotonCopiar.place(x=320, y=166)

        # Botón de cambio de modo
        self.modo_normal = True
        self.BotonModo = Button(self.ventana, text="Modo Oscuro", bg="gray", fg="white", command=self.cambiar_modo)
        self.BotonModo.place(x=0, y=0)
        
        # Botón de limpiar
        self.BotonLimpiar = Button(self.ventana, text="Limpiar", bg="gray", fg="white", command=self.limpiar)
        self.BotonLimpiar.place(x=0, y=27)
        
        # Botón para generar un color aleatorio
        self.BotonGenerarColorAleatorio = Button(self.ventana, text="Generar color aleatorio", bg="gray", fg="white", command=self.generate_random_color)
        self.BotonGenerarColorAleatorio.place(x=5, y=310)
        
        # Asociar la función de actualización al cambio en los sliders
        self.red_slider.configure(command=self.Update_Result)
        self.green_slider.configure(command=self.Update_Result)
        self.blue_slider.configure(command=self.Update_Result)
        
        # Campo de entrada para el valor hexadecimal        
        self.hex_input = Entry(self.ventana, fg="gray", bg="white", width=17)
        self.hex_input.insert(0, "Valor Hexadecimal: ")
        self.hex_input.bind('<FocusIn>', self.on_entry_click)
        self.hex_input.bind('<FocusOut>', self.on_focus_out)
        self.hex_input.place(x=200, y=313)

        # Botón para aplicar el valor hexadecimal ingresado
        self.BotonAplicarHex = Button(self.ventana, text="Aplicar", bg="gray", fg="white", command=self.apply_hex_value)
        self.BotonAplicarHex.place(x=310, y=310)
        
        # Botón sobre el desarrollador 
        self.BotonDesarrollador = Button(self.ventana, text="Desarrollador", bg="orange", fg="black", command=self.Abrir_pagina)
        self.BotonDesarrollador.place(x=315, y=5)
     
    # Funciones para agregar y quitar el texto predeterminado a hex_input
    def on_entry_click(self, event):
        if self.hex_input.get() == "Valor Hexadecimal: ":
            self.hex_input.delete(0, "end") # Eliminar el texto predeterminado al hacer clic
            self.hex_input.config(fg='black')
    def on_focus_out(self, event):
        if self.hex_input.get() == "":
            self.hex_input.insert(0, "Valor Hexadecimal: ") # Insertar el texto predeterminado si no hay texto ingresado
            self.hex_input.config(fg='gray')
            
    # Función para correr la ventana gráfica   
    def RunApp(self):
        self.ventana.mainloop()
      
    # Función para andar modificando el color final, según en que posición este cada slider  
    def Update_Result(self, *args):
        self.red_value = self.red_slider.get()
        self.green_value = self.green_slider.get()
        self.blue_value = self.blue_slider.get()

        self.rgb_value.set(f"({self.red_value}, {self.green_value}, {self.blue_value})")
        color_hex = rgb_to_hex((self.red_value, self.green_value, self.blue_value))
        self.hex_value.set(color_hex)
        self.color_canvas.config(bg=color_hex)

    # Funcion para copiar el número hexadecimal en el portapapeles
    def copiar_hex(self):
        color_hex = self.hex_value.get()
        pyperclip.copy(color_hex)
        messagebox.showinfo("Copiado", f"El color hexadecimal {color_hex} ha sido copiado al portapapeles.")

    # Función para cambiar el tema a oscuro o claro
    def cambiar_modo(self):
        if self.modo_normal:
            self.ventana.config(bg='white', cursor='tcross')
            self.BotonModo.config(text="Modo Claro")
            self.red_label.config(fg="black", bg="white")
            self.green_label.config(fg="black", bg="white")
            self.blue_label.config(fg="black", bg="white")
            self.red_slider.config(troughcolor="white")
            self.green_slider.config(troughcolor="white")
            self.blue_slider.config(troughcolor="white")
            self.modo_normal = False
        else:
            self.ventana.config(bg='black', cursor='tcross')
            self.BotonModo.config(text="Modo Oscuro")
            self.red_label.config(fg="white", bg="black")
            self.green_label.config(fg="white", bg="black")
            self.blue_label.config(fg="white", bg="black")
            self.red_slider.config(troughcolor="black")
            self.green_slider.config(troughcolor="black")
            self.blue_slider.config(troughcolor="black")
            self.modo_normal = True
     
    # Función para limpiar el color y dejar en #000000 (negro)   
    def limpiar(self):
        self.red_slider.set(0)
        self.green_slider.set(0)
        self.blue_slider.set(0)
        self.Update_Result()
        
    # Función para generar un color aleatorio
    def generate_random_color(self):
        self.red = random.randint(0, 255)
        self.green = random.randint(0, 255)
        self.blue = random.randint(0, 255)
        self.red_slider.set(self.red)
        self.green_slider.set(self.green)
        self.blue_slider.set(self.blue)
        
    # Función para aplicar el valor hexadecimal ingresado por el usuario
    def apply_hex_value(self):
        color_hex = self.hex_input.get()
        color_hex = color_hex.replace("#", '')
        try:
            r, g, b = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))
            self.red_slider.set(r)
            self.green_slider.set(g)
            self.blue_slider.set(b)
            self.Update_Result()
            self.hex_input.config(bg='white')
        except ValueError:
            self.hex_input.config(bg='red')
            messagebox.showerror("Error", "Valor hexadecimal inválido. Intente nuevamente.")
            
    # Función para abrir la pagina de mi portafolio WEB
    def Abrir_pagina(self):
        self.url = "https://sebastian-sanchez.netlify.app/"
        webbrowser.open(self.url)

# Función Principal - Main
if __name__ == '__main__':
    Sofware = Panel_Principal()
    Sofware.RunApp()