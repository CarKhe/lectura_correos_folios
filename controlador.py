from modelo import Modelo
from datetime import datetime, timedelta
import re
class Controlador(Modelo):
    def __init__(self):
        super().__init__()
    def separar_datos(datos):
        for dato in datos:
            print(dato)
            
    def cambio_fecha(self,fecha_inicio):
        patron = r"[\w]{3}, ([\w :]{20}) [-\d]{5}"
        fecha_inicio = re.findall(patron,fecha_inicio)
        fecha = datetime.strptime(fecha_inicio[0], "%d %b %Y %H:%M:%S")
        fecha = str(fecha)
        return fecha
    
    def es_iot(self,reportador_por):
        if reportador_por == "TIENDA INTELIGENTE":
            return 1
        else:
            return 0
    
    def tipo_prioridad(self,prioridad):
        prioridad = str(prioridad).capitalize()
        if prioridad == "Alta":
            return 1
        elif prioridad == "Media":
            return 2
        elif prioridad == "Baja":
            return 3
    
    def qutar_datos_extra(self,dato):
        try:
            patron = r"(Falla)"
            dato = re.sub(patron,' ',dato)
            return dato 
        except:
            return dato
    
    def fecha_limite(self,fecha_inicio,prioridad):
        dt = datetime.strptime(fecha_inicio, '%Y-%m-%d %H:%M:%S')
        if prioridad == 1:
            result = dt + timedelta(hours=6)
        elif prioridad == 2:
            result = dt + timedelta(hours=72)
        elif prioridad == 3:
            result = dt + timedelta(hours=720)
        return result
        
        
    def ordenar_datos(self,datos):
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
            
            referencia =int(referencia)
            datos_insertar.append(referencia)
            
            fecha_inicio=self.cambio_fecha(fecha_inicio)
            fecha_inicio=str(fecha_inicio)
            datos_insertar.append(fecha_inicio)
            
            reporte = self.es_iot(reportador_por)
            reporte = reporte
            datos_insertar.append(reporte)
            
            categoria=self.qutar_datos_extra(categoria)
            categoria = str(categoria).upper()
            datos_insertar.append(categoria)
            
            detalle_folio = "Reportado: "+reportador_por+", Motivo: "+motivo+", Detalle: "+especifico
            datos_insertar.append(detalle_folio)
            
            prioridad = self.tipo_prioridad(prioridad)
            datos_insertar.append(prioridad)
            
            fecha_limite = self.fecha_limite(fecha_inicio,prioridad)
            fecha_limite =str(fecha_limite)
            datos_insertar.append(fecha_limite)
            
            datos_insertar = tuple(datos_insertar)
            self.insertar_folio(datos_insertar)