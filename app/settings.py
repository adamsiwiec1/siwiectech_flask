import os 
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class ConfigClass(object):
    """ Flask application config """

    # Flask settings
    SECRET_KEY = 'This is an INSECURE secret!! DO NOT use this in production!!'

    # Flask-SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///basic_app.sqlite'    # File-based SQL database
    SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids SQLAlchemy warning

    # Flask-Mail SMTP server settings
    MAIL_SERVER = 'smtp.sendgrid.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ['MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['SENDGRID_API_KEY']
    MAIL_DEFAULT_SENDER = os.environ['MAIL_DEFAULT_SENDER']

    SENDGRID_API_KEY=os.environ['SENDGRID_API_KEY']

    # Application settings
    APP_NAME = "Flask-User starter app"
    APP_SYSTEM_ERROR_SUBJECT_LINE = APP_NAME + " system error"

    # Flask settings
    CSRF_ENABLED = True

    # Flask-SQLAlchemy settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-User settings
    USER_APP_NAME = APP_NAME
    
    # UserManager settings - https://flask-user.readthedocs.io/en/latest/api_user_manager__settings.html
    USER_ENABLE_EMAIL = True  # Register with Email
    USER_ENABLE_MULTIPLE_EMAILS = False
    USER_ENABLE_USERNAME = False  # Register and Login with username
    USER_ENABLE_CHANGE_USERNAME = False  # Allow users to change their username
    USER_ENABLE_CHANGE_PASSWORD = True  # Allow users to change their password
    USER_ENABLE_CONFIRM_EMAIL = True  # Force users to confirm their email
    USER_ENABLE_FORGOT_PASSWORD = True  # Allow users to reset their passwords
    USER_ENABLE_INVITE_USER = False

    
    
    USER_ENABLE_REGISTER = True  # Allow new users to register
    USER_ENABLE_REMEMBER_ME = True
    USER_REQUIRE_RETYPE_PASSWORD = True  # Prompt for `retype password` in:
    USER_AUTO_LOGIN_AT_LOGIN = True
    USER_ALLOW_LOGIN_WITHOUT_CONFIRMED_EMAIL = False
    USER_REQUIRE_RETYPE_PASSWORD = True
    USER_SHOW_EMAIL_DOES_NOT_EXIST = False
    USER_SHOW_USERNAME_DOES_NOT_EXIST = False
    USER_CONFIRM_EMAIL_EXPIRATION = 172800
    USER_RESET_PASSWORD_EXPIRATION = 172800 #Reset password token expiration in seconds.Default is 2 days (2*24*3600 seconds).
    USER_USER_SESSION_EXPIRATION = 3600
    
    
    # Flask URLS
    
    USER_AFTER_LOGIN_ENDPOINT = 'main.login_redirect'
    USER_AFTER_LOGOUT_ENDPOINT = 'user.login'
    USER_UNAUTHORIZED_ENDPOINT = 'main.error_403'
    USER_AFTER_REGISTER_ENDPOINT = 'main.confirmation_page'

    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')    




# UserManager URLS Reference
# SER_CHANGE_PASSWORD_URL = '/user/change-password'
# USER_CHANGE_USERNAME_URL = '/user/change-username'
# USER_CONFIRM_EMAIL_URL = '/user/confirm-email/<token>'
# USER_EDIT_USER_PROFILE_URL = '/user/edit_user_profile'
# USER_EMAIL_ACTION_URL = '/user/email/<id>/<action>'
# USER_FORGOT_PASSWORD_URL = '/user/forgot-password'
# USER_INVITE_USER_URL = '/user/invite'
# USER_LOGIN_URL = '/user/sign-in'
# USER_LOGOUT_URL = '/user/sign-out'
# USER_MANAGE_EMAILS_URL = '/user/manage-emails'
# USER_REGISTER_URL = '/user/register'
# USER_RESEND_EMAIL_CONFIRMATION_URL = '/user/resend-email-confirmation'
# USER_RESET_PASSWORD_URL = '/user/reset-password/<token>'
# USER_CHANGE_PASSWORD_TEMPLATE = 'flask_user/change_password.html'
# USER_CHANGE_USERNAME_TEMPLATE = 'flask_user/change_username.html'
# USER_EDIT_USER_PROFILE_TEMPLATE = 'flask_user/edit_user_profile.html'
# USER_FORGOT_PASSWORD_TEMPLATE = 'flask_user/forgot_password.html'
# USER_INVITE_USER_TEMPLATE = 'flask_user/invite_user.html'
# USER_LOGIN_TEMPLATE = 'flask_user/login.html'
# USER_LOGIN_AUTH0_TEMPLATE = 'flask_user/login_auth0.html'
# USER_MANAGE_EMAILS_TEMPLATE = 'flask_user/manage_emails.html'
# USER_REGISTER_TEMPLATE = 'flask_user/register.html'
# USER_RESEND_CONFIRM_EMAIL_TEMPLATE = 'flask_user/resend_confirm_email.html'
# USER_RESET_PASSWORD_TEMPLATE = 'flask_user/reset_password.html'
# USER_CONFIRM_EMAIL_TEMPLATE = 'flask_user/emails/confirm_email'
# USER_INVITE_USER_EMAIL_TEMPLATE = 'flask_user/emails/invite_user'
# USER_PASSWORD_CHANGED_EMAIL_TEMPLATE = 'flask_user/emails/password_changed'
# USER_REGISTERED_EMAIL_TEMPLATE = 'flask_user/emails/registered'
# USER_RESET_PASSWORD_EMAIL_TEMPLATE = 'flask_user/emails/reset_password'
# USER_USERNAME_CHANGED_EMAIL_TEMPLATE = 'flask_user/emails/username_changed'
# USER_AFTER_CHANGE_PASSWORD_ENDPOINT = ''
# USER_AFTER_CHANGE_USERNAME_ENDPOINT = ''
# USER_AFTER_CONFIRM_ENDPOINT = ''
# USER_AFTER_EDIT_USER_PROFILE_ENDPOINT = ''
# USER_AFTER_FORGOT_PASSWORD_ENDPOINT = ''
# USER_AFTER_LOGIN_ENDPOINT = ''
# USER_AFTER_LOGOUT_ENDPOINT = ''
# USER_AFTER_REGISTER_ENDPOINT = ''
# USER_AFTER_RESEND_EMAIL_CONFIRMATION_ENDPOINT = ''
# USER_AFTER_RESET_PASSWORD_ENDPOINT = ''
# USER_AFTER_INVITE_ENDPOINT = ''
# USER_UNAUTHENTICATED_ENDPOINT = 'user.login'
# USER_UNAUTHORIZED_ENDPOINT = ''