from flask_user.forms import ResendEmailConfirmationForm, InviteUserForm, RegisterForm, unique_email_validator
from wtforms import SubmitField, StringField, HiddenField, RadioField
from flask_user import UserManager, login_required, signals
from flask_login import current_user
from flask import current_app, flash, redirect, render_template, request, url_for
from wtforms import validators
from flask_user.translation_utils import lazy_gettext as _    # map _() to lazy_gettext()



# Form Classes
class CustomResendEmailConfirmationForm(ResendEmailConfirmationForm):
    email = StringField(_('Enter your email address below.'), validators=[
        validators.DataRequired(_('Email address is required')),
        validators.Email(_('Invalid Email address')),
        ])
    submit = SubmitField(_('Resend email confirmation email'))
    
    
class CustomInviteUserForm(InviteUserForm):
    email = StringField(_('Email New'), validators=[
        validators.DataRequired(_('Email is required')),
        validators.Email(_('Invalid Email')),
        unique_email_validator])
    # next = HiddenField()
    # submit = SubmitField(_('Invite!'))
    
class CustomRegisterForm(RegisterForm):
    user_type = RadioField(_('I am a...'), choices=[('student', 'Student'), ('client', 'Client')], validators=[
        validators.DataRequired(_('User type is required'))])
    
class CustomUserManager(UserManager):

    def customize(self, app):
        self.ResendEmailConfirmationFormClass = CustomResendEmailConfirmationForm
        self.InviteUserFormClass = CustomInviteUserForm
        self.RegisterFormClass = CustomRegisterForm

    # Override View Actions
    
    @login_required
    def invite_user_view(self):
        invite_user_form = self.InviteUserFormClass(request.form)

        if request.method == 'POST' and invite_user_form.validate():
            # Find User and UserEmail by email
            email = invite_user_form.email.data
            user, user_email = self.db_manager.get_user_and_user_email_by_email(email)
            if user:
                flash("User with that email has already registered", "error")
                return redirect(url_for('user.invite_user'))

            # Add UserInvitation
            user_invitation = self.db_manager.add_user_invitation(
                email=email,
                invited_by_user_id=current_user.id)
            self.db_manager.commit()

            try:
                # Send invite_user email
                self.email_manager.send_invite_user_email(current_user, user_invitation)
            except Exception as e:
                # delete new UserInvitation object if send fails
                self.db_manager.delete_object(user_invitation)
                self.db_manager.commit()
                raise

            # Send sent_invitation signal
            signals \
                .user_sent_invitation \
                .send(current_app._get_current_object(), user_invitation=user_invitation,
                      form=invite_user_form)

            # Flash a system message
            flash(('a NEW invitation has been sent.'), 'success')

            # Redirect
            safe_next_url = self._get_safe_next_url('next', self.USER_AFTER_INVITE_ENDPOINT)
            return redirect(safe_next_url)

        self.prepare_domain_translations()
        return render_template(self.USER_INVITE_USER_TEMPLATE, form=invite_user_form)

