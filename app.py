from flask import   render_template, \
                    request, \
                    redirect, \
                    url_for
from flask import Flask
from src import orchestrator

app = Flask(__name__)



@app.route('/')
def say_hello(name = None):
    if orchestrator.check_db():
        hired_employees_head, departments_head, jobs_head = orchestrator.query_head('hired_employees'),\
                                                            orchestrator.query_head('departments'),\
                                                            orchestrator.query_head('jobs')
        return render_template('welcome_preview.html')
    else:
        return render_template('welcome.html')

@app.route('/index/')
def show_form(name = None):
    return render_template('index.html', name = name)

@app.post('/index/')
def upload_files():
    file_objects = request.files.getlist('files')
    for file in file_objects:
        if file.filename != '':
            file.save('landingzone/'+file.filename)
    return redirect(url_for('process_files'))

@app.route('/index/end_upload')
def process_files(name = None):
    orchestrator.ingest_data()
    return render_template('postupload.html', name = name)
