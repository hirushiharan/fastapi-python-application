import os

# Load environment variables
MSSQL_SERVER = os.getenv('MSSQL_SERVER')
MSSQL_USER = os.getenv('MSSQL_USER')
MSSQL_PASSWORD = os.getenv('MSSQL_PASSWORD')
MSSQL_PORT = os.getenv('MSSQL_PORT')
MSSQL_DB = os.getenv('MSSQL_DB')

# Construct the DATABASE_URL
DATABASE_URL = f"sqlserver://{MSSQL_USER}:{MSSQL_PASSWORD}@{MSSQL_SERVER}:{MSSQL_PORT}/{MSSQL_DB}"
