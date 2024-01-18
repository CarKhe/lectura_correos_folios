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

def buscar_varias_expresiones_or(cadena,*patrones):
    for patron in patrones:
        r= mostrar_sin_ref(cadena,patron)
        if r: break
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
        return True
    else:
        return False    

def quitar_doble_espacio(folio):
    patron = r"(\s{2})"
    folio = re.sub(patron,' ',folio)
    return folio  

def lista_datos_folio(text,fecha,categoria,*patrones):
    lista = []
    lista.append(fecha)
    prioridad = mostrar_prioridad(text)
    if prioridad != None:
        lista.append(prioridad)
    if categoria:
        lista.append(categoria)
    for patron in patrones:
        try:
            val = re.findall(patron,text)
            lista.append(val[0])
        except:
            lista.append(False)
    return lista

def categoria_ti(folio):
    
    if mostrar_sin_ref(folio,r": (Conserva)"):
        return "Cuarto Frio"
    if mostrar_sin_ref(folio,r": (Hielo)"):
        return "CUARTO FRÍO DE HIELO"
    if mostrar_sin_ref(folio,r"(promedio)"):
        return "Aire Acondicionado"

def mostrar_info_folio(folio,tipo,fecha):
    folio = quitar_doble_espacio(folio)
    if tipo:
        ti = es_folio_ti(folio)
        if ti:
            categoria= categoria_ti(folio)
            lista = lista_datos_folio(folio,fecha,categoria,r"[0-9]{8}",r"[A-Z0-9]{10} ([\w\ ?]{2,}) \s?PDS",r"reporta:\ ([A-Z\ ]{1,})\ S",
            r"Situación: ([\w\  .>°-]{1,}) Equipo",r"Equipo: ([\w ]{1,}).")
            lista = tuple(lista)
            return lista
        else:
            categoria = False
            lista = lista_datos_folio(folio,fecha,categoria,r"Categoria: ([\w\ ]{1,})[.]? ",r"[0-9]{8}",r"[A-Z0-9]{10} ([\w\ ?]{2,}) \s?PDS"
            ,r"reporta:\ ([\w\ ]{1,}) Motivo",r"E?e?speci?í?fica: ([\w\ ,]{1,})\ ?\s?",r"Motivo: ([\w\ ,/]{1,})\s?\s?Representante")
            lista = tuple(lista)
            return lista

    
    
