from flask import Flask, render_template_string
app = Flask(__name__)
@app.route('/')
def home():
    html = """
    <html>
        <head><title>Home</title></head>
        <body>
            <h1>Welcome to Flask</h1>
            <p>This is a basic HTML page.</p>
        </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
