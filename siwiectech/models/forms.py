from flask_user.forms import ResendEmailConfirmationForm, InviteUserForm, unique_email_validator
from wtforms import SubmitField, StringField, HiddenField
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
    
    
class CustomInviteUserForm(InviteUserForm):
    """Invite new user form."""
    email_new = StringField(_('Email New'), validators=[
        validators.DataRequired(_('Email is required')),
        validators.Email(_('Invalid Email')),
        unique_email_validator])
    next = HiddenField()
    submit = SubmitField(_('Invite!'))
    
    
class CustomUserManager(UserManager):

    def customize(self, app):

        # Configure customized forms
        self.ResendEmailConfirmationFormClass = CustomResendEmailConfirmationForm
        self.InviteUserFormClass = CustomInviteUserForm