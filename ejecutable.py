from consulta_correo import *
from dotenv import load_dotenv
import os
from controlador import Controlador

class Main(Controlador):
    def __init__(self):
        super().__init__()
        load_dotenv()
        # Datos del usuario
        username = os.getenv("USER")
        password = os.getenv("PASSWORD")
        userfrom = os.getenv("USERFROM")
        datos = revisar_correo(username, password,userfrom)
        self.ordenar_datos(datos)  


Main()   