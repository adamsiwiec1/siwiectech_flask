from flask_user import roles_required, login_required
from flask import render_template, Blueprint

admin_blueprint = Blueprint('admin', __name__, template_folder='templates')


@admin_blueprint.route('/manage-clients')
@roles_required('admin')
@login_required
def manage_clients():
    return render_template('views/admin/manage-clients.html')


@admin_blueprint.route('/manage-deliverables')
@roles_required('admin')
@login_required
def manage_client_projects():
    return render_template('views/admin/manage-deliverables.html')


@admin_blueprint.route('/manage-client-calendar')
@roles_required('admin')
@login_required
def manage_client_calendar():
    return render_template('views/admin/manage-client-calendar.html')


@admin_blueprint.route('/manage-students')
@roles_required('admin')
@login_required
def manage_students():
    return render_template('views/admin/manage-students.html')


@admin_blueprint.route('/manage-student-apointments')
@roles_required('admin')
@login_required
def manage_student_apointments():
    return render_template('views/admin/manage-student-apointments.html')

@admin_blueprint.route('/manage-student-calendar')
@roles_required('admin')
@login_required
def manage_student_calendar():
    return render_template('views/admin/manage-student-calendar.html')

@admin_blueprint.route('/manage-billing')
@roles_required('admin')
@login_required
def manage_billing():
    return render_template('views/admin/manage-billing.html')

@admin_blueprint.route('/manage-servers')
@roles_required('admin')
@login_required
def manage_servers():
    return render_template('views/admin/manage-servers.html')