from flask import render_template, request, redirect, url_for
from flask import Flask

app = Flask(__name__)

@app.route('/index/')
def show_form(name = None):
    return render_template('index.html', name = name)

@app.post('/index/')
def upload_files():
    file_objects = request.files.getlist('files')
    for file in file_objects:
        if file.filename != '':
            file.save('landingzone/'+file.filename)
    return redirect(url_for('show_form'))

@app.route("/")
def say_hello(name = None):
    return render_template('welcome.html', name = name)