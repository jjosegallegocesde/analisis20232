from data.ListaUsuarios import usuarios
from helpers.crearCSV import crearCSVUsuarios
from helpers.crearHTML import crearTabla

import pandas as pd


#Usamos la funcion crearCSVusuarios
crearCSVUsuarios(usuarios,'bdUsuarios.csv')
#creando un dataframe desde una fuente CSV
dataFrameUsuarios=pd.read_csv('data/bdUsuarios.csv')
#convertir el DF en TABLA HTML
crearTabla(dataFrameUsuarios,'usuarios')

#Se filtran los datos
filtroUno=dataFrameUsuarios.query("(Edad>30) and (Nombre=='Jorge')")
print(filtroUno)
