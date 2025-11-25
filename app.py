from flask import Flask
from flask_cors import CORS
from components.auth import auth
from components.skilltypes import skilltypes
from models import db
from datetime import timedelta

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/myskills'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
CORS(app, resources={r"/*": {"origins": "*"}})

db.init_app(app);

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(skilltypes, url_prefix='/skilltypes')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)