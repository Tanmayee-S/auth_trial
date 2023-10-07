import streamlit as st
import sqlite3
import hashlib

conn = sqlite3.connect('user.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)''')
conn.commit()

st.title("User Authentication Service")

if st.button("Register"):
    st.subheader("Register a new user")
    new_username = st.text_input("Username:")
    new_password = st.text_input("Password:", type = "password")

    if new_username and new_password:
        create_user(new_username, new_password)

if st.button("Login"):
    st.subheader("Login")
    username = st.text_input("Username:")
    password = st.text_input("Password:", type = "password")
    
    if username and password:
        if authenticate_user(username,password):
            st.success("Log in successful")
        else:
            st.error("Authentication Denied")

    
