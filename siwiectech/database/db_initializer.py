from datetime import datetime


def initialize_db(app, db, user_manager, user_model, project_model, tutoring_model):
    with app.app_context():
        db.create_all()
        initialize_project_model(db, project_model)
        initialize_user_model(db, user_manager, user_model, project_model)
    
    
def initialize_project_model(db, pm):
    
    if not pm.Deliverable.query.filter(pm.Deliverable.name == 'Initialize Database').first():
        deliverable = pm.Deliverable(name='Initialize Database')
        db.session.add(deliverable)
        db.session.commit()
        
    if not pm.Task.query.filter(pm.Task.name == 'Create Example Data for a Project').first():
        task = pm.Task(name='Create Example Data for a Project')
        db.session.add(task)
        db.session.commit()

    if not pm.Incident.query.filter(pm.Incident.name == 'Oh no! The data didnt initialize').first():
        incident = pm.Incident(name='Oh no! The data didnt initialize')
        db.session.add(incident)
        db.session.commit()
    
    if not pm.Project.query.filter(pm.Project.name == 'Initializer Project').first():
        project = pm.Project(name='Initializer')
        project.deliverables.append(pm.Deliverable.query.filter(pm.Deliverable.name == 'Initialize Database').first())
        project.tasks.append(pm.Task.query.filter(pm.Task.name == 'Create Example Data for a Project').first())
        project.incidents.append(pm.Incident.query.filter(pm.Incident.name == 'Oh no! The data didnt initialize').first())
        db.session.add(project)
        db.session.commit()
    

def initialize_user_model(db, user_manager, um, pm):
    if not um.Role.query.filter(um.Role.name == 'admin').first():
        role = um.Role(name='admin')
        db.session.add(role)
        db.session.commit()

    if not um.Role.query.filter(um.Role.name == 'client').first():
        role = um.Role(name='client')
        db.session.add(role)
        db.session.commit()
        
    if not um.Role.query.filter(um.Role.name == 'student').first():
        role = um.Role(name='student')
        db.session.add(role)
        db.session.commit()
    
    
    # remove for production - replace with unit tests
    if not um.User.query.filter(um.User.email == 'client@example.com').first():
        client = um.Client(
            email='client@example.com',
            email_confirmed_at=datetime.utcnow(),
            password=user_manager.hash_password('Password1'),
            user_type='client',
        )
        role1 = um.Role.query.filter_by(name='client').first()
        project = pm.Project.query.filter_by(name='Initializer').first()
        client.roles.append(role1)
        client.projects.append(project)
        db.session.add(client)
        db.session.commit()


    # remove for production - replace with unit tests
    if not um.Student.query.filter(um.Student.email == 'student@example.com').first():
        user2 = um.Student(
            email='student@example.com',
            email_confirmed_at=datetime.utcnow(),
            password=user_manager.hash_password('Password1'),
            user_type='student',
        )
        role2 = um.Role.query.filter_by(name='student').first()
        user2.roles.append(role2)
        db.session.add(user2)
        db.session.commit()

    # remove for production - replace with unit tests
    if not um.User.query.filter(um.User.email == 'admin@example.com').first():
        user3 = um.User(
            email='admin@example.com',
            email_confirmed_at=datetime.utcnow(),
            password=user_manager.hash_password('Password1'),
            user_type='consultant',
        )
        role3 = um.Role.query.filter_by(name='admin').first()
        user3.roles.append(role3)
        db.session.add(user3)
        db.session.commit()