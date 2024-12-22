from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/home")
def Home():
    return render_template("home.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if username and email and password:
            users[username] = {
                'email': email,
                'password': password,
                'points': 0
            }
            return redirect(url_for('home'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/ar')
def ar():
    return render_template('ar.html')  

@app.route('/tips')
def advices():
    return render_template('tips.html')

if __name__ == "__main__":
    app.run(debug=True)
