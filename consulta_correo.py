import imaplib
import email
from email.header import decode_header
from datos import *




def revisar_correo(username, password,correo_enviado):
    datos_completos = []
    # Crear conexión
    imap = imaplib.IMAP4_SSL("outlook.office365.com")
    # iniciar sesión
    imap.login(username, password)
    status, mensajes = imap.select("INBOX")
    N = 15
    # cantidad total de correos
    mensajes = int(mensajes[0])
    
    for i in range(mensajes, mensajes - N, -1):
        try:
            res, mensaje = imap.fetch(str(i), "(RFC822)")
        except:
            break
        for respuesta in mensaje:
            if isinstance(respuesta, tuple):
                # Obtener el contenido
                mensaje = email.message_from_bytes(respuesta[1])
                
                # decodificar el contenido
                subject = decode_header(mensaje["Subject"])[0][0]
                fecha = decode_header(mensaje["date"])[0][0]
                from_ = mensaje.get("From")
                res = folio_abierto_cerrado(subject)
                correo_deseado  = confirmar_correo(from_)
                if bool(correo_deseado == correo_enviado) & (res):
                    if mensaje.is_multipart():
                        # Recorrer las partes del correo
                        for part in mensaje.walk():
                            # Extraer el contenido
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            try:
                                # el cuerpo del correo
                                body = part.get_payload(decode=True).decode()
                            except:
                                pass
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                # Mostrar el cuerpo del correo
                                
                                datos = mostrar_info_folio(body,res,fecha)
                                datos_completos.append(datos)
                    else:
                        # contenido del mensaje
                        content_type = mensaje.get_content_type()
                        # cuerpo del mensaje
                        body = mensaje.get_payload(decode=True).decode()
                        if content_type == "text/plain":
        #                     # mostrar solo el texto
                            print(body)
                                   
    imap.close()
    imap.logout()
    return datos_completos 