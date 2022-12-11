import psycopg2
import os
# from dotenv import load_dotenv
# load_dotenv()
QUERY="SELECT * from winners"
# print(os.environ.get('DATABASE_URL'))
# print(os.environ.get('DATABASE_NAME'))
# print(os.environ.get('DATABASE_USERNAME'))
# print(os.environ.get('DATABASE_PASSWORD'))
conn = psycopg2.connect(
    host=os.environ.get('DATABASE_URL'),
    database=os.environ.get('DATABASE_NAME'),
    user=os.environ.get('DATABASE_USERNAME'),
    password=os.environ.get('DATABASE_PASSWORD'))

cur = conn.cursor()
results = cur.execute(QUERY)
print(f"the results are here!\n{results}")
