from flask import Flask, make_response, request, jsonify
import mysql.connector

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

mydb = mysql.connector.connect(host='containers-us-west-168.railway.app',
                               user='root', password='46HroTHKyjsKYUr7Pp8s',
                               database='railway', port='6835')

@app.route('/')
def hello():

    return "<p>Hello!</p>"

@app.route('/Notification', methods=['POST'])
def post_notification():

    notification = request.json

    my_cursor = mydb.cursor()

    sent = notification['sent'].split('.', 1)
    received = notification['received'].split('.', 1)

    print(sent)

    sql = f"INSERT INTO Notifications (_id, resource, user_id, topic, application_id, attempts, sent, received) VALUES ('{notification['_id']}', '{notification['resource']}', {notification['user_id']}, '{notification['topic']}', {notification['application_id']}, {notification['attempts']}, '{sent[0]}', '{received[0]}')"

    my_cursor.execute(sql)
    mydb.commit()

    return make_response(
        jsonify(
            messagem="Notificação registrada.",
            notification=notification
        )
    )

app.run()