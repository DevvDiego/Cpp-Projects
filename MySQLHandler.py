import mysql.connector as SQL

mysql = SQL

class MySqlHandler:
    # isRead = False; #internal flag to mark a read operation

    def __init__(self, credentials:dict):
        self.credentials = credentials

    def insert(self, values:tuple):
        conn = mysql.connect(**self.credentials); #discompose the dict
        cursor = conn.cursor();

        cursor.execute(
            operation="INSERT INTO matriculas (matricula, plaza) VALUES (%s, %s)",
            params=values 
        );
        conn.commit();

        cursor.close();
        conn.close();    

    def read_all(self) -> list[tuple]:
        conn = mysql.connect(**self.credentials); #discompose the dict
        cursor = conn.cursor();

        cursor.execute(
            operation="SELECT * FROM matriculas", 
        );
        result = cursor.fetchall();

        cursor.close();
        conn.close();

        print("MySQL read all action");
        return result  
    
    def delete(self, value:tuple):
        conn = mysql.connect(**self.credentials); #discompose the dict
        cursor = conn.cursor();

        cursor.execute(
            operation="DELETE FROM matriculas WHERE matricula = %s",
            params=value 
        );
        conn.commit()

        cursor.close();
        conn.close();

        print("MySQL delete action"); 
        