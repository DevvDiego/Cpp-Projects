import mysql.connector as SQL

mysql = SQL

class MySqlHandler:

    def __init__(self, credentials:dict):
        self.credentials = credentials
    

    def dbexecute(self, query:str, values:tuple):
        conn = mysql.connect(**self.credentials); #discompose the dict
        cursor = conn.cursor();
        
        cursor.execute(query, values);
        conn.commit();

        cursor.close();
        conn.close();

    def insert(self, values:tuple):
        query = "INSERT INTO matriculas (matricula, plaza) VALUES (%s, %s)";
        self.dbexecute(query, values);

        print("MySQL insert action");

    def read(self, val:str):
        query = "SELECT * FROM matriculas WHERE matricula =" + val;
        self.cursor.execute(query)
        self.db.commit();
        result = self.cursor.fetchall();

        print("MySQL read action");
        return result
    
    def delete(self, values:tuple):
        query = "DELETE FROM matriculas WHERE matricula = %s";
        self.dbexecute(query, values);


        print("MySQL delete action");
        return
