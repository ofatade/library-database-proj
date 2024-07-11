import mysql.connector
from book import BookManager
from user import UserManager
import re

# Database configuration
db_config = {
    'user': 'root',
    'password': 'Olamide/1',
    'host': 'localhost',
    'database': 'library_db'
}

def main():
    book_manager = BookManager(db_config)
    user_manager = UserManager(db_config)

    while True:
        print('''
Welcome to the Library Management System!

Main Menu:
1. Book Operations
2. User Operations
3. Quit
''')
        choice = input("Enter your choice: ")
        
        if choice == '1':
            book_operations(book_manager)
        elif choice == '2':
            user_operations(user_manager)
        elif choice == '3':
            print("Quitting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def book_operations(book_manager):
    while True:
        print('''
Book Operations:
1. Add a new book
2. Borrow a book
3. Return a book
4. Search for a book
5. Display all books
6. Back to Main Menu
''')
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            publication_date = input("Enter publication date (YYYY-MM-DD): ")
            book_manager.add_book(title, author, genre, publication_date)
        elif choice == '2':
            book_id = int(input("Enter book ID to borrow: "))
            user_id = int(input("Enter user ID: "))
            book_manager.borrow_book(book_id, user_id)
        elif choice == '3':
            book_id = int(input("Enter book ID to return: "))
            user_id = int(input("Enter user ID: "))
            book_manager.return_book(book_id, user_id)
        elif choice == '4':
            title = input("Enter book title to search: ")
            book_manager.search_book(title)
        elif choice == '5':
            book_manager.display_all_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

def user_operations(user_manager):
    while True:
        print('''
User Operations:
1. Add a new user
2. View user details
3. Display all users
4. Back to Main Menu
''')
        choice = input("Enter your choice: ")
        
        if choice == '1':
            user_name = input("Enter user name: ")
            email = input("Enter user email: ")
            if re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
                user_manager.add_user(user_name, email)
            else:
                print("Invalid email format.")
        elif choice == '2':
            user_id = int(input("Enter user ID to view: "))
            user_manager.view_user_details(user_id)
        elif choice == '3':
            user_manager.display_all_users()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
