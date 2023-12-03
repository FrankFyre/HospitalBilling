import mysql.connector


class ConnectDB:

    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        # This ensure, whenever an object is created using "with"
        # this magic method is called, where you can create the connection.
        self.connection = mysql.connector.connect(host ='localhost', user ='root', password ='lichking', database ='dvdstore_new')
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exception_type, exception_val, trace):
        # once the with block is over, the __exit__ method would be called
        # with that, you can save and close
        try:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()

        except AttributeError:  # isn't closable
            print("Not closable.")

            return True  #

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        records = self.cursor.fetchall()
        return records

    def save_execute_sql(self, sql):
        self.cursor.execute(sql)

