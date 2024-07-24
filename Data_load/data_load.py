import pandas as pd
from sqlalchemy import create_engine
import urllib.parse

password = 'vinod@123'
encoded_password = urllib.parse.quote(password)
print(encoded_password)
import sys
print(sys.version)
conn_string = f'postgresql://postgres:{encoded_password}@localhost:5432/painting'
db = create_engine(conn_string)
conn = db.connect()

