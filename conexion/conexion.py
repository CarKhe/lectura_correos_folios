import mysql.connector

class MysqlConnection:
    def __init__(self):
        try:
            self.cnn = mysql.connector.connect(host="localhost", user="root", 
            passwd="", database="db_folios")
        except:
            print("No hay conexion a la base datos")

    
    def to_list_cmd(self,consult):
        data=self.search_all(consult)
        aux=""
        for row in data:
            aux=aux + str(row) + "\n"
        return aux
        
    def search_all(self, consult):
        cur = self.cnn.cursor()
        cur.execute(consult)
        data = cur.fetchall()
        cur.close()    
        return data
    
    def search_all_by_condition(self, table,condition):
        try:
            cur = self.cnn.cursor()
            cur.execute("SELECT * FROM {} WHERE {}".format(table,condition))
            datos = cur.fetchone()
            cur.close() 
            if datos is None:
                return False
            else:   
                return datos
        except:
            return False
    
    def search_select_columns(self, table,condition,*columns):
        cur = self.cnn.cursor()
        col=''
        for i in columns:
            col = col + f'{i},'    
        col = col[:-1]
        cur.execute("SELECT {} FROM {} WHERE {}".format(col,table,condition))
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    
    def insert(self,table,columns,values):
        cur = self.cnn.cursor()
        cur.execute("Insert into {} {} VALUES {}".format(table,columns,values))
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    
    
    def delete_by_id(self,table,condition):
        cur = self.cnn.cursor()
        cur.execute("DELETE FROM {} WHERE {}".format(table,condition))
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n  
    
    def update_row(self,table,values,condition):
        cur = self.cnn.cursor()
        cur.execute("UPDATE {} SET {} WHERE {}".format(table,values,condition))
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   



