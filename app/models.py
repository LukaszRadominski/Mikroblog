from app import db


# Modelem jest tu klasa User, która dziedziczy po db.Models. 
# # db - jest instancją SQLAlchemy 
# # Model  - pochodzi z pluginu flask-sqlalchemy 
# Klasa reprezentuje tabelę, a jej atrybuty odzwierciedlają poszczególne kolumny.

class User(db.Model):                               
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(100), index=True, unique=True)
   email = db.Column(db.String(200), index=True, unique=True)
   password_hash = db.Column(db.String(128))

   def __str__(self):
       return f"<User {self.username}>"