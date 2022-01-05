from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.secret_key = 'jlnbcjsbf8473ry3u4r8348r3ciojidoht$^%$#%^@&^##G@#8cxn9ud9y8u9f8yd92'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dmyibvqxelodpb:df1329a4282103c7099bfe870b5677c06c33362395fdaadccf222857d46d4326@ec2-34-197-195-181.compute-1.amazonaws.com:5432/d128r57i8qb24s'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    
    return app




if __name__ == "__main__":
  app.run()
  
  

