import mysql.connector
from datetime import date

class BookManager:
    def __init__(self, db_config):
        self.conn = mysql.connector.connect(**db_config)
        self.cursor = self.conn.cursor()

    def add_book(self, title, author, genre, publication_date):
        query = "INSERT INTO books (title, author, genre, publication_date) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (title, author, genre, publication_date))
        self.conn.commit()
        print(f"Book '{title}' added successfully.")

    def borrow_book(self, book_id, user_id):
        query = "SELECT availability FROM books WHERE id = %s"
        self.cursor.execute(query, (book_id,))
        result = self.cursor.fetchone()
        if result and result[0]:
            borrow_query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)"
            self.cursor.execute(borrow_query, (user_id, book_id, date.today()))
            update_query = "UPDATE books SET availability = 0 WHERE id = %s"
            self.cursor.execute(update_query, (book_id,))
            self.conn.commit()
            print(f"Book with ID {book_id} borrowed successfully.")
        else:
            print("The book is already borrowed or not found.")

    def return_book(self, book_id, user_id):
        return_query = "UPDATE borrowed_books SET return_date = %s WHERE book_id = %s AND user_id = %s AND return_date IS NULL"
        self.cursor.execute(return_query, (date.today(), book_id, user_id))
        if self.cursor.rowcount > 0:
            update_query = "UPDATE books SET availability = 1 WHERE id = %s"
            self.cursor.execute(update_query, (book_id,))
            self.conn.commit()
            print(f"Book with ID {book_id} returned successfully.")
        else:
            print("No borrowed record found for this book and user.")

    def search_book(self, title):
        query = "SELECT * FROM books WHERE title LIKE %s"
        self.cursor.execute(query, (f"%{title}%",))
        books = self.cursor.fetchall()
        for book in books:
            print(book)

    def display_all_books(self):
        query = "SELECT * FROM books"
        self.cursor.execute(query)
        books = self.cursor.fetchall()
        for book in books:
            print(book)

    def __del__(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
