from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()
    


# $ pipenv run migrants # (para realizar las migraciones)
# $ pipenv run upgrade # (para actualizar su base de datos con las migraciones)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         # return '<User %r>' % self.username
#         return '<User %r>' % self.email

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favorites = db.Column(db.String(80), unique=False, nullable=False)
    favorites_people = relationship("Favorites_People", backref="user")
 

    def __repr__(self):
        # return '<User %r>' % self.username
        return '<User %r>' % self.last_name
    #es necesario pasar mas datos? self.name, self.id?para que sirven exactamente datos aquí?

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email,
            "favorites_people": self.favorites_people

        }
    

class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer, nullable=False)
    skin_color = db.Column(db.String(120), nullable=False)
    eye_color = db.Column(db.String(120), nullable=False)
    homeworld = db.Column(db.String(120), nullable=False)
    user_favorites = relationship("Favorites_People", backref="user")
    user_id = Column(Integer, ForeignKey('users.id'))


    def __repr__(self):
        # return '<User %r>' % self.username
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "homeworld": self.homeworld,
         

        }
    
class Favorites_People(db.Model):
    __tablename__ = 'favorites_people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False)
    user = db.relationship("User", back_populates="favorites")
    people = db.relationship("People", back_populates="favorites_people")
    favorites_people = relationship("Favorites_People", backref="user")

    def __repr__(self):
        # return '<User %r>' % self.username
        return '<Favorites_People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "people_id": self.people_id,

          

        }