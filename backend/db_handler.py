import psycopg2
import os

# from dotenv import load_dotenv
# load_dotenv()

# SQL Queries
QUERY = "SELECT * from winners"
INSERT = """INSERT into winners (winner_name) values ('ido')"""
conn = psycopg2.connect(
    host=os.environ.get('DATABASE_URL'),
    database=os.environ.get('DATABASE_NAME'),
    user=os.environ.get('DATABASE_USERNAME'),
    password=os.environ.get('DATABASE_PASSWORD'))

"""
returns all the data from winners table
"""
def get_data():
    cur = conn.cursor()
    cur.execute(QUERY)
    results = cur.fetchall()
    print(f"the results are here!\n{results}")
    return results

"""
adds another winner to db
"""
def update_data():
    cur = conn.cursor()
    cur.execute(INSERT)
    conn.commit()
    print("hurray!")
    return "Updated DB"
