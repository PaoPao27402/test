import mysql.connector

class DAL:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="P@22word2710",
            database="travel_agency"
        )
        print(f'DB connected: {self.connection.is_connected()}')

    def get_table(self, sql, params=None):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            table = cursor.fetchall()
        return table
        
    # def get_table_v1(self, sql, params=None):
    #     cursor = self.connection.cursor()
    #     cursor.execute(sql, params) 
    #     table = cursor.fetchall()
    #     cursor.close()
    #     return table
    
    def get_scalar(self, sql, params=None):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            scalar = cursor.fetchone()
        return scalar
        
    def insert(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit() # Save to database now.
            last_row_id = cursor.lastrowid
        return last_row_id 

    def update(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit() # Save to database now.
            row_count = cursor.rowcount
        return row_count
       
    def delete(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit() # Save to database now.
            row_count = cursor.rowcount
        return row_count
    
    def close(self):
        self.connection.close()