from flask import render_template, Blueprint, request, redirect, url_for, flash
from database.queries import *

main_view = Blueprint("main_view", __name__)


@main_view.route("/home")
def home():
    raw_students = get_all_students()    
    students = [
        {
            "id": id, 
            "name": f"{first_name} {last_name}",
            "email": email,
            "enrollment_date": date.strftime("%B %d, %Y")
        } 
        for (id, first_name, last_name, email, date) in raw_students
    ]
    return render_template("home.html", students=students)


@main_view.route('/addStudent', methods=['POST'])
def add_student_handler():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    enrollment_date = request.form.get('enrollment_date')

    if student_email_exists(email):
        flash("A student with this email already exists.", "danger")
    else:
        add_student(first_name, last_name, email, enrollment_date)
        flash("Student added successfully!", "success")
    return redirect(url_for('main_view.home'))


@main_view.route('/editStudent/<int:student_id>', methods=['GET', 'POST'])
def edit_student_handler(student_id):
    if request.method == 'POST':
        email = request.form.get('email')
        if 'delete' in request.form:
            delete_student_row(student_id)
            flash("Student deleted successfully!", "success")
        else:
            if student_email_exists(email):
                flash("A student with this email already exists.", "danger")
                return redirect(url_for('main_view.edit_student_handler', student_id=student_id))
            else:
                update_student_email(student_id, email)
                flash("Student updated successfully!", "success")
        return redirect(url_for('main_view.home'))
    else:
        raw_student = get_student_by_id(student_id)
        student = {
            "id": raw_student[0], 
            "name": f"{raw_student[1]} {raw_student[2]}",
            "email": raw_student[3],
            "enrollment_date": raw_student[4].strftime("%B %d, %Y")
        }
        return render_template('edit_student.html', student=student)