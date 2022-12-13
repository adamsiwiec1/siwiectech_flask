from flask_user import UserMixin
from siwiectech.extensions import db


class Project(db.Model, UserMixin):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    budget = db.Column(db.Integer, nullable=True)
    deliverables = db.relationship('Deliverable', secondary='project_deliverable')
    tasks = db.relationship('Task', secondary='project_task')
    incidents = db.relationship('Incident', secondary='project_incident')

class UserProjects(db.Model):
    __tablename__ = 'user_project'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    project_id = db.Column(db.Integer(), db.ForeignKey('project.id', ondelete='CASCADE'))

class Deliverable(db.Model):
    __tablename__ = 'deliverable'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(255))

class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(255))
    
class Incident(db.Model):
    __tablename__ = 'incident'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(255))
    
class ProjectDeliverables(db.Model):
    __tablename__ = 'project_deliverable'
    id = db.Column(db.Integer(), primary_key=True)
    project_id = db.Column(db.Integer(), db.ForeignKey('project.id', ondelete='CASCADE'))
    deliverable_id = db.Column(db.Integer(), db.ForeignKey('deliverable.id', ondelete='CASCADE'))
    
class ProjectTasks(db.Model):
    __tablename__ = 'project_task'
    id = db.Column(db.Integer(), primary_key=True)
    project_id = db.Column(db.Integer(), db.ForeignKey('project.id', ondelete='CASCADE'))
    task_id = db.Column(db.Integer(), db.ForeignKey('task.id', ondelete='CASCADE'))
    
class ProjectIncidents(db.Model):
    __tablename__ = 'project_incident'
    id = db.Column(db.Integer(), primary_key=True)
    project_id = db.Column(db.Integer(), db.ForeignKey('project.id', ondelete='CASCADE'))
    incident_id = db.Column(db.Integer(), db.ForeignKey('incident.id', ondelete='CASCADE'))