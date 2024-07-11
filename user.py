import mysql.connector

class UserManager:
    def __init__(self, db_config):
        self.conn = mysql.connector.connect(**db_config)
        self.cursor = self.conn.cursor()

    def add_user(self, user_name, email):
        query = "INSERT INTO users (user_name, email) VALUES (%s, %s)"
        self.cursor.execute(query, (user_name, email))
        self.conn.commit()
        print(f"User '{user_name}' added successfully.")

    def view_user_details(self, user_id):
        query = "SELECT * FROM users WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        user = self.cursor.fetchone()
        if user:
            print(user)
        else:
            print("User not found.")

    def display_all_users(self):
        query = "SELECT * FROM users"
        self.cursor.execute(query)
        users = self.cursor.fetchall()
        for user in users:
            print(user)

    def __del__(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
