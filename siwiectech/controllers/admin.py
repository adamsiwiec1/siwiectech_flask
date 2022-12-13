from flask_user import roles_required, login_required
from flask import render_template, Blueprint
from siwiectech.models import user as user_model

blueprint = Blueprint('admin', __name__, template_folder='templates')


@blueprint.route('/manage-clients')
@roles_required('admin')
@login_required
def manage_clients():    
    users = user_model.User.query.all()
    return render_template('views/admin/manage-clients.html', data=users)


@blueprint.route('/manage-deliverables')
@roles_required('admin')
@login_required
def manage_client_projects():
    return render_template('views/admin/manage-deliverables.html')


@blueprint.route('/manage-students')
@roles_required('admin')
@login_required
def manage_students():
    return render_template('views/admin/manage-students.html')


@blueprint.route('/manage-student-apointments')
@roles_required('admin')
@login_required
def manage_student_apointments():
    return render_template('views/admin/manage-student-apointments.html')

@blueprint.route('/manage-calendar')
@roles_required('admin')
@login_required
def manage_calendar():
    return render_template('views/admin/manage-calendar.html')

@blueprint.route('/manage-billing')
@roles_required('admin')
@login_required
def manage_billing():
    return render_template('views/shared/payment.html')

@blueprint.route('/manage-servers')
@roles_required('admin')
@login_required
def manage_servers():
    return render_template('views/admin/manage-servers.html')