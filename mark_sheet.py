import pyodbc
import streamlit as st

connection_string = r"DRIVER={SQL Server};SERVER=.\SQLEXPRESS01;DATABASE=dbo_Marksheet;Trusted_connection=yes"
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

st.title("Student Mark Sheet")

Name = st.text_input("Name: ")
Id_Number = st.text_input("Id_number: ")
Math = st.text_input("Math: ")
English = st.text_input("English: ")
Science = st.text_input("Science: ")

if st.button("Submit Marks"):
    cursor.execute(R"INSERT INTO dbo.Mark_sheet (Name, Id_Number, Math, English, Science) VALUES (?, ?, ?, ?, ?)", (Name, Id_Number, Math, English, Science))

    connection.commit()
    st.success("The data is transferred")
