import logging
import sys

from flask import Flask, render_template, request

from siwiectech import models, controllers, database
from siwiectech.extensions import (
    bcrypt,
    cache,
    csrf_protect,
    db,
    debug_toolbar,
    flask_static_digest,
    login_manager,
    migrate,
)


def create_app(config_object="siwiectech.settings.ConfigClass"):
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)
    db = register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_hooks(app)
    um = models.user
    user_manager = models.forms.CustomUserManager(app, db, um.User, UserInvitationClass=um.UserInvitation)
    database.db_initializer.initialize_db(app, db, user_manager, um, models.client, models.student)
    return app


def register_extensions(app):
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    csrf_protect.init_app(app)
    login_manager.init_app(app)
    debug_toolbar.init_app(app)
    migrate.init_app(app, db)
    flask_static_digest.init_app(app)
    return db


def register_blueprints(app):
    app.register_blueprint(controllers.main.blueprint)
    app.register_blueprint(controllers.admin.blueprint)
    app.register_blueprint(controllers.consultant.blueprint)
    app.register_blueprint(controllers.client.blueprint)
    app.register_blueprint(controllers.student.blueprint)
    return None


def register_errorhandlers(app):
    @app.errorhandler(403)
    def access_forbidden(error):
        return render_template('error/403.html'), 403
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('error/403.html'), 404
    @app.errorhandler(500)
    def internal_error(error):
        return render_template('error/403.html'), 500
    
    
def register_hooks(app):
    from flask_user.signals import user_registered
    from siwiectech.extensions import db
    with app.app_context():
        @user_registered.connect_via(app)
        def _after_registration_hook(sender, user, **extra):
            role = models.user.Role.query.filter_by(name=request.form.get('user_type')).one()
            user.roles.append(role)
            db.session.add(user)
            db.session.commit()