from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for passwords
passwords = {}

# Messages storage
messages = []

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/chat', methods=['POST'])
def chat():
    return render_template('chat.html', messages=messages)

@app.route('/send', methods=['POST'])
def send():
    password = request.form['password']
    
    if password == 'your_secret_password':
        message = request.form['message']
        messages.append({'username': 'Guest', 'message': message})
    
    return redirect(url_for('chat'))

if __name__ == '__main__':
    app.run(debug=True)
