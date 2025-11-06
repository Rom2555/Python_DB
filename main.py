import psycopg2

conn = psycopg2.connect(database="netology_db", user="postgres", password="postgres")

with conn.cursor() as cur:
    cur.execute("CREATE TABLE test_1 (id serial PRIMARY KEY);")
    conn.rollback()

conn.close()