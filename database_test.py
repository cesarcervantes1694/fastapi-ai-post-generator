# Ejemplo conectarte a SUPABASE
import psycopg2

conn = psycopg2.connect(
    host="db.slnfqachxgkfajhjduyl.supabase.co",
    database="postgres",
    user="postgres",
    password="Comerpay1234!",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM Users;")
rows = cursor.fetchall()

print(rows)
