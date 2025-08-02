# models.py

class User:
    def __init__(self, user_id, name, email, age, role='User'):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.age = age
        self.role = role

    def __str__(self):
        return f"User({self.name}, {self.email}, {self.role})"


class Book:
    def __init__(self, book_id, title, author, genre, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available

    def mark_as_borrowed(self):
        self.available = False

    def mark_as_returned(self):
        self.available = True

    def __str__(self):
        status = 'Available' if self.available else 'Borrowed'
        return f"Book({self.title} by {self.author}, {status})"


class BorrowRecord:
    def __init__(self, record_id, user_id, book_id, borrow_date, return_date=None):
        self.record_id = record_id
        self.user_id = user_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.return_date = return_date

    def __str__(self):
        return f"BorrowRecord(User ID: {self.user_id}, Book ID: {self.book_id}, Borrowed: {self.borrow_date}, Returned: {self.return_date})"
