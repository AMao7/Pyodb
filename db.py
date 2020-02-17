import pyodbc
import time

# Look at our package for the documentation to connect our SPECIFIC database
# get the parameters it's looking for..
# Parameters of DB
server = 'localhost,1433'
databse = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
# Connection object of db
docker_nww_conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + databse + ';UID=' + username +
    ';PWD=' + password)

## this is our new connection object
# print(docker_nww_conn)

# # Create a cursor() object
new_cursor = docker_nww_conn.cursor()
#
# # Starting query
# Query = 'SELECT * FROM Products;'
# cursor.execute(Query)

# Get one row from the curosr
# row = cursor.fetchone   # cursor maintains state, selects the first row
# print(row)
# row = cursor.fetchone   # if i use fetchone() on the same cursor, it selects the second row :D
# print(row)

new_cursor = docker_nww_conn.cursor()
# new_cursor.execute('SELECT * FROM Customers')
# all_customer_rows = new_cursor.fetchall()   # bad practise to fetchall as it can crash servers
# print(all_customer_rows)
# for x in all_customer_rows:
#     print(x)
#     time.sleep(1)

# Better way to use fetchone()



rows2 = new_cursor.execute('SELECT * FROM Products')

while True:
    record = rows2.fetchone()
    if record == None:
        break
    print(record)

# print(rows2.fetchone())



