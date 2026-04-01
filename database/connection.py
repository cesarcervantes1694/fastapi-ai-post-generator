# Ejemplo conectarte a SUPABASE
import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    conn = psycopg2.connect(
        host="db.slnfqachxgkfajhjduyl.supabase.co",
        database="postgres",
        user="postgres",
        password="",
        port="5432",
        cursor_factory=RealDictCursor
    )

    return conn

