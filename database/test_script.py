import psycopg2 as pg

conn = pg.connect(
    host="174.138.23.75",
    database="testing",
    user="postgres",
    password="cl0udplus!"
)

with conn.cursor() as cur:
    cur.execute("SELECT * FROM users")
    result = cur.fetchall()

    print(result)