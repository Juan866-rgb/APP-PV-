# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 16:15:23 2022

@author: JESID PEREZ
"""
import math
# math.ceil # pasa al valor siguiente 
import tkinter as tk
from tkinter import ttk

#def convertir_temp():
#    temp_celsius = float(caja_temp_celsius.get())
#    temp_kelvin = temp_celsius + 273.15
#    temp_fahrenheit = temp_celsius*1.8 + 32
#    etiqueta_temp_kelvin.config(text=f"Temperatura en K: {temp_kelvin}")
#    etiqueta_temp_fahrenheit.config(text=f"Temperatura en ºF: {temp_fahrenheit}")
    
    
#-------------------------------------------------------------------------------
    
ventana = tk.Tk()


ventana.title("PV calculator")
ventana.resizable(0,0)                                          # No deja redimensionar 
ventana.config(width=600, height=500)                           # Dimensiones
ventana.config(bg='white')                                      # color5

#-------------------------------- Pedir consumo diario -----------------------------------------------

etiqueta_temp_celsius = ttk.Label(text="Consumo diario (Watts):")
etiqueta_temp_celsius.place(x=10, y=10)


#--------------------------------- Caja para el valor de consumo----------------------------------------------

caja_temp_celsius = ttk.Entry()
caja_temp_celsius.place(x=140, y=10, width=50)


#-------------------------------- Pedir potencia del panel-----------------------------------------------

etiqueta_temp_celsius = ttk.Label(text="Potencia del panel(W):")
etiqueta_temp_celsius.place(x=200, y=10)

#--------------------------------- Caja para el valor de potencia panel----------------------------------------------

caja_potencia_panel = ttk.Entry()
caja_potencia_panel.place(x=320, y=10, width=50)


#-------------------------------- Pedir corriente del panel-----------------------------------------------

etiqueta_corriente_panel = ttk.Label(text="Corriente del panel(A):")
etiqueta_corriente_panel.place(x=200, y=40)

#--------------------------------- Caja para el valor de corriente panel----------------------------------------------

caja_corriente_panel = ttk.Entry()
caja_corriente_panel.place(x=320, y=40, width=50)


#--------------------------------- Pedir voltaje de baterias ----------------------------------------------

etiqueta_temp_celsius = ttk.Label(text="Voltaje baterias(V):")
etiqueta_temp_celsius.place(x=380, y=10)

#--------------------------------- Caja para el valor de baterias ----------------------------------------------


caja_voltaje_baterias = ttk.Combobox(values=["2", "6", "12", "24", "48"], state="readonly")
caja_voltaje_baterias.place(x=480, y=10, width=50)






#-----------------------------------------------------------------------------------------------------

#--------------------------------------- llamar las funciones-----------------------------------


#boton_convertir = ttk.Button(text="Convertir", command=convertir_temp)
#boton_convertir.place(x=20, y=60)

                                                
#etiqueta_temp_kelvin = ttk.Label(text="Temperatura en K: n/a")
#etiqueta_temp_kelvin.place(x=20, y=120)


#etiqueta_temp_fahrenheit = ttk.Label(text="Temperatura en ºF: n/a")
#etiqueta_temp_fahrenheit.place(x=20, y=160)

ventana.mainloop()