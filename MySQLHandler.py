import mysql.connector as SQL

mysql = SQL

class MySqlHandler:
    #TODO make the conn and cursor part of every event of the class
    def __init__(self, credentials:dict):
        self.db = mysql.connect(
            host = credentials["host"],
            database = credentials["database"],
            user = credentials["user"],
            password = credentials["password"],
        )

        self.cursor = self.db.cursor();

    def insert(self, vals:tuple):
        query = "INSERT INTO matriculas (matricula, plaza) VALUES (%s, %s)";
        self.cursor.execute(query, vals)
        self.db.commit()

        print("MySQL insert action");

    def read(self, val:str):
        query = "SELECT * FROM matriculas WHERE matricula =" + val;
        self.cursor.execute(query)
        result = self.cursor.fetchall();

        print("MySQL read action");
        return result
    
    def delete(self, val:str):
        query = "DELETE FROM matriculas WHERE matricula =" + val;
        self.cursor.execute(query)

        print("MySQL delete action");
        return
