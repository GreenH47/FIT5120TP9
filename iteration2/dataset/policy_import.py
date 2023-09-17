import pandas as pd
import mysql.connector

# Database credentials
root_username = 'greenh47'
root_password = 'RRCgwXAfWw53cej'

# Database credentials
host = 'carbonvic.clx2a8hznypy.us-east-1.rds.amazonaws.com'
port = 3306
database = 'council'

username = root_username
password = root_password


# CSV file path
csv_file = 'waste_policy_waste.csv'

# Connect to the database
connection = mysql.connector.connect(
    host=host, port=port, database=database,
    user=username, password=password
)

# Create a cursor to execute SQL queries
cursor = connection.cursor()

# Read the CSV file into a Pandas DataFrame
data = pd.read_csv(csv_file)

print("connection established and data read")

council_name = ""
# Iterate over the rows in the DataFrame
for index, row in data.iterrows():
    waste_type = row['waste_type']

    # Iterate over the columns (except the first one, which is waste_type)
    for column in data.columns[1:]:
        council_name = column
        waste_policy = row[column]

        # Insert the record into the Policy table
        query = "INSERT INTO Policy (waste_type, council_name, waste_policy) VALUES (%s, %s, %s)"
        values = (waste_type, council_name, waste_policy)
        # print("SQL Query: ", query)
        # print("Query Values: ", values)

        cursor.execute(query, values)

#print("Inserted for " + council_name)

# Commit the changes to the database
connection.commit()

print("Changes committed")

# Close the cursor and connection
cursor.close()
connection.close()
