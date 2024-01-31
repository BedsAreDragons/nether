from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# Serve static files from the public directory
@app.route('/')
def index():
    return render_template('index.html')

# Map socket IDs to usernames
users = {}

# Listen for connections
@socketio.on('connect')
def handle_connect():
    print(f"Client connected: {request.sid}")

# Handle login event
@socketio.on('login')
def handle_login(data):
    input_username = data['username']
    password = data['password']

    if password != 'nss':
        emit('loginError', 'Incorrect password')
        print(f"LOGIN ATTEMPT User: {input_username} Pass: {password}")
    else:
        print(f"User '{input_username}' logged in")
        username = input_username
        # Associate username with socket ID
        users[request.sid] = username
        emit('loginSuccess')

# Handle send message event
@socketio.on('sendMessage')
def handle_send_message(message):
    # Get username from session ID
    username = users.get(request.sid)
    print(f"{username}: {message}")
    emit('message', {'username': username, 'text': message}, broadcast=True)

# Handle disconnect event
@socketio.on('disconnect')
def handle_disconnect():
    username = users.pop(request.sid, None)
    if username:
        print(f"Disconnected '{username}'")

if __name__ == '__main__':
    socketio.run(app, debug=True)
