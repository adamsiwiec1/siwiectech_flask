from flask_user import UserMixin
from siwiectech.extensions import db

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    email = db.Column(db.String(255, collation='NOCASE'), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    password = db.Column(db.String(255), nullable=False, server_default='')
    first_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
    last_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
    roles = db.relationship('Role', secondary='user_role')
    account = db.relationship('Account', uselist=False, backref='user')
    user_type = db.Column(db.String(32), nullable=False)
    __mapper_args__ = {'polymorphic_on': user_type}

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

class UserRoles(db.Model):
    __tablename__ = 'user_role'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))

class UserInvitation(db.Model):
    __tablename__ = 'user_invitation'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255, collation='NOCASE'), nullable=False, unique=True)
    invited_by_user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))

class Admin(User):
    __tablename__ = 'admin'
    __mapper_args__ = {'polymorphic_identity': 'admin'}
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

class Client(User):
    __tablename__ = 'client'
    __mapper_args__ = {'polymorphic_identity': 'client'}
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    projects = db.relationship('Project', secondary='user_project')
    business_name = db.Column(db.String(50), nullable=True)

class Student(User):
    __tablename__ = 'student'
    __mapper_args__ = {'polymorphic_identity': 'student'}
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    courses = db.relationship('Course', secondary='user_course')
    school_name = db.Column(db.String(50), nullable=True)

class Consultant(User):
    __tablename__ = 'consultant'
    __mapper_args__ = {'polymorphic_identity': 'consultant'}
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    clients = db.relationship("Client", secondary="consultant_client")
    students = db.relationship("Student", secondary="consultant_student")

class ConsultantClient(db.Model):
    __tablename__ = 'consultant_client'
    id = db.Column(db.Integer(), primary_key=True)
    consultant_id = db.Column(db.Integer(), db.ForeignKey('consultant.id', ondelete='CASCADE'))
    client_id = db.Column(db.Integer(), db.ForeignKey('client.id', ondelete='CASCADE'))
    
class ConsultantStudent(db.Model):
    __tablename__ = 'consultant_student'
    id = db.Column(db.Integer(), primary_key=True)
    consultant_id = db.Column(db.Integer(), db.ForeignKey('consultant.id', ondelete='CASCADE'))
    student_id = db.Column(db.Integer(), db.ForeignKey('student.id', ondelete='CASCADE'))