from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/admin')
def admin():
    """Redirects to user page with admin name"""
    return redirect(url_for('user', name='admin'))

@app.route('/user/<name>')
def user(name):
    """Greets the user with their name"""
    return f"Welcome, {name}"

if __name__ == '__main__':
    app.run(debug=True)
