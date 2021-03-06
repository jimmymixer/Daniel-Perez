from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,'emails')
app.secret_key="pussyfoot"
EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/process', methods= ['POST'])
def validate():
    if not EMAIL_REGEX.match(request.form['email']):
        flash('email is not valid format')
        print "here"
        return redirect ('/')
    # else:
    #     query ="INSERT into emails (created_at, updated_at, email) VALUES(NOW(), NOW(), :email)"
    #
    #     data= {
    #     'email': request.form['email']
    #     }
    #     mysql.query_db(query, data)
    #
    #     posting = 'SELECT * FROM email'
    #     emailData = mysql.query_db(posting)
    #     success = str(request.form['email'])
    #     flash('The email address you entered ' + success + ' is a VALID email address! Thank you!')


        return render_template('/success.html', info = emailData)


app.run(debug=True)
