from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

messages = []

@app.route('/')
def home():
    return render_template('index.html', messages=messages)

@app.route('/send', methods=['POST'])
def send():
    username = request.form['username']
    message = request.form['message']
    messages.append({'username': username, 'message': message})
    return jsonify({'status': 'success', 'message': message, 'username': username})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=int(os.getenv("WEB_PORT", 5000, )))
