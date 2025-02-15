from flask_sqlalchemy import SQLAlchemy


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
    name = db.Column(db.String(120), unique=False, nullable=False)
    last_name = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    # favorites_people = db.Column(db.String(120), unique=False, nullable=True)
    

 

    def __repr__(self):
        return '<User %r>' % self.name
    #es necesario pasar mas datos? self.name, self.id?para que sirven exactamente datos aquí?

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email
            # "favorites_people":self.favorites_people,
            
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
  


    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "homeworld": self.homeworld
        }
    
class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    # climate = db.Column(db.String(120), nullable=True)
    # population = db.Column(db.Integer, nullable=True)
    # diameter = db.Column(db.Integer, nullable=True)
    # orbital = db.Column(db.Integer, nullable=True)
    # favoritos: Mapped[List["Favorites_planets"]] = relationship("Favorites_planets", back_populates="planet")
    def __repr__(self):
       return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # "climate": self.climate,
            # "population": self.population,
            # "diameter": self.diameter,
            # "orbital": self.orbital
        }


class Favorites_people(db.Model):
    __tablename__ = 'favorites_people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False)

    user = db.relationship("User", backref="favorites_people")
    people = db.relationship("People", backref="favorites_people")
  


    def __repr__(self):
        return '<Favorites_people %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
           
        }
    
class Favorites_planets(db.Model):
    __tablename__ = 'favorites_planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False)

    user = db.relationship("User", backref="favorites_planets")
    planets = db.relationship("Planets", backref="favorites_planets")
  


    def __repr__(self):
        return '<Favorites_planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
           
        }
  