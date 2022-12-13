import os
from flask_migrate import Migrate
from flask_minify  import Minify
from sys import exit
from siwiectech.app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001, debug=True)