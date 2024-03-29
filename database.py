import urllib
from sqlalchemy import create_engine
import pandas as pd
import getpass

server   = 'budget-app.database.windows.net'
database = 'TestDB'
username = 'Augusto'
password = getpass.getpass("Enter password:\n")
driver   = '{ODBC Driver 18 for SQL Server}'

conn = f"""Driver={driver};Server=tcp:{server},1433;Database={database};
Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"""

params = urllib.parse.quote_plus(conn)
conn_str = 'mssql+pyodbc:///?autocommit=true&odbc_connect={}'.format(params)
engine = create_engine(conn_str, echo=True)
