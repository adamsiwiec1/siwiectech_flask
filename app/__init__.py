import datetime
from flask import Flask, request, render_template
from flask_babelex import Babel
from flask_sqlalchemy import SQLAlchemy
from flask_user import current_user, login_required, roles_required, UserMixin, UserManager
from app.controllers.main_controller import main_blueprint
from app.controllers.client_controller import client_blueprint
from app.settings import ConfigClass
from app.database.db_initializer import initialize_db
from wtforms import validators

app = Flask(__name__)
db = SQLAlchemy(app)

def register_blueprints(app):
    app.register_blueprint(main_blueprint)
    app.register_blueprint(client_blueprint)

def define_error_handlers(app):
    @app.errorhandler(403)
    def access_forbidden(error):
        return render_template('error/page-403.html'), 403


    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('error/page-404.html'), 404


    @app.errorhandler(500)
    def internal_error(error):
        return render_template('error/page-500.html'), 500

def create_app():
    #  create all db tab;es
    babel = Babel(app)
    app.config.from_object(ConfigClass)
    from app.models.user_model import User, Role
    register_blueprints(app)
    define_error_handlers(app)
    from app.models.custom_form_models import CustomUserManager
    user_manager = CustomUserManager(app, db, User)
    #  initialize users
    from app.models.project_model import Project, Deliverable, Task, Incident
    initialize_db(db, user_manager, User, Role, Project, Deliverable, Task, Incident)
    return app, db





# Start development web server
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
