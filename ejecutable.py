from consulta_correo import *
from dotenv import load_dotenv
import os
from controlador import Controlador

load_dotenv()

# Datos del usuario
username = os.getenv("USER")
password = os.getenv("PASSWORD")
userfrom = os.getenv("USERFROM")

datos = revisar_correo(username, password,userfrom)
Controlador.ordenar_datos(datos)