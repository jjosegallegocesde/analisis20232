from data.ListaUsuarios import usuarios
from helpers.crearCSV import crearCSVUsuarios 

#Usamos la funcion crearCSVusuarios
crearCSVUsuarios(usuarios,'bdUsuarios.csv')