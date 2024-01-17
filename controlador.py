from modelo import Modelo
from datetime import datetime
import re
class Controlador:
    def separar_datos(datos):
        for dato in datos:
            print(dato)
    
    def ordenar_datos(datos):
        for dato in datos:
            datos_insertar = []
            fecha_inicio = dato[0]
            prioridad = dato[1]
            categoria = dato[2]
            referencia = dato[3]
            oxxo = dato[4]
            reportador_por = dato[5]
            motivo = dato[6]
            especifico = dato[7]
            
            oxxo = str(oxxo).upper()
            datos_insertar.append(oxxo)
            referencia = int(referencia)
            datos_insertar.append(referencia)
            
            patron = r"[\w]{3}, ([\w :]{20}) [-\d]{5}"
            fecha_inicio = re.findall(patron,fecha_inicio)
            fecha = datetime.strptime(fecha_inicio[0], "%d %b %Y %H:%M:%S")
            fecha = str(fecha)
            datos_insertar.append(fecha)
            
            if reportador_por == "TIENDA INTELIGENTE":
                datos_insertar.append(1)
            else:
                datos_insertar.append(0)
            
            categoria = str(categoria).upper()
            datos_insertar.append(categoria)
            
            detalle_folio = "Reportado: "+reportador_por+", Motivo: "+motivo+", Detalle: "+especifico
            datos_insertar.append(detalle_folio)
            
            prioridad = str(prioridad).capitalize()
            datos_insertar.append(prioridad)
            
            datos_insertar = tuple(datos_insertar)
            Modelo.insertar(datos_insertar)