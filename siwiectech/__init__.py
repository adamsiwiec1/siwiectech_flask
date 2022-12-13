# import datetime
# from flask import Flask, request, render_template
# from flask_babelex import Babel
# from flask_sqlalchemy import SQLAlchemy
# from flask_user import current_user, login_required, roles_required, UserMixin, UserManager
# from siwiectech.controllers.main import main_blueprint
# from siwiectech.controllers.client import client_blueprint
# from siwiectech.controllers.admin import admin_blueprint
# from siwiectech.controllers.student import student_blueprint
# from siwiectech.settings import ConfigClass

# app = Flask(__name__)
# db = SQLAlchemy(app)

# # def register_blueprints(app):
# #     app.register_blueprint(main_blueprint)
# #     app.register_blueprint(client_blueprint)
# #     app.register_blueprint(admin_blueprint)
# #     app.register_blueprint(student_blueprint)


# # def define_error_handlers(app):
# #     @app.errorhandler(403)
# #     def access_forbidden(error):
# #         return render_template('error/page-403.html'), 403


# #     @app.errorhandler(404)
# #     def not_found_error(error):
# #         return render_template('error/page-404.html'), 404


# #     @app.errorhandler(500)
# #     def internal_error(error):
# #         return render_template('error/page-500.html'), 500

# def create_app():
#     from siwiectech.database.db_initializer import initialize_db
#     #  create all db tab;es
#     babel = Babel(app)
#     app.config.from_object(ConfigClass)
#     from siwiectech.models.user_model import User, Role, UserInvitation
#     register_blueprints(app)
#     define_error_handlers(app)
#     from siwiectech.models.custom_form_models import CustomUserManager
#     user_manager = CustomUserManager(app, db, User, UserInvitationClass=UserInvitation)
#     #  initialize users
#     from siwiectech.models.project_model import Project, Deliverable, Task, Incident
#     initialize_db(db, user_manager, User, Role, Project, Deliverable, Task, Incident)
#     return app, db