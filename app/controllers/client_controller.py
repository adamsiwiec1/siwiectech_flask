from flask_user import roles_required, login_required
from flask import render_template, redirect, url_for, Blueprint

client_blueprint = Blueprint('client', __name__, template_folder='templates')



@client_blueprint.route('/projects')
@roles_required('client')
@login_required
def projects_page():
    return render_template('views/client/projects.html')


@client_blueprint.route('/tasks')
@roles_required('client')
@login_required
def tasks_page():
    return render_template('views/client/tasks.html')


@client_blueprint.route('/incidents')
@roles_required('client')
@login_required
def incidents_page():
    return render_template('views/client/incidents.html')


@client_blueprint.route('/payment')
@roles_required('client')
@login_required
def payment_page():
    return render_template('views/client/client_billing.html')


@client_blueprint.route('/servers')
@roles_required('client')
@login_required
def servers_page():
    return render_template('views/client/servers.html')


@client_blueprint.route('/client-schedule-meeting')
@roles_required('client')
def schedule_meeting():
    return render_template('views/client/schedule-meeting.html')