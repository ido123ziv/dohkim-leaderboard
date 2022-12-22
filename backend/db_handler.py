import psycopg2
import os

# from dotenv import load_dotenv
# load_dotenv()
QUERY = "SELECT * from winners"
INSERT = """INSERT into winners (winner_name) values ('ido')"""
conn = psycopg2.connect(
    host=os.environ.get('DATABASE_URL'),
    database=os.environ.get('DATABASE_NAME'),
    user=os.environ.get('DATABASE_USERNAME'),
    password=os.environ.get('DATABASE_PASSWORD'))


def get_data():
    cur = conn.cursor()
    results = cur.execute(QUERY)
    print(f"the results are here!\n{results}")
    return results


def update_data():
    cur = conn.cursor()
    result = cur.execute(INSERT)
    print("hurray!")
    return "Updated DB"
