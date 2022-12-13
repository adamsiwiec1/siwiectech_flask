from datetime import datetime


def initialize_db(app, db, user_manager, User, Role, Project, Deliverable, Task, Incident):
    with app.app_context():
        db.create_all()
        initialize_project_model(db, Project, Deliverable, Task, Incident)
        initialize_user_model(db, user_manager, User, Role, Project)
    
    
def initialize_project_model(db, Project, Deliverable, Task, Incident):
    if not Deliverable.query.filter(Deliverable.name == 'Initialize Database').first():
        deliverable = Deliverable(name='Initialize Database')
        db.session.add(deliverable)
        db.session.commit()
        
    if not Task.query.filter(Task.name == 'Create Example Data for a Project').first():
        task = Task(name='Create Example Data for a Project')
        db.session.add(task)
        db.session.commit()

    if not Incident.query.filter(Incident.name == 'Oh no! The data didnt initialize').first():
        incident = Incident(name='Oh no! The data didnt initialize')
        db.session.add(incident)
        db.session.commit()
    
    if not Project.query.filter(Project.name == 'Initializer Project').first():
        project = Project(name='Initializer')
        project.deliverables.append(Deliverable.query.filter(Deliverable.name == 'Initialize Database').first())
        project.tasks.append(Task.query.filter(Task.name == 'Create Example Data for a Project').first())
        project.incidents.append(Incident.query.filter(Incident.name == 'Oh no! The data didnt initialize').first())
        db.session.add(project)
        db.session.commit()
    

def initialize_user_model(db, user_manager, User, Role, Project):
    if not Role.query.filter(Role.name == 'admin').first():
        role = Role(name='admin')
        db.session.add(role)
        db.session.commit()

    if not Role.query.filter(Role.name == 'client').first():
        role = Role(name='client')
        db.session.add(role)
        db.session.commit()
        
    if not Role.query.filter(Role.name == 'student').first():
        role = Role(name='student')
        db.session.add(role)
        db.session.commit()
    
    
    # remove for production
    if not User.query.filter(User.email == 'client@example.com').first():
        user1 = User(
            email='client@example.com',
            email_confirmed_at=datetime.utcnow(),
            password=user_manager.hash_password('Password1'),
        )
        role1 = Role.query.filter_by(name='client').first()
        project = Project.query.filter_by(name='Initializer').first()
        user1.roles.append(role1)
        user1.projects.append(project)
        db.session.add(user1)
        db.session.commit()


    # remove for production
    if not User.query.filter(User.email == 'student@example.com').first():
        user2 = User(
            email='student@example.com',
            email_confirmed_at=datetime.utcnow(),
            password=user_manager.hash_password('Password1'),
        )
        role2 = Role.query.filter_by(name='student').first()
        user2.roles.append(role2)
        db.session.add(user2)
        db.session.commit()

    # remove for production
    if not User.query.filter(User.email == 'admin@example.com').first():
        user3 = User(
            email='admin@example.com',
            email_confirmed_at=datetime.utcnow(),
            password=user_manager.hash_password('Password1'),
        )
        role3 = Role.query.filter_by(name='admin').first()
        user3.roles.append(role3)
        db.session.add(user3)
        db.session.commit()