import sqlite3 as sql

def insertUser(name,email,password):
    con = sql.connect("mydb.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Users (name,email,password) VALUES (?,?,?)", (name,email,password))
    con.commit()
    con.close()

def retrieveUsers():
    con = sql.connect("mydb.db")
    cur = con.cursor()
    cur.execute("SELECT name, email, password FROM Users")
    users = cur.fetchall()

    '''if len(users) is 0:
        con.commit()
        return json.dumps({'message':'User created successfully !'})
    else:
        return json.dumps({'error':str(users[0])})'''

    con.close()
    return users


def userValidate(e,p):
    con = sql.connect("mydb.db")
    cur = con.cursor()
    login = cur.execute('SELECT * from Users WHERE email = ? AND password = ?', (e,p))

    if (len(login.fetchall()) > 0):
         print ("Welcome")
         con.close()
         return True
    else:
         print ("Login failed")
         return False


'''
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
 '''