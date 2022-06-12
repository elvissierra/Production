from mysql.connector import connect, Error



try:
    with connect(
        host="localhost",
        user="root",
        password="Mysqlwizard",
        database = "productionDB",
    ) as connection:
        print("Connection to productionDB was successful")
except Error as err:
    print(err)