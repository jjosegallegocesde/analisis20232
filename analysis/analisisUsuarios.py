from data.ListaUsuarios import usuarios
from helpers.crearCSV import crearCSVUsuarios
from helpers.crearHTML import crearTabla

import pandas as pd


#Usamos la funcion crearCSVusuarios
crearCSVUsuarios(usuarios,'bdUsuarios.csv')

#creando un dataframe desde una fuente CSV
dataFrameUsuarios=pd.read_csv('data/bdUsuarios.csv')
print(dataFrameUsuarios)

#convertir el DF en TABLA HTML
crearTabla(dataFrameUsuarios,'usuarios')
