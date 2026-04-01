from database.connection import get_connection

class UserDALC:

    @staticmethod
    def get_by_username(username:str):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username = %s",
            (username,)
        )
        
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        return user
    