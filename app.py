from flask import Flask, jsonify, session, request
from flask_sqlalchemy import SQLAlchemy

import secrets
import string


app = Flask(__name__)
app.config['SECRET_KEY'] = "#XTj~-lQt%$\aFz2"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String())


    def __init__(self,email,username,password):
        self.email=email
        self.username=username
        self.password=password



from flask import jsonify

# Login route
@app.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']

    user = User.query.filter_by(email=email).first()

    if user.password ==password:
          return jsonify({"msg":"Login succesful"})
    return jsonify({"msg":"invalid details"})


@app.route('/register', methods = ['POST'])
def Signup():
    email = request.json['email']
    username = request.json['username']
    password = request.json['password']

    my_post = User(email, username,password)
    db.session.add(my_post)
    db.session.commit()
    

    return jsonify({"msg":"Registration successfull"})

# Logout route
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return jsonify({"msg": "Logout successful"})





def generate_secret_key(length=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

print(generate_secret_key())  # Output a randomly generated key


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)  
