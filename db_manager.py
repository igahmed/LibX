import sqlite3
from threading import Lock

class DataBaseManager:
    _instance = None
    _lock = Lock()  # For thread safety

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(DataBaseManager, cls).__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self, db_path='library.db'):
        if self._initialized:
            return  # Skip re-initializing if already initialized
        self.connect = sqlite3.connect(db_path)
        self.cursor = self.connect.cursor()
        self._initialized = True

    # Add user to the database
    def add_user(self, name, email, password, age, role="User"):
        try:
            self.cursor.execute("""
                INSERT INTO users (name, email, password, age, role)
                VALUES (?, ?, ?, ?, ?)
            """, (name, email, password, age, role))
            self.connect.commit()
            return True
        except sqlite3.IntegrityError:
            return False  # Email already exists

    # Add book to the database
    def add_book(self, title, author, genre):
        self.cursor.execute("""
            INSERT INTO books (title, author, genre, available)
            VALUES (?, ?, ?, 1)
        """, (title, author, genre))
        self.connect.commit()

    # Borrow a book
    def borrow_book(self, user_id, book_id, borrow_date):
        self.cursor.execute("SELECT available FROM books WHERE id=?", (book_id,))
        result = self.cursor.fetchone()

        if not result or result[0] == 0:
            return False  # Book not available

        # Record borrowing and mark book unavailable
        self.cursor.execute("""
            INSERT INTO borrow_records (user_id, book_id, borrow_date)
            VALUES (?, ?, ?)
        """, (user_id, book_id, borrow_date))
        self.cursor.execute("UPDATE books SET available=0 WHERE id=?", (book_id,))
        self.connect.commit()
        return True

    # Return a borrowed book
    def return_book(self, record_id, return_date):
        self.cursor.execute("""
            UPDATE borrow_records SET return_date=? WHERE id=?
        """, (return_date, record_id))

        self.cursor.execute("""
            SELECT book_id FROM borrow_records WHERE id=?
        """, (record_id,))
        book_id = self.cursor.fetchone()

        if book_id:
            self.cursor.execute("UPDATE books SET available=1 WHERE id=?", (book_id[0],))
            self.connect.commit()
            return True
        return False

    # Fetch user by email
    def get_user_by_email(self, email):
        self.cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        return self.cursor.fetchone()

    # Fetch all books
    def get_all_books(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

    # Fetch borrowing history of a user
    def get_borrow_records_by_user(self, user_id):
        self.cursor.execute("SELECT * FROM borrow_records WHERE user_id=?", (user_id,))
        return self.cursor.fetchall()

    # Close database connection
    def close(self):
        self.connect.close()
