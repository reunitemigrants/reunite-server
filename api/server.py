import os

from flask import Flask, jsonify, request
import pyrebase


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'dev')
if app.config['SECRET_KEY'] == 'dev':
    app.config['DEBUG'] = True


firebase_config = {
    "apiKey": os.environ.get('FIREBASE_API_KEY'),
    "authDomain": "reunitefamilies-28bee.firebaseapp.com",
    "databaseURL": "https://reunitefamilies-28bee.firebaseio.com",
    "storageBucket": "reunitefamilies-28bee.appspot.com"
}
firebase = pyrebase.initialize_app(firebase_config)


@app.route('/register')
def register():
    data = request.form
    email = data['email']
    password = data['password']
    user = firebase.auth().create_user_with_email_and_password(email, password)
    volunteer = {
        'firebase_id': user['uid'],
        'name': data['name'],
        'location': data['location'],
        'languages': data['languages']
    }
    firebase.child('volunteers').push(volunteer)
    return 'registered'


@app.route('/login')
def login():
    data = request.form
    email = data['email']
    password = data['password']
    firebase.auth().sign_in_with_email_and_password(email, password)
    return 'logged in'


@app.route('/current-user')
def current_user():
    user = firebase.auth().current_user
    return jsonify(current_user=user)


if __name__ == "__main__":
    kwargs = {}
    if os.getenv('PORT'):
        kwargs.update(port=os.getenv('PORT'))
    app.run(**kwargs)
