import psycopg2 as pg

conn = pg.connect(
    host="174.138.23.75",
    database="testing",
    user="postgres",
    password="cl0udplus!"
)

with conn.cursor() as cur:
    cur.execute("""SELECT * from Checkinouts c
    INNER JOIN Users u
        ON c.user_id = u.id
    WHERE u.id = (
        SELECT id from Users 
            WHERE name = 'user1'
    );""")
    result = cur.fetchall()

    print(result)