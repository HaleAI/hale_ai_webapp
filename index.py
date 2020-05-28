from flask import Flask, request, jsonify, render_template, redirect, flash, url_for
import http.server
import socketserver
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')	

@app.route('/team')
def contact():
	return render_template('team.html')

@app.route('/login')
def loginpage():
	return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def registration():
	if request.method=='POST':
		emid = request.form['emid']
	return render_template('register.html',emid=emid)

@app.route('/reglogin', methods=['GET','POST'])
def printf():
	conn = sqlite3.connect('user.db')
	cur = conn.cursor()
	fname = request.form['firstname']
	lname = request.form['lastname']
	email = request.form['emailadd']
	password = request.form['password']
	conpass = request.form['confirmpass']
	phone = request.form['phoneno']
	usert = request.form['usertype']
	cur.execute("SELECT * FROM users WHERE Email=:Email",{'Email':email})
	if(cur.fetchone()==None):
		cur.execute("INSERT INTO users VALUES (:First_Name,:Last_name,:Email,:Password,:Phone_No,:User_Type)",{'First_Name':fname,'Last_name':lname,'Email':email,'Password':password,'Phone_No':phone,'User_Type':usert})
	else:
		flash("Email Id already exists")
		return render_template('register.html',f=fname,l=lname,email=email,ph=phone,u=usert,emid='')
	if(password!=conpass):
		flash("Passwords don't match")
		return render_template('register.html',f=fname,l=lname,email=email,ph=phone,u=usert,emid='')
	conn.commit()
	conn.close()
	return render_template('login.html',e=email)

@app.route('/logincon',methods=['GET','POST'])
def check():
	conn = sqlite3.connect('user.db')
	cur = conn.cursor()
	email = request.form['eid']
	password = request.form['password']
	a=cur.execute("SELECT Password FROM users WHERE Email=:Email",{'Email':email})
	for b in a:
		c=b
	if(password==c[0]):
		flash("Valid user")
	else:
		flash("Invalid User")
	conn.commit()
	conn.close()
	return render_template('home.html')

if __name__ == "__main__":
    #app.run(host='0.0.0.0',port=5000,debug=True)
	app.secret_key='HaleAI'
	app.run(debug=True)