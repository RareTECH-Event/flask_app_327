from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['post'])
def authentication():
    return redirect('/')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

