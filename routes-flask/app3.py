from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        if not username:
            return "Username is required!", 400
        return f"Welcome, {username}!"
    
    return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Login</title>
        </head>
        <body>
            <h1>Login</h1>
            <form method="post">
                <div>
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username" required>
                </div>
                <div>
                    <input type="submit" value="Login">
                </div>
            </form>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
