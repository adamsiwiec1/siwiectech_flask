from flask_user import roles_required, login_required
from flask import render_template, Blueprint
from siwiectech.models import user as user_model

blueprint = Blueprint('admin', __name__, template_folder='templates')


@blueprint.route('/admin/create-user')
@roles_required('admin')
@login_required
def create_user():    
    return render_template('views/admin/create-user.html')


@blueprint.route('/admin/manage-users')
@roles_required('admin')
@login_required
def manage_users():    
    users = user_model.User.query.all()
    return render_template('views/admin/manage-users.html', data=users)


@blueprint.route('/admin/manage-deliverables')
@roles_required('admin')
@login_required
def manage_client_projects():
    return render_template('views/admin/manage-deliverables.html')

@blueprint.route('/admin/accounting')
@roles_required('admin')
@login_required
def manage_billing():
    return render_template('views/admin/manage-billing.html')