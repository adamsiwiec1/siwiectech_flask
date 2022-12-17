from flask_user import roles_required, login_required
from flask import render_template, Blueprint
from siwiectech.models import user as user_model

blueprint = Blueprint('consultant', __name__, template_folder='templates')

@blueprint.route('/consultant/invite-user')
@roles_required('consultant')
@login_required
def invite_user():    
    return render_template('views/consultant/invite-user.html')

@blueprint.route('/manage-clients')
@roles_required('consultant')
@login_required
def manage_clients():    
    clients = user_model.Client.query.all()
    return render_template('views/consultant/manage-clients.html', data=clients)

@blueprint.route('/manage-deliverables')
@roles_required('consultant')
@login_required
def manage_client_projects():
    return render_template('views/consultant/manage-deliverables.html')


@blueprint.route('/manage-students')
@roles_required('consultant')
@login_required
def manage_students():
    return render_template('views/consultant/manage-students.html')

@blueprint.route('/manage-student-apointments')
@roles_required('consultant')
@login_required
def manage_student_apointments():
    return render_template('views/consultant/manage-student-apointments.html')

@blueprint.route('/manage-calendar')
@roles_required('consultant')
@login_required
def manage_calendar():
    return render_template('views/consultant/manage-calendar.html')

@blueprint.route('/manage-billing')
@roles_required('consultant')
@login_required
def manage_billing():
    return render_template('views/shared/payment.html')

@blueprint.route('/manage-servers')
@roles_required('consultant')
@login_required
def manage_servers():
    return render_template('views/consultant/manage-servers.html')