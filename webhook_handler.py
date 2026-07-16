from flask import Flask, request, jsonify
import pandas as pd
import datetime

app = Flask(__name__)

# WebHook-Sentinel: A lightweight logging service
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.json
    data['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Save to CSV log file
    df = pd.DataFrame([data])
    df.to_csv('webhook_logs.csv', mode='a', header=False, index=False)
    
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(port=5000)
