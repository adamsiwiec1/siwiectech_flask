from flask_user import UserMixin
from siwiectech.extensions import db


class Course(db.Model, UserMixin):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    assignments = db.relationship('Assignment', secondary='course_assignments')
    appointments = db.relationship('Appointment', secondary='course_appointments')

class Assignment(db.Model):
    __tablename__ = 'assignments'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(255))

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(255))
    datetime = db.Column(db.DateTime, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    payment_recieved = db.Column(db.Boolean, nullable=False)    
    discounted = db.Column(db.Boolean, nullable=False)


class CourseAssignments(db.Model):
    __tablename__ = 'course_assignments'
    id = db.Column(db.Integer(), primary_key=True)
    project_id = db.Column(db.Integer(), db.ForeignKey('courses.id', ondelete='CASCADE'))
    deliverable_id = db.Column(db.Integer(), db.ForeignKey('assignments.id', ondelete='CASCADE'))
    
class CourseAppointments(db.Model):
    __tablename__ = 'course_appointments'
    id = db.Column(db.Integer(), primary_key=True)
    project_id = db.Column(db.Integer(), db.ForeignKey('courses.id', ondelete='CASCADE'))
    task_id = db.Column(db.Integer(), db.ForeignKey('appointments.id', ondelete='CASCADE'))