import streamlit as st
import sqlite3
import hashlib

conn = sqlite3.connect('user.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)''')
conn.commit()

def create_user(username, password):
    hased_password = hashlib.sha256(password.encode()).hexdigest()
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
    conn.commit()
    st.success("user created successfully!")

def authenticate_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, hashed_password))
    user = c.fetchone()
    if user:
        return True
    else:
        return False

st.title("User Authentication Service")

if st.button("Register"):
    st.subheader("Register a new user")
    new_username = st.text_input("Usernmae:")
    new_password = st.text_input("Password:", type = "password")

    if new_username and new_password:
        create_user(new_username, new_password)

if st.button("Login"):
    st.subheader("Login")
    username = st.text_input("Usernmae:")
    password = st.text_input("Password:", type = "password")
    
    if username and password:
        if authenticate_user(username,password):
            st.success("Log in successful")
        else:
            st.error("Authentication Denied")

    
