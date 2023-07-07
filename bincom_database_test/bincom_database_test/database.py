import mysql.connector

from bincom_database_test import bincom_database_test

# from bincom_test import database_config.py

# Replace the placeholders with your actual database connection details

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Abosede@1'
)

database_name = 'bincom_database_test'

# Create a cursor object to execute SQL statements
cursor = connection.cursor()

# Execute the CREATE DATABASE statement
cursor.execute(f'CREATE DATABASE {bincom_database_test}')

sql_file = 'path_to_your_sql_file.sql'

# Read the SQL file
with open(sql_file, 'r') as file:
    sql_script = file.read()

# Execute the SQL script
cursor.execute(sql_script)
# Commit the changes to make them persistent
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',  # or 'django.db.backends.sqlite3'
#         'NAME': 'bincom_test',
#         'USER': 'root',
#         'PASSWORD': 'Abosede@1',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }
