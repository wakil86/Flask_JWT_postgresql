from flask import Flask, jsonify
from config import Config
from extensions import db, jwt
from routes.auth_routes import auth_bp, blacklist
from routes.protected_routes import protected_bp
from models import User 

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)


    db.init_app(app)
    jwt.init_app(app)

    with app.app_context(): 
        db.create_all()     

    app.register_blueprint(auth_bp)
    app.register_blueprint(protected_bp)

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blacklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in blacklist

    return app


app = create_app()


def create_tables():
    with app.app_context():
        db.create_all()
        

@app.route('/')
def index():
    return jsonify({'msg': 'API is working'}), 200

if __name__ == '__main__':
    create_tables()
    app.run(debug=True,host='0.0.0.0', port=5000)
