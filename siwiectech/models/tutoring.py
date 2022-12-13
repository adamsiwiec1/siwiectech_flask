from flask_user import UserMixin
from siwiectech.extensions import db


class Course(db.Model, UserMixin):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    assignments = db.relationship('Assignment', secondary='course_assignment')
    appointments = db.relationship('Appointment', secondary='course_appointment')

class UserCourses(db.Model):
    __tablename__ = 'user_course'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    course_id = db.Column(db.Integer(), db.ForeignKey('course.id', ondelete='CASCADE'))

class Assignment(db.Model):
    __tablename__ = 'assignment'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(255))

class Appointment(db.Model):
    __tablename__ = 'appointment'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(255))
    datetime = db.Column(db.DateTime, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    payment_recieved = db.Column(db.Boolean, nullable=False)    
    discounted = db.Column(db.Boolean, nullable=False)

class CourseAssignments(db.Model):
    __tablename__ = 'course_assignment'
    id = db.Column(db.Integer(), primary_key=True)
    project_id = db.Column(db.Integer(), db.ForeignKey('course.id', ondelete='CASCADE'))
    deliverable_id = db.Column(db.Integer(), db.ForeignKey('assignment.id', ondelete='CASCADE'))
    
class CourseAppointments(db.Model):
    __tablename__ = 'course_appointment'
    id = db.Column(db.Integer(), primary_key=True)
    project_id = db.Column(db.Integer(), db.ForeignKey('course.id', ondelete='CASCADE'))
    task_id = db.Column(db.Integer(), db.ForeignKey('appointment.id', ondelete='CASCADE'))