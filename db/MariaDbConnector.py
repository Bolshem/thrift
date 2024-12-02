import os
import mariadb
import sys


ip = os.environ['DB_IP_ADDRESS']
port = os.environ['DB_PORT']
user = os.environ['DB_USER']
password = os.environ['DB_PASSWORD']
database = os.environ['DB_DATABASE']
table_name = os.environ['DB_TABLE']

params = {
    ip,
    port,
    user,
    password,
    database,
    table_name
}

# check that all parameters are set
for param in params:
    if param is None:
        print("Missing environment variable {}".format(param))
        sys.exit(1)

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user=user,
        password=password,
        host=ip,
        port=int(port),
        database=database
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

def connect():
    return conn


