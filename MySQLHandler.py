import mysql.connector as SQL

mysql = SQL

class MySqlHandler:
    isRead = False; #internal flag to mark a read operation

    def __init__(self, credentials:dict):
        self.credentials = credentials
    

    def dbexecute(self, query:str, values:tuple=("",)) -> list[tuple] | None:
        #have the values tuple to a default tuple in case there is a read op
        # so interpreter doesnt mark an error
        conn = mysql.connect(**self.credentials); #discompose the dict
        cursor = conn.cursor();
        
        if(MySqlHandler.isRead):
            cursor.execute(query);
            result = cursor.fetchall()

            cursor.close();
            conn.close();
        
            return result;
    
        cursor.execute(query, values);
        conn.commit();

        cursor.close();
        conn.close();



    #? might be useful to make cpp and db go in the same data path?
    # def dbexecutemany(self, query:str, values:tuple):
    #     conn = mysql.connect(**self.credentials); #discompose the dict
    #     cursor = conn.cursor();
        
    #     cursor.executemany(query, values);
    #     conn.commit();

    #     cursor.close();
    #     conn.close();

    def insert(self, values:tuple):
        query = "INSERT INTO matriculas (matricula, plaza) VALUES (%s, %s)";
        self.dbexecute(query, values);

        print("MySQL insert action");

    def read(self, val:str):
        MySqlHandler.isRead = True;

        query = "SELECT * FROM matriculas WHERE matricula =" + val;
        self.cursor.execute(query)
        self.db.commit();
        result = self.cursor.fetchall();

        print("MySQL read action");
        return result
    
    def readAll(self):
        MySqlHandler.isRead = True;

        #? add to dbexecute trouhg a flag param?
        query = "SELECT * FROM matriculas";

        result = self.dbexecute(query)
        
        print("mysql readAll")

        #mark isRead as false again after operations
        MySqlHandler.isRead= False;
        return result;

    def delete(self, values:tuple):
        query = "DELETE FROM matriculas WHERE matricula = %s";
        self.dbexecute(query, values);


        print("MySQL delete action");
        return
