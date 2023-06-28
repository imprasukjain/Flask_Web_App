from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY']='a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0'


from apps.main.routes import main
from apps.future.routes import future

app.register_blueprint(main)
app.register_blueprint(future)
