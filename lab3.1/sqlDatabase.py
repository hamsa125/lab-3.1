import sqlite3
#find commit errors
class CJRecord:

    database= "Worldrecord5.db"

#initialize database
    def __init__(self):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
#create database it not exist
    #Todo give good table name + input verifecation for catches row
    def create(self):
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS ChainsawJuggling(RecordHolder TEXT NOT NULL,Country TEXT NOT NULL, NumofCatches INT NOT NULL);")
            self.connection.commit()
        except sqlite3.Error as er:
            print("Create table Error ",er)

# insert data into that table
    def insert(self, data):
        query = "INSERT INTO ChainsawJuggling VALUES(?, ?, ?)"
        try:
            self.cursor.execute(query, data)
            self.connection.commit()

        except sqlite3.Error as er:

            print("insert error", er)


    def get_table(self):
        query = "SELECT rowId, RecordHolder,Country,NumofCatches  FROM ChainsawJuggling"
        try:
            self.cursor.execute(query)

            return self.cursor.fetchall()

        except sqlite3.Error as er:
            print("From Get_table ",er )


#delete
    #create
    def delete_query(self, id):
        query = "DELETE FROM ChainsawJuggling WHERE rowid = ?"
        self.delete(query,id)
    #exacute  (with try expect)
    def delete(self, query, data):
        try:
            self.cursor.execute(query, (data,))
            self.connection.commit()
        except sqlite3.Error as er:
            print("Delete error", er)


#update
    #create query
    def update_prepare(self, new_data):
        query = "UPDATE ChainsawJuggling SET RecordHolder  = ?, Country = ?, NumofCatches = ? WHERE rowid = ?"
        self.update(query, new_data)
    # exacute update (with try expect)
    def update(self, query, data):
        try:
            self.cursor.execute(query, (data[1], data[2], data[3], data[0]))
            self.connection.commit()

        except sqlite3.Error as er:
            print("update error", er)


# search by column
    def find(self, search, column):
        query = "SELECT * FROM ChainsawJuggling WHERE "+ str(column)+" LIKE ?"
        return self.select(query, search)
    #
    def select(self, query, search):
        try:
            #print(query, ('%' + str(search) + '%',))
            self.cursor.execute(query, ('%' + str(search) + '%',))

            return self.cursor.fetchall()

        except sqlite3.Error as er:
            print('Select Error', er)

# exit
    def close_connection(self):
        self.connection.close()



