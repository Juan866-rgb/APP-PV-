# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 16:15:23 2022

@author: JESID PEREZ; @author: JESUS SANTANA; @author: JUAN MONSALVE
"""
import math # math.ceil # pasa al valor siguiente 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

#def convertir_temp():
#    temp_celsius = float(caja_temp_celsius.get())
#    temp_kelvin = temp_celsius + 273.15
#    temp_fahrenheit = temp_celsius*1.8 + 32
#    etiqueta_temp_kelvin.config(text=f"Temperatura en K: {temp_kelvin}")
#    etiqueta_temp_fahrenheit.config(text=f"Temperatura en ºF: {temp_fahrenheit}")

# Numero de paneles
def calcular_paneles() :

    try:
        consumo = float(caja_consumo_diario.get())
        potencia_panel = float(caja_potencia_panel.get())
        capacidad_individual_baterias = float(caja_capacidad_baterias.get())
        dias_de_autonomia = float(caja_días_de_operacion.get())
        corriente_panel = float(caja_corriente_panel.get())
    except:
        messagebox.showinfo('Warning','Entrada Inválida. Intente de Nuevo')

    # Aproximado    
    consumo_con_factor_de_error = consumo*(1.2)
    eficiencia_panel = 0.9
    horas_solares = 4
    numero_de_paneles = consumo_con_factor_de_error/(horas_solares*eficiencia_panel*potencia_panel)
    etiqueta_numero_de_paneles_aprox.config(text=f"Número de paneles necesarios aproximados: {math.ceil(numero_de_paneles)} módulos")
    
    # Exacto
    eficiencia_bateria = 0.95
    eficiencia_controlador = 1
    eficiencia_inversor = 0.9
    numero_de_paneles_2 = (consumo_con_factor_de_error/eficiencia_inversor*eficiencia_controlador*eficiencia_bateria)/(horas_solares*eficiencia_panel*potencia_panel)
    etiqueta_numero_de_paneles_exac.config(text=f"Número de paneles necesarios exactos: {math.ceil(numero_de_paneles_2)} módulos")

    # Cálculo acumuladores
    voltaje_sistema = float(caja_voltaje_sistema.get())
    profundidad_de_descarga = float(caja_profundidad_de_descarga.get())/100
    c_a = consumo_con_factor_de_error*dias_de_autonomia/(voltaje_sistema*profundidad_de_descarga)
    etiqueta_c_a.config(text=f"Cálculo acumuladores: {round(c_a)} Ah")
    
    # Número de Baterías
    voltaje_baterias = float(caja_voltaje_baterias.get())
    arreglo_de_baterias = math.ceil(c_a/capacidad_individual_baterias)
    numero_baterias = arreglo_de_baterias*(voltaje_sistema/voltaje_baterias)
    etiqueta_numero_baterias.config(text=f"Número baterías: {math.ceil(numero_baterias)} Baterías en arreglos de {arreglo_de_baterias}")

    # Controldor de carga
    corriente_entrada = 1.25*numero_de_paneles_2*corriente_panel
    corriente_salida = 1.25*(392/0.9)/voltaje_sistema

#-------------------------------------------------------------------------------
    
ventana = tk.Tk()                                                              # Se crea la ventana
ventana.title("PV calculator")                                                 # Título de la ventana
ventana.resizable(0,0)                                                         # No deja redimensionar 
ventana.config(width=800, height=600)                                          # Dimensiones
ventana.config(bg='white')                                                     # color del fondo

#--------------------------------- Estética ----------------------------------------------

ventana.iconbitmap("C:/Users/JESID PEREZ/Documents/GitHub/APP-PV-/Aestethic/Icono1.ico")

icono_grande = tk.PhotoImage(file="C:/Users/JESID PEREZ/Documents/GitHub/APP-PV-/Aestethic/Barra.png")

imagen = PhotoImage(file = "C:/Users/JESID PEREZ/Documents/GitHub/APP-PV-/Aestethic/ejemplo1.png")

# Con Label y la opción image, puedes mostrar una imagen en el widget:
background = Label(image = imagen, text = "Imagen")

# Con place puedes organizar el widget de la imagen posicionandolo
# donde lo necesites (relwidth y relheight son alto y ancho en píxeles):
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)


#-------------------------------- Pedir consumo diario -----------------------------------------------

etiqueta_consumo_diario = ttk.Label(text="Consumo Diario (Watts):")            # Nombre de la etiqueta
etiqueta_consumo_diario.place(x=10, y=10)                                      # Posición de la etiqueta


#--------------------------------- Caja para el valor de consumo----------------------------------------------

caja_consumo_diario = ttk.Entry()
caja_consumo_diario.place(x=145, y=10, width=50)



#-------------------------------- Pedir potencia del panel-----------------------------------------------

etiqueta_potencia_panel = ttk.Label(text="Potencia del Panel(W):")             # Nombre de la etiqueta
etiqueta_potencia_panel.place(x=200, y=10)                                     # Posición de la etiqueta

#--------------------------------- Caja para el valor de potencia panel----------------------------------------------

caja_potencia_panel = ttk.Entry()
caja_potencia_panel.place(x=320, y=10, width=50)



#-------------------------------- Pedir corriente del panel-----------------------------------------------

etiqueta_corriente_panel = ttk.Label(text="Corriente del Panel(A):")           # Nombre de la etiqueta
etiqueta_corriente_panel.place(x=200, y=40)                                    # Posición de la etiqueta

#--------------------------------- Caja para el valor de corriente panel----------------------------------------------

caja_corriente_panel = ttk.Entry()
caja_corriente_panel.place(x=320, y=40, width=50)



#--------------------------------- Pedir voltaje de baterias ----------------------------------------------

etiqueta_voltaje_baterias = ttk.Label(text="Voltaje Baterías(V):")             # Nombre de la etiqueta
etiqueta_voltaje_baterias.place(x=380, y=10)                                   # Posición de la etiqueta

#--------------------------------- Caja para voltaje de baterias ----------------------------------------------

caja_voltaje_baterias = ttk.Combobox(values=["2", "6", "12", "24", "48"], state="readonly")
caja_voltaje_baterias.place(x=480, y=10, width=50)



#--------------------------------- Pedir corriente de baterias ----------------------------------------------

etiqueta_capacidad_baterias = ttk.Label(text="Capacidad Baterías(Ah):")             # Nombre de la etiqueta
etiqueta_capacidad_baterias.place(x=380, y=40)                                   # Posición de la etiqueta

#--------------------------------- Caja para corriente de baterias ----------------------------------------------

caja_capacidad_baterias = ttk.Entry()
caja_capacidad_baterias.place(x=510, y=40, width=50)




#--------------------------------- Pedir voltaje del sistema ----------------------------------------------

etiqueta_voltaje_sistema = ttk.Label(text="Voltaje Sistema(V):")             # Nombre de la etiqueta
etiqueta_voltaje_sistema.place(x=380, y=70)                                   # Posición de la etiqueta

#--------------------------------- Caja para voltaje del sistema ----------------------------------------------

caja_voltaje_sistema = ttk.Combobox(values=["2", "6", "12", "24", "48"], state="readonly")
caja_voltaje_sistema.place(x=480, y=70, width=50)



#--------------------------------- Pedir profundidad de descarga ----------------------------------------------

etiqueta_profundidad_de_descarga = ttk.Label(text="Profundidad de descarga de las baterias(%):")             # Nombre de la etiqueta
etiqueta_profundidad_de_descarga.place(x=380, y=100)                                   # Posición de la etiqueta

#--------------------------------- Caja para profundidad de descarga ----------------------------------------------

caja_profundidad_de_descarga = ttk.Combobox(values=["60", "80", "85", "90", "95"], state="readonly")
caja_profundidad_de_descarga.place(x=615, y=100, width=50)



#--------------------------------- Días de Operación ----------------------------------------------

etiqueta_días_de_operacion = ttk.Label(text="Días de Operación:")             # Nombre de la etiqueta
etiqueta_días_de_operacion.place(x=380, y=130)                                   # Posición de la etiqueta

#--------------------------------- Caja para Días de Operación ----------------------------------------------

caja_días_de_operacion = ttk.Entry()
caja_días_de_operacion.place(x=485, y=130, width=50)



#-------------------------------- Pedir voltaje del inversor -----------------------------------------------

etiqueta_voltaje_inversor = ttk.Label(text="Voltaje inversor(V):")             # Nombre de la etiqueta
etiqueta_voltaje_inversor.place(x=200, y=70)                                   # Posición de la etiqueta


#--------------------------------- Caja para el voltaje del inversor ----------------------------------------------

caja_voltaje_inversor = ttk.Combobox(values=["12", "24", "48", "96", "120"], state="readonly")
caja_voltaje_inversor.place(x=300, y=70, width=50)



#-------------------------------- Pedir factor de seguridad del inversor -----------------------------------------------

etiqueta_factor_inversor = ttk.Label(text="Factor del inversor(%):")           # Nombre de la etiqueta
etiqueta_factor_inversor.place(x=200, y=100)                                   # Posición de la etiqueta     


#--------------------------------- Caja para el factor de seguridad del inversor ----------------------------------------------

caja_factor_inversor = ttk.Combobox(values=["0", "20", "25", "30", "50"], state="readonly")
caja_factor_inversor.place(x=320, y=100, width=50)





#-----------------------------------------------------------------------------------------------------

#--------------------------------------- llamar las funciones-----------------------------------
#                                                 
boton_calcular_paneles = ttk.Button(text="Calcular número de paneles", command = calcular_paneles)
boton_calcular_paneles.place(x=20, y=130)

etiqueta_numero_de_paneles_aprox = ttk.Label(text='Número de paneles necesarios aprox: n/a')
etiqueta_numero_de_paneles_aprox.place(x=20, y=160)

etiqueta_numero_de_paneles_exac = ttk.Label(text='Número de paneles necesarios exac: n/a')
etiqueta_numero_de_paneles_exac.place(x=20, y=180)

etiqueta_c_a = ttk.Label(text='Cálculo acumuladores: n/a')
etiqueta_c_a.place(x=20, y=200)

etiqueta_numero_baterias = ttk.Label(text='Número baterías: n/a')
etiqueta_numero_baterias.place(x=20, y=220)

ventana.mainloop()
