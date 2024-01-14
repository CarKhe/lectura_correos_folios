import re
from oxxos import *

def obtener_num_folio(text):
    patron = r"[0-9]{8}"
    num_folio = re.findall(patron,text)
    num_folio=num_folio.pop()
    print("Folio: "+num_folio)

def comprobar_lista(ref,text,patron,oxxos):
    tienda = re.findall(patron,text)
    try:
        tienda= str(tienda[0]).upper()
        v = tienda in oxxos
    except:
        v= tienda
    if v: print(ref+": "+tienda)
    else: print(ref+": "+"False")

def mostrar_con_referencia(ref,text,patron):
    try:
        val = re.findall(patron,text)
        print(ref+": "+val[0])
    except:
        print(ref+": "+"False")

def mostrar_sin_ref(text,patron):
    try:
        val = re.findall(patron,text)
        if val !=[]:
            return True
        else:
            return False
    except:
        return False

def buscar_de_dos_o_mas_expresiones(cadena,*patrones):
    for patron in patrones:
        r= mostrar_sin_ref(cadena,patron)
        if r: continue
        else: return False
    return True

def mostrar_prioridad(text):
    try:
        patron = r"([BJALTAMEDI]{4,5})"
        valores = re.findall(patron,text)
        for val in valores:
            if (val == "BAJA") | (val == "MEDIA") | (val == "ALTA"):
                print("Prioridad: "+val)
                break
    except:
        return False
        
def mostrar_motivo(text):
    try:
        patron = r"Motivo: ([\w\ ,/]{1,})\s?\s?Representante"
        valores = re.findall(patron,text)
        print("Motivo: "+valores[0])
    except:
        return False

def buscar_oxxo(text):
    try:
        patron = r"tienda [A-Z0-9]{10} ([\w\ ?]{2,}) \s?PDS"
        valores = re.findall(patron,text)
        print("Oxxo: "+valores[0])
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
    
def quitar_doble_espacio(folio):
    patron = r"(\s{2})"
    folio = re.sub(patron,' ',folio)
    return folio        


def mostrar_info_folio(folio,tipo):
    folio = quitar_doble_espacio(folio)
    print(folio)
    if tipo == "Abierto":
        ti = es_folio_ti(folio)
        if ti:
            print("Folio TI")
            obtener_num_folio(folio)   
            mostrar_con_referencia("Oxxo",folio,r"[A-Z0-9]{10} ([\w\ ?]{2,}) \s?PDS") 
            print ("reportado por: TIENDA INTELIGENTE")
            mostrar_con_referencia("Situación",folio, r": ([\w\  >°-]{1,}) \s?Equ")
            mostrar_con_referencia("Equipo",folio, r"Equipo: ([\w ]{1,}).")
            mostrar_con_referencia("Prioridad",folio,r"([BJALTAMEDI]{4,5})")
        else:
            print("Folio Normal")
            obtener_num_folio(folio)   
            mostrar_con_referencia("Oxxo",folio,r"[A-Z0-9]{10} ([\w\ ?]{2,}) \s?PDS") 
            mostrar_con_referencia("Reportado por",folio, r"reporta:\ ([\w\ ]{1,})\ ?\s?")
            mostrar_con_referencia("Categoria",folio, r"Categoria: ([\w\ ]{1,}).?\ ?\s?")
            mostrar_con_referencia("Fallo especifico",folio, r"E?e?speci?í?fica: ([\w\ ,]{1,})\ ?\s?")
            mostrar_prioridad(folio)
            mostrar_motivo(folio)
    else:
        print("Folio Cierre")
        obtener_num_folio(folio)   
        buscar_oxxo(folio) 
        mostrar_motivo(folio)
        mostrar_con_referencia("Fallo especifico",folio, r"E?e?speci?í?fica: ([\w\ ,]{1,})\ ?\s?")
        mostrar_con_referencia("Reportado por",folio, r"reporta:\ ([\w\ ]{1,})\ ?\s?")
        mostrar_con_referencia("Categoria",folio, r"Categoria: ([\w\ ]{1,}).?\ ?\s?")
        

    
def folio_abierto_cerrado(subject):
    res = buscar_de_dos_o_mas_expresiones(subject,r"(Abierto)",r"[0-9]{8}")
    if res:
        return "Abierto",True
    else:
        res = buscar_de_dos_o_mas_expresiones(subject,r"(Cierre)",r"[0-9]{8}")
        if res:
            return "Cerrado",True
    return False,False
    
        




