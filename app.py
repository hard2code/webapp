
import sqlite3
from werkzeug import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, g, json
app = Flask(__name__)



#config database
DATABASE = 'db/database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('database.sql') as f:
            db.cursor().executescript(f.read().decode('utf8'))
        db.commit()


init_db()
 #end of database connection



@app.route('/')
def main():
	
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp', methods = ['POST'])
def signUp():
	# read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']


    # validate the received values
    if _name and _email and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == "__main__":
	app.run(debug=True)



