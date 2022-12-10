from flask_user import roles_required, login_required, current_user
from flask import render_template, redirect, url_for, Blueprint, redirect
main_blueprint = Blueprint('main', __name__, template_folder='templates')


@main_blueprint.route('/')
def home_page():
    return redirect(url_for('user.login'))


@main_blueprint.route('/login-redirect')
@login_required
def login_redirect():
    if current_user.has_roles("admin"):
        return redirect(url_for('main.admin_page'))
    return redirect(url_for('main.client_page'))

@main_blueprint.route('/confirmation')
def confirmation_page():
    return render_template('views/shared/confirmation.html')

@main_blueprint.route('/admin')
@roles_required('admin')    
def admin_page():
    return render_template('views/admin/admin_page.html')
    
    
@main_blueprint.route('/client')
@login_required
def client_page():
    return render_template('views/client/client_page.html')


@main_blueprint.route('/profile')
@roles_required('admin')
def profile_page():
    return render_template('views/shared/profile.html')


@main_blueprint.route('/unauthorized-error')
def error_403():
    return render_template('error/page-403.html')

@main_blueprint.route('/not-found-error')
def error_404():
    return render_template('error/page-404.html')

@main_blueprint.route('/unknown-error')
def error_500():
    return render_template('error/page-500.html')