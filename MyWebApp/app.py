from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database='service_db',
                        user = 'postgres',
                        password = '5591',
                        host = 'localhost',
                        port = '5432')
cursor = conn.cursor()
cursor1 = conn.cursor()



@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')
@app.route('/login/',methods=['POST'])
def login():
    message = ''
    username = request.form.get('username')
    password = request.form.get('password')
    if username + password != '':
        cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username),str(password)))
        records = list(cursor.fetchall())
        cursor1.execute("SELECT * FROM service.users")
        records1 = list(cursor1.fetchall())
        if records != []:
            message = 'You authorized'
            return render_template('account.html',full_name=records[0][1],password=password,username=username)
        elif records == [] and username != records1[0][2]:
            message = 'There is no such person in database'  
        elif records == [] and username == records1[0][2] and password != records1[0][3]:
            message = 'Wrong username or password'
    else:
        message = 'Please fill the gaps'

    return render_template('login.html',message=message)