import streamlit as st

userdata = {}

st.title("User authentication service")

st.subheader("Register a new user")
new_username = st.text_input("Username:")
new_password = st.text_input("Password, type="password")


if st.button("Register"):
  if new_username and new_password:
    if new_usernmae in user_data:
      st.error("Username already exists.")
    else:
      user_data[new_username] = new_password
      st.success("User is now registered")

st.subheader("Login")
username = st.text_input("Username:")
password = st.text_input("Password:", type="password")

if st.button("Login"):
  if username in user_data and user_data[username] == password:
    st.success("Logged in")
  else:
    st.error("Authentication denied")
  
