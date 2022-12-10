from flask_user.forms import ResendEmailConfirmationForm
from wtforms import SubmitField, StringField
from flask_user import UserManager
from wtforms import validators
from flask_user.translation_utils import lazy_gettext as _    # map _() to lazy_gettext()


#  Override Flask-User's Forms Here


class CustomResendEmailConfirmationForm(ResendEmailConfirmationForm):
    """Resend email confirmation form."""
    email = StringField(_('Enter your email address below.'), validators=[
        validators.DataRequired(_('Email address is required')),
        validators.Email(_('Invalid Email address')),
        ])
    submit = SubmitField(_('Resend email confirmation email'))
    
class CustomUserManager(UserManager):

    def customize(self, app):

        # Configure customized forms
        self.ResendEmailConfirmationFormClass = CustomResendEmailConfirmationForm
