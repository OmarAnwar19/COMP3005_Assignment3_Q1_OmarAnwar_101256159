from flask import render_template, Blueprint, request, redirect, url_for, flash
from database.queries import * # import all functions from the queries module

# create a new blueprint for the main view
main_view = Blueprint("main_view", __name__)


# create a route for the home page
@main_view.route("/home")
def home():
    # get all students from the database
    raw_students = get_all_students()   
    # create a list of dictionaries with the student information to pass to the template 
    students = [
        {
            "id": id, 
            "name": f"{first_name} {last_name}",
            "email": email,
            "enrollment_date": date.strftime("%B %d, %Y")
        } 
        for (id, first_name, last_name, email, date) in raw_students
    ]
    # render the home template and pass the students list to the template
    return render_template("home.html", students=students)


# create a route for the addStudent form and handle the form submission
@main_view.route('/addStudent', methods=['POST'])
def add_student_handler():
    # get the form data from the request (first_name, last_name, email, enrollment_date)
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    enrollment_date = request.form.get('enrollment_date')

    # check if a student with the same email already exists
    if student_email_exists(email):
        # if a student with the same email exists, flash a message and redirect to the home page
        flash("A student with this email already exists.", "danger")
    else:
        # if the email is unique, add the student to the database and flash a success message
        add_student(first_name, last_name, email, enrollment_date)
        flash("Student added successfully!", "success")
    # then redirect to the home page
    return redirect(url_for('main_view.home'))


# create a route for the editStudent form and handle the form submission
@main_view.route('/editStudent/<int:student_id>', methods=['GET', 'POST'])
def edit_student_handler(student_id):
    # if the form is submitted handle the form data
    if request.method == 'POST':
        # get the email from the form data
        email = request.form.get('email')
        # if the delete button was clicked, delete the student and flash a success message
        if 'delete' in request.form:
            delete_student(student_id)
            flash("Student deleted successfully!", "success")
        # otherwise, the email was updated, so check if the new email already exists
        else:
            # if the email already exists, flash a message and redirect to the editStudent page
            if student_email_exists(email):
                flash("A student with this email already exists.", "danger")
                # redirect to the editStudent page with the student_id as a URL parameter
                return redirect(url_for('main_view.edit_student_handler', student_id=student_id))
            else:
                # if the email is unique, update the student's email and flash a success message
                update_student_email(student_id, email)
                flash("Student updated successfully!", "success")
        # redirect to the home page
        return redirect(url_for('main_view.home'))
    # if the form is not submitted, then the user has just clicked the edit button for a student
    else:
        # get the student from the database by the student_id
        raw_student = get_student_by_id(student_id)
        # and create a dictionary with the student information to pass to the template
        student = {
            "id": raw_student[0], 
            "name": f"{raw_student[1]} {raw_student[2]}",
            "email": raw_student[3],
            "enrollment_date": raw_student[4].strftime("%B %d, %Y")
        }
        # render the edit_student template and pass the student
        return render_template('edit_student.html', student=student)