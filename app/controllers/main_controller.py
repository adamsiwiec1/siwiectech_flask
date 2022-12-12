from flask_user import roles_required, login_required, current_user
from flask import render_template, redirect, url_for, Blueprint, redirect, abort

main_blueprint = Blueprint('main', __name__, template_folder='templates')


@main_blueprint.route('/')
def home_page():
    return redirect(url_for('user.login'))


@main_blueprint.route('/login-redirect')
@login_required
def login_redirect():
    if current_user.has_roles("admin"):
        return redirect(url_for('main.admin_page'))
    if current_user.has_roles("client"):
        return redirect(url_for('main.client_page'))
    if current_user.has_roles("student"):
        return redirect(url_for('main.student_page'))
    abort(403)

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


@main_blueprint.route('/student')
@login_required
def student_page():
    return render_template('views/student/student_page.html')

@main_blueprint.route('/profile')
@login_required
def profile_page():
    if current_user.has_roles("student"):
        return redirect(url_for('student.profile'))
    if current_user.has_roles("client"):
        return redirect(url_for('client.profile'))
    abort(403)

@main_blueprint.route('/403')
@login_required
def error_403():
    return render_template('error/page-403.html')

@main_blueprint.route('/404')
@login_required
def error_404():
    return render_template('error/page-404.html')


@main_blueprint.route('/500')
@login_required
def error_500():
    return render_template('error/page-500.html')
