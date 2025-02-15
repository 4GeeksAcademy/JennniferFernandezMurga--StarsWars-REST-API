"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People
from models import Planets, Favorites_people, Favorites_planets
from sqlalchemy import func

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def get_all_users():
    try:
        # Realiza la consulta a la base de datos
        data = db.session.scalars(db.select(User)).all()
        
        # Comprueba si hay resultados
        if not data:
            return jsonify({"msg": "No users found"}), 404
        
        # Serializa los resultados
        result = list(map(lambda item: item.serialize(), data))
        
        # Construye la respuesta
        response_body = {
            "results": result
        }
        
        return jsonify(response_body), 200

    except Exception as e:
        # Maneja cualquier otro tipo de error
        return jsonify({"msg": "An error occurred", "error": str(e)}), 500
    
@app.route('/users/favorites', methods=['GET'])
def get_favorites_users():
    try:
        # Realiza la consulta a la base de datos
        data = db.session.scalars(db.select(Favorites_people)).all()
        
        # Comprueba si hay resultados
        if not data:
            return jsonify({"msg": "No users found"}), 404
        
        # Serializa los resultados
        result = list(map(lambda item: item.serialize(), data))
        
        # Construye la respuesta
        response_body = {
            "results": result
        }
        
        return jsonify(response_body), 200

    except Exception as e:
        # Maneja cualquier otro tipo de error
        return jsonify({"msg": "An error occurred", "error": str(e)}), 500



@app.route('/people', methods=['GET'])
def get_all_people():
    try:
        # Realiza la consulta a la base de datos
        data = db.session.scalars(db.select(People)).all()
        
        # Comprueba si hay resultados
        if not data:
            return jsonify({"msg": "No people found"}), 404
        
        # Serializa los resultados
        result = list(map(lambda item: item.serialize(), data))
        
        # Construye la respuesta
        response_body = {
            "results": result
        }
        
        return jsonify(response_body), 200

    except Exception as e:
        # Maneja cualquier otro tipo de error
        return jsonify({"msg": "An error occurred", "error": str(e)}), 500
    

    
@app.route('/people/<int:id>', methods=['GET'])
def get_one_person(id):
    try:
        # Obtiene la persona de la base de datos
        person = db.session.execute(db.select(People).filter_by(id=id)).scalar_one()
        
        # Comprueba si hay resultados
        if person is None:
            return jsonify({"msg": "No person found"}), 404
        
        # Serializa el resultado
        result = person.serialize()
        
        # Construye la respuesta
        response_body = {
            "result": result
        }
        
        return jsonify(response_body), 200

    except Exception as e:
        # Maneja cualquier otro tipo de error
        return jsonify({"msg": "An error occurred", "error": str(e)}), 500

    

@app.route('/planets', methods=['GET'])
def get_all_planets():
    try:
     # Realiza la consulta a la base de datos
        # data = db.session.scalars(db.select(Planets)).all()
       
        # data = db.session.scalars(db.select(func.count('*')).select_from(Planets)).all()
        data = db.session.query(func.count(Planets.id)).scalar()

        
        # Comprueba si hay resultados
        if not data:
            return jsonify({"msg": "No planets found"}), 404
        
        # Serializa los resultados
        result = list(map(lambda item: item.serialize(), data))
        
        # Construye la respuesta
        response_body = {
            "results": result
        }
        
        return jsonify(response_body), 200

    except Exception as e:
        # Maneja cualquier otro tipo de error
        return jsonify({"msg": "An error occurred", "error": str(e)}), 500
    
@app.route('/planets/<int:id>', methods=['GET'])
def get_one_planet(id):
    try:
        # Obtiene la persona de la base de datos
        planet = db.session.execute(db.select(Planets).filter_by(id=id)).scalar_one()
        
        # Comprueba si hay resultados
        if planet is None:
            return jsonify({"msg": "No planet found"}), 404
        
        # Serializa el resultado
        result = planet.serialize()
        
        # Construye la respuesta
        response_body = {
            "result": result
        }
        
        return jsonify(response_body), 200

    except Exception as e:
        # Maneja cualquier otro tipo de error
        return jsonify({"msg": "An error occurred", "error": str(e)}), 500



    

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
