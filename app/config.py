import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
MSSQL_SERVER = os.getenv('MSSQL_SERVER')
MSSQL_USER = os.getenv('MSSQL_USER')
MSSQL_PASSWORD = os.getenv('MSSQL_PASSWORD')
MSSQL_PORT = os.getenv('MSSQL_PORT')
MSSQL_DB = os.getenv('MSSQL_DB')

# Construct the DATABASE_URL
DATABASE_URL = f"sqlserver://{MSSQL_USER}:{MSSQL_PASSWORD}@{MSSQL_SERVER}:{MSSQL_PORT}/{MSSQL_DB}"

# Secret key for JWT encoding and decoding
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")