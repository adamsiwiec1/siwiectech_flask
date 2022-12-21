from flask_user import roles_required, login_required
from flask import render_template, Blueprint
from siwiectech.models import user as user_model

blueprint = Blueprint('consultant', __name__, template_folder='templates')

@blueprint.route('/consultant/invite-user')
@roles_required('consultant')
@login_required
def invite_user():    
    return render_template('views/consultant/invite-user.html')

@blueprint.route('/consultant/manage-clients')
@roles_required('consultant')
@login_required
def manage_clients():    
    clients = user_model.Client.query.all()
    return render_template('views/consultant/manage-clients.html', data=clients)

@blueprint.route('/consultant/manage-deliverables')
@roles_required('consultant')
@login_required
def manage_client_projects():
    return render_template('views/consultant/manage-deliverables.html')


@blueprint.route('/consultant/manage-students')
@roles_required('consultant')
@login_required
def manage_students():
    return render_template('views/consultant/manage-students.html')

@blueprint.route('/consultant/manage-student-apointments')
@roles_required('consultant')
@login_required
def manage_student_apointments():
    return render_template('views/consultant/manage-student-apointments.html')

@blueprint.route('/consultant/manage-calendar')
@roles_required('consultant')
@login_required
def manage_calendar():
    return render_template('views/consultant/manage-calendar.html')

@blueprint.route('/consultant/manage-billing')
@roles_required('consultant')
@login_required
def manage_billing():
    return render_template('views/consultant/manage-billing.html')

@blueprint.route('/consultant/manage-servers')
@roles_required('consultant')
@login_required
def manage_servers():
    return render_template('views/consultant/manage-servers.html')