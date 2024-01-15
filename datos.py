import re


def confirmar_correo(from_):
    patron = r"<([a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})>"
    correo_deseado = re.findall(patron,from_)
    return correo_deseado[0]

def buscar_varias_expresiones(cadena,*patrones):
    for patron in patrones:
        r= mostrar_sin_ref(cadena,patron)
        if r: continue
        else: return False
    return True

def mostrar_sin_ref(text,patron):
    try:
        val = re.findall(patron,text)
        if val !=[]:
            return True
        else:
            return False
    except:
        return False

def mostrar_prioridad(text):
    try:
        patron = r"([BJALTAMEDI]{4,5})"
        valores = re.findall(patron,text)
        for val in valores:
            if (val == "BAJA") | (val == "MEDIA") | (val == "ALTA"):
                return val
        return None
    except:
        return False

def es_folio_ti(text):
    try:
        patron = r"reporta:\ ([A-Z\ ]{1,})\ S"
        val = re.findall(patron,text)
        if val[0] == "TIENDA INTELIGENTE":
            return True
        else:
            return False
    except:
        return False
    
def folio_abierto_cerrado(subject):
    res = buscar_varias_expresiones(subject,r"(Abierto)",r"[0-9]{8}")
    if res:
        return "Abierto",True
    else:
        res = buscar_varias_expresiones(subject,r"(Cierre)",r"[0-9]{8}")
        if res:
            return "Cerrado",True
    return False,False      

def quitar_doble_espacio(folio):
    patron = r"(\s{2})"
    folio = re.sub(patron,' ',folio)
    return folio  

def lista_datos_folio(text,*patrones):
    lista = []
    for patron in patrones:
        try:
            val = re.findall(patron,text)
            lista.append(val[0])
        except:
            lista.append(False)
    prioridad = mostrar_prioridad(text)
    if prioridad != None:
        lista.append(prioridad)
    return lista

def mostrar_info_folio(folio,tipo):
    folio = quitar_doble_espacio(folio)
    if tipo == "Abierto":
        ti = es_folio_ti(folio)
        if ti:
            
            lista = lista_datos_folio(folio,r"[0-9]{8}",r"[A-Z0-9]{10} ([\w\ ?]{2,}) \s?PDS",r"reporta:\ ([A-Z\ ]{1,})\ S",
            r": ([\w\  >°-]{1,}) \s?Equ",r"Equipo: ([\w ]{1,}).")
            print(lista)
        else:
            
            lista = lista_datos_folio(folio,r"[0-9]{8}",r"[A-Z0-9]{10} ([\w\ ?]{2,}) \s?PDS",r"reporta:\ ([\w\ ]{1,})\ ?\s?",
            r"Categoria: ([\w\ ]{1,}).?\ ?\s?",r"E?e?speci?í?fica: ([\w\ ,]{1,})\ ?\s?",r"Motivo: ([\w\ ,/]{1,})\s?\s?Representante")
            print(lista)
    else:
        
        lista = lista_datos_folio(folio,r"[0-9]{8}",r"[A-Z0-9]{10} ([\w\ ?]{2,}) \s?PDS",r"reporta:\ ([\w\ ]{1,})\ ?\s?",r"Categoria: ([\w\ ]{1,}).?\ ?\s?",
            r"E?e?speci?í?fica: ([\w\ ,]{1,})\ ?\s?",r"Motivo: ([\w\ ,/]{1,})\s?\s?Representante")
        print(lista)