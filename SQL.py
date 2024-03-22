import os

# Get the value of HBNB_ENV
env = os.environ.get('HBNB_ENV')
print("Running environment:", env)

# Get the MySQL username
mysql_user = os.environ.get('HBNB_MYSQL_USER')
print("MySQL username:", mysql_user)

# Get the MySQL password
mysql_password = os.environ.get('HBNB_MYSQL_PWD')
print("MySQL password:", mysql_password)

# Get the MySQL host
mysql_host = os.environ.get('HBNB_MYSQL_HOST')
print("MySQL host:", mysql_host)

# Get the MySQL database name
mysql_db = os.environ.get('HBNB_MYSQL_DB')
print("MySQL database:", mysql_db)

# Get the type of storage
storage_type = os.environ.get('HBNB_TYPE_STORAGE')
print("Storage type:", storage_type)

