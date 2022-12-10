from flask_user import roles_required, login_required
from flask import render_template, redirect, url_for, Blueprint

client_blueprint = Blueprint('client', __name__, template_folder='templates')



@client_blueprint.route('/projects')
@login_required
def projects_page():
    return render_template('views/client/projects.html')


@client_blueprint.route('/tasks')
@login_required
def tasks_page():
    return render_template('views/client/tasks.html')


@client_blueprint.route('/incidents')
@login_required
def incidents_page():
    return render_template('views/client/incidents.html')


@client_blueprint.route('/payment')
@login_required
def payment_page():
    return render_template('views/client/payment.html')


@client_blueprint.route('/servers')
@login_required
def servers_page():
    return render_template('views/client/servers.html')