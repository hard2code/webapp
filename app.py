
import db_init as get_db
from flask import Flask, render_template, request, g, json
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)



@app.route('/')
def main():
	
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp', methods = ['POST'])
def signUp():

	if request.method=='POST':
		email = request.form['inputEmail']
		username = request.form['inputName']
		password = request.form['inputPassword']
		get_db.insertUser(username, password)
		users = get_db.retrieveUsers()

		# validate the received values
		if username and email and password:
			return json.dumps({'html':'<span>All fields good !!</span>'})
		else:
			return json.dumps({'html':'<span>Enter the required fields</span>'})

		return render_template('login.html', users=users)
	else:
		return render_template('login.html')



@app.route('/showSignin')
def showSignin():
    return render_template('login.html')


@app.route('/validateLogin',methods=['POST'])
def validateLogin():
    try:
        username = request.form['inputEmail']
        password = request.form['inputPassword']
 
    except Exception as e:
        return render_template('error.html',error = str(e))

if __name__ == "__main__":
	app.run(debug=True)



