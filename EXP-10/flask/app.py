from flask import Flask, render_template, request, render_template_string
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])


def form():
    if request.method == 'POST':
        name = request.form['name']
        return render_template("greeting.html", name=name)
    return render_template("form.html")
if __name__ == '__main__':
    app.run(debug=True)
