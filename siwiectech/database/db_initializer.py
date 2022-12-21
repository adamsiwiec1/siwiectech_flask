from datetime import datetime


def initialize_db(app, db, user_manager, user_model, project_model, tutoring_model, accounting_model=None):
    with app.app_context():
        db.create_all()
        initialize_project_model(db, project_model)
        initialize_tutoring_model(db, tutoring_model)
        initialize_user_model(db, user_manager, user_model, project_model, accounting_model)
    
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
        
        
def initialize_tutoring_model(db, tm):
    if not tm.Course.query.filter(tm.Course.name == 'Math').first():
        math_course = tm.Course(name='Math')
        db.session.add(math_course)
        db.session.commit()

    if not tm.Course.query.filter(tm.Course.name == 'Coding').all():
        coding_course = tm.Course(name='Coding')
        db.session.add(coding_course)
        db.session.commit()
        
    if len(tm.Course.query.filter(tm.Course.name == 'Math').first().assignments) <= 0:
        assignment = tm.Assignment(name='Algebra stuff')
        math_course = tm.Course.query.filter(tm.Course.name == 'Math').first()
        math_course.assignments.append(assignment)
        db.session.add(math_course)
        db.session.commit()
    

def initialize_user_model(db, user_manager, um, pm, am):
    if not um.Role.query.filter(um.Role.name == 'admin').first():
        role = um.Role(name='admin')
        db.session.add(role)
        db.session.commit()
    
    if not um.Role.query.filter(um.Role.name == 'consultant').first():
        role = um.Role(name='consultant')
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
        client_role = um.Role.query.filter_by(name='client').first()
        project = pm.Project.query.filter_by(name='Initializer').first()
        client.roles.append(client_role)
        client.projects.append(project)
        client.account = am.Account(balance=0)
        db.session.add(client)
        db.session.commit()

    # remove for production - replace with unit tests
    if not um.Student.query.filter(um.Student.email == 'student@example.com').first():
        student = um.Student(
            email='student@example.com',
            email_confirmed_at=datetime.utcnow(),
            password=user_manager.hash_password('Password1'),
            user_type='student',
        )
        student_role = um.Role.query.filter_by(name='student').first()
        student.roles.append(student_role)
        student.account = am.Account(balance=0)
        db.session.add(student)
        db.session.commit()

    # remove for production - replace with unit tests
    if not um.Consultant.query.filter(um.Consultant.email == 'consultant@example.com').first():
        consultant = um.Consultant(
            email='consultant@example.com',
            email_confirmed_at=datetime.utcnow(),
            password=user_manager.hash_password('Password1'),
            user_type='consultant',
        )
        consultant_role = um.Role.query.filter_by(name='consultant').first()
        consultant.roles.append(consultant_role)
        consultant.clients.append(client)
        consultant.students.append(student)
        db.session.add(consultant)
        db.session.commit()
            
    # remove for production - replace with unit tests
    if not um.Admin.query.filter(um.Admin.email == 'admin@example.com').first():
        admin = um.Admin(
            email='admin@example.com',
            email_confirmed_at=datetime.utcnow(),
            password=user_manager.hash_password('Password1'),
            user_type='admin',
        )
        admin_role = um.Role.query.filter_by(name='admin').first()
        admin.roles.append(admin_role)
        db.session.add(admin)
        db.session.commit()