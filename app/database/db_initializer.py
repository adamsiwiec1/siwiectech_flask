from datetime import datetime


def initialize(db, user_manager, User, Role):
    
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
        user = User(
            email='client@example.com',
            email_confirmed_at=datetime.utcnow(),
            password=user_manager.hash_password('Password1'),
        )
        role = Role.query.filter_by(name='client').first()
        user.roles.append(role)
        db.session.add(user)
        db.session.commit()

    # remove for production
    if not User.query.filter(User.email == 'admin@example.com').first():
        user = User(
            email='admin@example.com',
            email_confirmed_at=datetime.utcnow(),
            password=user_manager.hash_password('Password1'),
        )
        role = Role.query.filter_by(name='admin').first()
        user.roles.append(role)
        db.session.add(user)
        db.session.commit()
        
