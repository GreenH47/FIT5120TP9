import pymysql

'''
this class is simple usage to test mysql connection
just change it with your account and password to login
'''
root_username = 'greenh47'
root_password = 'RRCgwXAfWw53cej'

# Database credentials
host = 'carbonvic.clx2a8hznypy.us-east-1.rds.amazonaws.com'
port = 3306
database = 'test'
# username = 'yuntao'
# password = 'MzA4NDA0MDNjNjkxOTVi'
username = root_username
password = root_password

try:
    # Connect to the database
    connection = pymysql.connect(host=host, port=port, database=database,
                                 user=username, password=password)

    # Create a cursor object
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM bill")

    # Fetch all rows from the result set
    rows = cursor.fetchall()
    for row in rows:
        print(row)  # Print each row

except pymysql.Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    # Close the connection
    if connection:
        connection.close()
