from database.db import connect


def get_all_students():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return students


def get_student_by_id(student_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
    student = cursor.fetchone()
    cursor.close()
    conn.close()
    return student


def student_email_exists(email):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE email = %s", (email,))
    student = cursor.fetchone()
    cursor.close()
    conn.close()
    return bool(student)


def add_student(first_name, last_name, email, enrollment_date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
    conn.commit()
    cursor.close()
    conn.close()


def update_student_email(student_id, new_email):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET email = %s WHERE id = %s", (new_email, student_id))
    conn.commit()
    cursor.close()
    conn.close()


def delete_student_row(student_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    cursor.close()
    conn.close()    