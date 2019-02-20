
import db_init as db
from flask import Flask, render_template, request, g, json
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)

#database config


@app.route('/')
def main():
	
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp', methods = ['POST'])
def signUp():


	if request.method=='POST':
		name = request.form['inputName']
		email = request.form['inputEmail']
		password = request.form['inputPassword']
		db.insertUser(name,email, password)
		users = db.retrieveUsers()

		# validate the received values
		if name and email and password:
			return json.dumps({'html':'<span>All fields good !!</span>'})
		else:
			return json.dumps({'html':'<span>Enter the required fields</span>'})

		return render_template('login.html', users=users)
	else:
		return render_template('signUp.html')



@app.route('/showSignin')
def showSignin():
    return render_template('login.html')


@app.route('/validateLogin',methods=['POST'])
def validateLogin():
    try:
        email = request.form['inputEmail']
        password = request.form['inputPassword']
 
    except Exception as e:
        return render_template('error.html',error = str(e))

if __name__ == "__main__":
	app.run(debug=True)



