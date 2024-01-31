from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_message():
    user = request.form['user']
    message = request.form['message']
    return {'user': user, 'message': message}

if __name__ == '__main__':
    app.run(debug=True)
