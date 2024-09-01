import os
from sqlalchemy.engine import URL
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
MSSQL_SERVER = os.getenv('MSSQL_SERVER')
MSSQL_USER = os.getenv('MSSQL_USER')
MSSQL_PASSWORD = os.getenv('MSSQL_PASSWORD')
MSSQL_PORT = os.getenv('MSSQL_PORT')
MSSQL_DB = os.getenv('MSSQL_DB')

# Construct the DATABASE_URL
connection_string = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={MSSQL_SERVER};DATABASE={MSSQL_DB};UID={MSSQL_USER};PWD={MSSQL_PASSWORD};Encrypt=no"
DATABASE_URL = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

# Secret key for JWT encoding and decoding
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")