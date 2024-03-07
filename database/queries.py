# import the connect function from the db.py file
from database.db import connect


# this is the query for Application Function 1
def get_all_students():
    # connect to the database
    conn = connect()
    cursor = conn.cursor()
    # execute the query to get all the students
    cursor.execute("SELECT * FROM students")
    # fetch all the students from the database
    students = cursor.fetchall()
    # close the cursor and the connection
    cursor.close()
    conn.close()
    # return the students list
    return students


# this is an additional query to get a student by their id 
def get_student_by_id(student_id):
    # the database connection and closing is the same for all functions
    conn = connect()
    cursor = conn.cursor()
    # execute the query to get the student by a given id
    cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
    student = cursor.fetchone()
    cursor.close()
    conn.close()
    return student


# this is an additional query to check if a student with a given email already exists
def student_email_exists(email):
    # the database connection and closing is the same for all functions
    conn = connect()
    cursor = conn.cursor()
    # execute the query to check if a student with a given email exists
    cursor.execute("SELECT * FROM students WHERE email = %s", (email,))
    student = cursor.fetchone()
    cursor.close()
    conn.close()
    return bool(student)


# this is the query for Application Function 2
def add_student(first_name, last_name, email, enrollment_date):
    # the database connection and closing is the same for all functions
    conn = connect()
    cursor = conn.cursor()
    # execute the query to add a student to the database with the given information
    cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
    conn.commit()
    cursor.close()
    conn.close()


# this is the query for Application Function 3
def update_student_email(student_id, new_email):
    # the database connection and closing is the same for all functions
    conn = connect()
    cursor = conn.cursor()
    # execute the query to update a student's email by their id with the new email
    cursor.execute("UPDATE students SET email = %s WHERE id = %s", (new_email, student_id))
    conn.commit()
    cursor.close()
    conn.close()


# this is the query for Application Function 4
def delete_student(student_id):
    # the database connection and closing is the same for all functions
    conn = connect()
    cursor = conn.cursor()
    # execute the query to delete a student by their id
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    cursor.close()
    conn.close()    