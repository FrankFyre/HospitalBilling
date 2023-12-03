from connectdb import ConnectDB
from datetime import date

# get amount rented
def get_rented_copies(movie_id):
    with ConnectDB() as cursor:
        record = cursor.execute_sql(
            f"SELECT COUNT(*) FROM rented JOIN dvdcopies ON `rented`.`dvd id` = `dvdcopies`.`dvd id`"
            f" WHERE `dvdcopies`.`Movie ID` = '{movie_id}' ")
        # Query returns a tuple. so return the first value
        record = record[0]
        return record[0]


# Gets all movies in the database
def get_db_dvd():
    with ConnectDB() as cursor:
        records = cursor.execute_sql("SELECT * FROM movie ")
        return records


def get_db_customer():
    with ConnectDB() as cursor:
        records = cursor.execute_sql("SELECT * FROM customer ")
        return records


def db_custo_movie(value):
    with ConnectDB() as cursor:
        records = cursor.execute_sql(f"SELECT movie.* FROM movie JOIN dvdcopies ON `movie`.`Movie ID` = `dvdcopies`.`Movie ID` "
                       f"JOIN `rented` ON `dvdcopies`.`dvd id` = `rented`.`dvd id` "
                       f"WHERE `rented`.`account number` = '{value}'")
        return records


def get_movie_rental(value):
    with ConnectDB() as cursor:
        records = cursor.execute_sql(f"SELECT dvdcopies.*, `rented`.`account number`, `movie`.`movie name` "
                   f"FROM `dvdcopies` Left JOIN rented ON `dvdcopies`.`dvd id` = `rented`.`dvd id`"
                   f"LEFT JOIN movie ON `dvdcopies`.`Movie ID` = `movie`.`Movie ID`"
                   f"WHERE `dvdcopies`.`Movie ID` = '{value}'")

        return records


def sql_checkout(acct_no, dvd_id):
    today = date.today()
    with ConnectDB() as cursor:

        records = cursor.execute_sql(f'SELECT *'
                                     f'FROM `rented`'
                                     f'WHERE `dvd id` = "{dvd_id}"')
        if records is None:
            return False

        else:

            cursor.save_execute_sql(f"INSERT INTO rented (`dvd id`,`account number`,`checkout date`) "
                       f"VALUES ('{dvd_id}','{acct_no}','{today}')")
            return True


def sql_checkin(dvd_id):
    today = date.today()
    with ConnectDB() as cursor:
        records = cursor.execute_sql(f'SELECT *'
                                     f'FROM `rented`'
                                     f'WHERE `dvd id` = "{dvd_id}"')
        if not records:
            return False

        else:

            cursor.save_execute_sql(f"INSERT INTO `pasttransactions` (`transaction id`, `Account`, `dvd id`,`checkout date`,`checkin date`) "
                                    f"SELECT `rental id`, `Account Number`, `dvd id`, `checkout date`, '{today}' "
                                    f"FROM `rented`"
                                    f"WHERE `rented`.`dvd id` ='{dvd_id}';")

            cursor.save_execute_sql(f"DELETE FROM rented WHERE `dvd id` = '{dvd_id}'")
            return True


def sql_active_rentals_customer(account):
    with ConnectDB() as cursor:
        records = cursor.execute_sql(f"SELECT rented.*, `movie`.`movie name` "
                                     f"FROM rented  "
                                     f"JOIN dvdcopies ON `rented`.`dvd id` = `dvdcopies`.`dvd id` "
                                     f"JOIN movie ON `dvdcopies`.`Movie ID` = `movie`.`Movie ID`"
                                     f"WHERE `rented`.`Account Number` = '{account}';")
        return records

def get_list_rented_dvdid(account):
    with ConnectDB() as cursor:
        records = cursor.execute_sql(f"SELECT `dvd id` FROM rented WHERE Account_ID = [{account}];;")

        return records

def get_all_dvdid(movieid):
    with ConnectDB() as cursor:
        records = cursor.execute_sql(f"SELECT `dvd id` FROM dvdcopies WHERE `dvdcopies`.`Movie ID` = {movieid};")
        #returns list of tuple. Example [(2,),(3,).....]
        dvdid_list = [dvd[0] for dvd in records]
        return dvdid_list


def add_new_customer(first_name, last_name):
    with ConnectDB() as cursor:
        cursor.save_execute_sql(f" INSERT INTO `dvdstore_new`.`customer`(`First Name`, `Last Name`) "
                                f"VALUES('{first_name}','{last_name}');")

        records = cursor.execute_sql(f'SELECT * FROM customer ORDER BY `Account Number` DESC LIMIT 1;')
        #Returns a single tuple
        return records[0]


def add_new_dvd(movie_name, list_stars_names, producer, director, production_company, total_copies):
    with ConnectDB() as cursor:
        cursor.save_execute_sql(f"INSERT INTO `dvdstore_new`.`movie` "
                                f"(`movie name`,`Stars name`,`Producer`,`Director`,`Production Company`,`Copies`)"
                                f"VALUES ('{movie_name}', '{list_stars_names}', '{producer}', '{director}', "
                                f"'{production_company}','{total_copies}');")
        records = cursor.execute_sql(f'SELECT * FROM movie ORDER BY `Movie ID` DESC LIMIT 1;')
        # Returns a single tuple
        return records[0]

def add_dvd_table(copies, movie_id):
    with ConnectDB() as cursor:
        for copy in range(copies):
            cursor.save_execute_sql(f"INSERT INTO `dvdstore_new`.`dvdcopies` (`Movie ID`)VALUES('{movie_id}');")

        records = cursor.execute_sql(f'SELECT `dvd id` FROM `dvdstore_new`.`dvdcopies`'
                                         f'WHERE `Movie ID` = {movie_id}')
        dvd_id =[]
        for dvd in records:
            dvd_id.append(dvd[0])
        return dvd_id

def each_dvd_rented():
    with ConnectDB() as cursor:
        records = cursor.execute_sql(
               f' SELECT  movie.`movie name`,  dvdcopies.`dvd id`, customer.`First Name`,'
               f' customer.`Last Name`, customer.`Account Number` '     
               f' FROM dvdcopies'     
               f' JOIN movie ON dvdcopies.`Movie ID` = movie.`Movie ID`'     
               f' JOIN rented ON dvdcopies.`dvd id` = rented.`dvd id`'     
               f' JOIN customer ON rented.`Account Number` = customer.`Account Number`'     
               f' ORDER BY dvdcopies.`dvd id` ASC;' )
        return records
