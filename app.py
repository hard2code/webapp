
import db_init as db

from flask import Flask, render_template, request, g, json, redirect, session
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = 'why would I tell you my secret key?'
#database config


@app.route('/')
def main():
	
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/showSignin')
def showSignin():
    return render_template('login.html')


@app.route('/validateLogin',methods=['POST'])
def validateLogin():
    try:
        email = request.form['inputEmail']
        password = request.form['inputPassword']
        session['user'] = db.getUser(email)
        if db.userValidate(email,password):
        	return redirect('/userHome')
        else:
        	return render_template('error.html',error = 'Wrong Email address or Password.')

 
    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
    	print("success signin")

@app.route('/signUp', methods = ['POST'])
def signUp():

	try:
		name = request.form['inputName']
		email = request.form['inputEmail']
		password = request.form['inputPassword']

			# validate the received values
		if name and email and password:
			if db.userValidate(email,password):
				print("error in render")
				return render_template('error.html',error = 'Email address already exists.')
			else:
				db.addUser(name,email, password)
				return json.dumps({'html':'<span>All fields good and user has been added !!</span>'})
		else:
			return json.dumps({'html':'<span>Enter the required fields</span>'})

		
	except Exception as e:
		return json.dumps({'error':str(e)})
	finally:
		return redirect('/showSignin')




@app.route('/userHome')
def userHome():
	if session.get('user'):
		return render_template('dashboard.html')
	else:
		return render_template('error.html',error = 'Unauthorized Access')

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/')


@app.route('/showSell')
def showSell():
    return render_template('Sell.html')

@app.route('/addItem',methods=['POST'])
def addItem():
    # Code will be here
    try:
        if session.get('user'):
            name = request.form['inputTitle']
            disc = request.form['inputDescription']
            picURL = request.form['inputImage'] 
            userId = session.get('user')

            db.add_item(userId,name,disc,picURL)
            item = db.get_item(name)
            if len(item) is 0:
                return render_template('error.html',error = 'Item is not added!')
            else:
                return redirect('/showSell')
 
        else:
            return render_template('error.html',error = 'Unauthorized Access')
    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
        print("item added")

if __name__ == "__main__":
	app.run(debug=True)



