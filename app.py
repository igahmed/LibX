import streamlit as st
from auth_manager import AuthManager
from models import Book

class LibraryApp:
    def __init__(self):
        self.auth_manager = AuthManager()

    def run(self):
        st.set_page_config(page_title="Library Management", layout="centered")
        st.title("📚 Welcome to Library")

        if 'logged_in' not in st.session_state:
            st.session_state.logged_in = False
        if 'current_user' not in st.session_state:
            st.session_state.current_user = None

        if st.session_state.logged_in:
            self.dashboard()
        else:
            menu = st.selectbox("Select Option", ["Login", "Sign Up"])
            if menu == "Login":
                self.login_section()
            elif menu == "Sign Up":
                self.signup_section()

    def login_section(self):
        st.subheader(" Login")
        username = st.text_input("Username")
        __password = st.text_input("Password", type="password")
        if st.button("Login"):
            # Replace with actual login logic
            self.auth_manager.login([username,__password])
            user = self.auth_manager.current_user
            if user:
                st.session_state.logged_in = True
                st.session_state.current_user = user
                st.experimental_rerun()

    def signup_section(self):
        st.subheader("📝 Sign Up")
        name = st.text_input("Name")
        email = st.text_input("Email")
        age = st.text_input("Age")
        password = st.text_input("Password", type="password")
        if st.button("Sign Up"):
            # Replace with actual signup logic
            user = type("User", (), {"name": name})  # Dummy user object
            if user:
                st.session_state.logged_in = True
                st.session_state.current_user = user
                st.experimental_rerun()
            else:
                st.write("User not found try again!")


    def dashboard(self):
        st.subheader("📘 Dashboard")
        st.success(f"Welcome, {st.session_state.current_user.name}!")
        st.write("Here are your books:")

        books = [
            Book(1, "1984", "George Orwell", "Dystopian"),
            Book(2, "To Kill a Mockingbird", "Harper Lee", "Classic"),
            Book(3, "The Great Gatsby", "F. Scott Fitzgerald", "Novel", available=False),
        ]

        book_data = [{
            "ID": book.book_id,
            "Title": book.title,
            "Author": book.author,
            "Genre": book.genre,
            "Status": "Available" if book.available else "Borrowed"
        } for book in books]

        st.table(book_data)


a = LibraryApp()
a.run()