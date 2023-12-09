import sqlite3
from flask import Flask, render_template, request, g

app = Flask(__name__)
DATABASE = './inf.db'

# preinit?
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# reservations 테이블 생성
create_table_query = '''
CREATE TABLE IF NOT EXISTS reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    date TEXT NOT NULL
);
'''
cursor.execute(create_table_query)

# 변경 사항 커밋 및 연결 종료
conn.commit()
conn.close()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# twilio
from twilio.rest import Client

account_sid = 'AC206ef4d70c94e4dc749095654bb2689b'
auth_token = 'c95346acfa82e164b1e9168a72442d4d'
client = Client(account_sid, auth_token)

def send_sms(phone_number, message):
    client.messages.create(to=phone_number, 
                           from_='+18304338633', # TODO: 수정 
                           body=message)

TO = '+821074735898'

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        date = request.form.get('date')

        db = get_db()
        db.execute('INSERT INTO reservations (name, phone, date) VALUES (?, ?, ?)',
                   [name, phone, date])
        db.commit()

        send_sms(TO, '새로운 방문 예약이 있습니다:\n이름: {}\n전화번호: {}\n, 날짜:{}'.format(name, phone, date))

        return render_template('index.html')
    elif request.method == 'GET':
        return render_template('index.html')

app.run(host = '127.0.0.1', port=8080)