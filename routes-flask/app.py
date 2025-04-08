from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/form')
def form():
    return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Name Form</title>
        </head>
        <body>
            <form action="/result" method="get">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    '''

@app.route('/result')
def result():
    name = request.args.get('name')
    if not name:
        return "Please provide a name parameter", 400
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
