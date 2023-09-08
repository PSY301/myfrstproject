import streamlit as st
import sqlite3
import os

name = st.text_input("username", "")
password = st.text_input("password", "")
conn = sqlite3.connect(r'C:\Users\HP\pythonProject6\pyps.db')
cur = conn.cursor()
user = (name, password)

st.write(user)

cur.execute("SELECT * FROM pyps;")
st.write(cur.fetchall())

if st.button("sign up"):
    try:
        cur.execute("INSERT INTO pyps VALUES(?, ?);", user)

        conn.commit()
        cur = conn.cursor()

        cur.execute("SELECT * FROM pyps;")
        st.write(cur.fetchall())
        st.success('Hi')
        os.system(r'streamlit run C:\Users\HP\pythonProject6\choose_an_option.py')

    except:
        st.write('try again')

elif st.button('sign in'):
    cur.execute("SELECT * FROM pyps;")

    if user in cur.fetchall():
        st.success('Hi')
        os.system(r'streamlit run C:\Users\HP\pythonProject6\choose_an_option.py')

    else:
        st.write("try again")
