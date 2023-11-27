from flask import Flask, jsonify
import pandas as pd
import time
from sklearn.ensemble import IsolationForest
from flask_apscheduler import APScheduler

from flask_cors import CORS
from twilio.rest import Client

app = Flask(__name__)
CORS(app)

# Load the dataset from CSV
dataset = pd.read_csv('dataset.csv')
isolation_forest = IsolationForest(contamination=0.1)
isolation_forest.fit(dataset[['Heart Beat','SPO2','Systolic','Diastolic','Respiratory','Body Temp.','Sugar Level', 'hbpm', 'rbpm']].values) 
# Index to keep track of the current row to send
current_row = 0
bp = []
heart = []

# Initialize the counter
counter = 0

scheduler = APScheduler()
# if you don't wanna use a config, you can set options here:
# scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()

def sendMsg():


    account_sid = 'AC3c64a93f2c330dd53fa0bf6a16884e29'
    auth_token = '789b8f3a4a222cbe0b2fa76f32ff500e'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='+12673547173',
    body='Alert',
    to='+917005674461'
    )

    print(message.sid)

@scheduler.task('interval', id='do_job_1', seconds=1, misfire_grace_time=900)
def job1():
    global counter
    counter += 1
    print(counter)

@scheduler.task('interval', id='do_job_2', seconds=1, misfire_grace_time=900)
def job2():
    row = get_next_row()

    # Perform anomaly detection
    is_anomaly = detect_anomaly(row)

    # Execute a function when an anomaly is detected
    if is_anomaly:
        sendMsg()
        print("Anomaly detected!")

# Function to get the next row from the dataset
def get_next_row():
    global counter
    if counter < len(dataset):
        row = dataset.iloc[counter].to_dict()
        return row
    else:
        counter = 0
        row = dataset.iloc[counter].to_dict()
        return row

def detect_anomaly(row):
    # Use isolation forest to detect anomalies Heart Beat,SPO2,Systolic,Diastolic,Respiratory,Body Temp.,Sugar Level
    data_point = [row['Heart Beat'], row['SPO2'], row['Systolic'], row['Diastolic'], row['Respiratory'], row['Body Temp.'], row['Sugar Level'], row['hbpm'], row['rbpm']]  # Replace with your actual features
    is_anomaly = isolation_forest.predict([data_point])[0] == -1
    return is_anomaly

# Endpoint to get the next row as JSON
@app.route('/data', methods=['GET'])
def getData():
    row = get_next_row()
    if row is not None:
        return jsonify(row)
    else:
        return jsonify({'message': 'End of dataset'})

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
