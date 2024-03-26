from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Dummy database for users and messages
users = {}
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users[username] = password
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('publish'))
    return render_template('login.html')

@app.route('/publish', methods=['GET', 'POST'])
def publish():
    if request.method == 'POST':
        message = request.form['message']
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        messages.append({'message': message, 'timestamp': timestamp})
        return redirect(url_for('index'))
    return render_template('publish.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
