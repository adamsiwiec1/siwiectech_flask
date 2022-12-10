from flask_user import UserMixin
from app import db


class Project(db.Model, UserMixin):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    budget = db.Column(db.Integer, nullable=True)
    deliverables = db.relationship('Deliverable', secondary='project_deliverables')
    tasks = db.relationship('Task', secondary='project_tasks')
    incidents = db.relationship('Incident', secondary='project_incidents')

# Define the Role data-model
class Deliverable(db.Model):
    __tablename__ = 'deliverables'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(255))

# Define the UserRoles association table
class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(255))
    
# Define the UserRoles association table
class Incident(db.Model):
    __tablename__ = 'incident'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(255))
    
class UserProjects(db.Model):
    __tablename__ = 'user_projects'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    project_id = db.Column(db.Integer(), db.ForeignKey('projects.id', ondelete='CASCADE'))

class ProjectDeliverables(db.Model):
    __tablename__ = 'project_deliverables'
    id = db.Column(db.Integer(), primary_key=True)
    project_id = db.Column(db.Integer(), db.ForeignKey('projects.id', ondelete='CASCADE'))
    deliverable_id = db.Column(db.Integer(), db.ForeignKey('deliverables.id', ondelete='CASCADE'))
    
class ProjectTasks(db.Model):
    __tablename__ = 'project_tasks'
    id = db.Column(db.Integer(), primary_key=True)
    project_id = db.Column(db.Integer(), db.ForeignKey('projects.id', ondelete='CASCADE'))
    task_id = db.Column(db.Integer(), db.ForeignKey('task.id', ondelete='CASCADE'))
    
class ProjectIncidents(db.Model):
    __tablename__ = 'project_incidents'
    id = db.Column(db.Integer(), primary_key=True)
    project_id = db.Column(db.Integer(), db.ForeignKey('projects.id', ondelete='CASCADE'))
    incident_id = db.Column(db.Integer(), db.ForeignKey('incident.id', ondelete='CASCADE'))