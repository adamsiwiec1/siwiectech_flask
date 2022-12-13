from flask_user import roles_required, login_required
from flask import render_template, redirect, url_for, Blueprint

blueprint = Blueprint('student', __name__, template_folder='templates')


@blueprint.route('/student-profile')
@roles_required('student')
@login_required
def profile():
    return render_template('views/student/student-profile.html')

@blueprint.route('/student-courses')
@roles_required('student')
@login_required
def courses_page():
    return render_template('views/student/student-courses.html')


@blueprint.route('/student-assignments')
@roles_required('student')
@login_required
def assignments_page():
    return render_template('views/student/student-assignments.html')


@blueprint.route('/student-appointments')
@roles_required('student')
@login_required
def appointments_page():
    return render_template('views/student/student-appointments.html')


@blueprint.route('/student-calendar')
@roles_required('student')
@login_required
def calendar_page():
    return render_template('views/student/student-calendar.html')

@blueprint.route('/student-billing')
@roles_required('student')
def billing_page():
    return render_template('views/student/student-billing.html')