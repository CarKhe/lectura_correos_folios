from conexion.conexion import MysqlConnection
class Modelo(MysqlConnection):
    table ='tbl_folios'
    values="(id_oxxo,referencia,fecha_inicio,iot,detalle_folio,fecha_limite,id_prioridad,id_area_oxxo)"
    def __init__(self):
        super().__init__()
    
    def buscar_oxxo(self,oxxo):
        try:
            resultado = self.search_select_columns("tbl_oxxo","name_oxxo='"+oxxo+"'","id_oxxo")
            return resultado[0]
        except:
            return False
    
    def buscar_area_oxxo(self,oxxo):
        try:
            resultado = self.search_select_columns("tbl_area_oxxo","area_oxxo='"+oxxo+"'","id_area_oxxo")
            return resultado[0]
        except:
            return False
        
    def buscar_por_referencia(self,referencia):
        datos = self.search_all_by_condition(self.table,f"referencia={referencia}")
        if datos:
            return False
        else:
            return True
   
    def insertar_folio(self,dato): 
        insert=self.buscar_por_referencia(dato[1])
        if insert:
            id_oxxo = self.buscar_oxxo(dato[0])
            referencia = dato[1]
            fecha_inicio = dato[2]
            iot = dato[3]
            id_area_oxxo = self.buscar_area_oxxo(dato[4])
            detalle_folio = dato[5]
            fecha_limite = dato[7]
            id_prioridad = dato[6]
            datos_inseratar =  f"({id_oxxo},{referencia},'{fecha_inicio}',{iot},'{detalle_folio}','{fecha_limite}',{id_prioridad},{id_area_oxxo})"
            result = self.insert(self.table,self.values,datos_inseratar)
            print(result)
        else:
            print(0)
        
        
        


        
        
        
        
        
    