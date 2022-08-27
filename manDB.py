from sqlite3 import DatabaseError
import mysql.connector
import pickle


class dataBase:

    DATABSE_NAME="flask_proj"

    def __init__(self) -> None:
        self.db=dataBase.establishConncetion()
        self.coursor=self.db.cursor()
        self.databeseCRT()

    @property
    def db(self):
        return self.__db
    @db.setter
    def db(self,database):
        self.__db=database

    @staticmethod
    def establishConncetion():
        try:
            mydb = mysql.connector.connect(
            host="localhost",
            user="flask",
            password=""
            )
            return mydb
        except:
            raise DatabaseError("connection to databse has failed")

    #checking if db exist
    def databeseCRT(self):
        self.coursor.execute("SHOW DATABASES")
        existingDBs=list(self.coursor)

        if (dataBase.DATABSE_NAME,) not in existingDBs:
            with open("flask_proj_users.sql", encoding='utf8') as f:
                self.coursor.execute(f.read(),multi=True)
                # self.db.database=dataBase.DATABSE_NAME
            print(f"created {dataBase.DATABSE_NAME}")
        else:
            self.db.database=dataBase.DATABSE_NAME
            print(f"databse {dataBase.DATABSE_NAME} is connected")

    #CR (UD don't have a use in this project)
    def addUser(self,userName,passwordHash)->bool:
        try:
            self.coursor.execute("INSERT INTO `users` (userName,passwordHash) VALUES (%s,%s)",(userName,passwordHash,))
            self.db.commit()
            return True
        except:
            return False

    def getUser(self,userName):
        self.coursor.execute("SELECT * FROM `users` WHERE `userName`=(%s)",(userName,))
        return self.coursor.fetchone()
    
    def import_model(self, model_name):
        self.coursor.execute("SELECT * FROM `models` WHERE `model_name`=(%s)",(model_name,))
        return self.coursor.fetchone()[-1]
    
    def export_model(self, model_name, pickled):
        self.coursor.execute("INSERT INTO `models` (model_name,pickle) VALUES (%s,%s)",(model_name,pickled,))
        self.db.commit()
        

#TESTS
# b=dataBase()
# print(b.addUser("admin111","admin"))
# print(b.getUser("asfasfs"))