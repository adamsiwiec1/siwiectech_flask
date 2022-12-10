import os
from flask_migrate import Migrate
from flask_minify  import Minify
from sys import exit
from app import create_app

app, db = create_app()
Migrate(app, db)




if __name__ == "__main__":
    app.run()