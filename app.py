from flask import   render_template, \
                    request, \
                    redirect, \
                    url_for
from flask import Flask
from src import orchestrator

app = Flask(__name__)

FIELDS = {
    'hired_employees':['name', 'department_id', 'job_id'],
    'departments':['department'],
    'jobs':['job']
}

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

# !! Work in progress.
@app.route('/per_record_upload/<string:table_name>', methods = ["GET", "POST"])
def upload_row_to(table_name):
    if request.method == 'POST':
        response = []
        for field_name in FIELDS[table_name]:
            if 'id' not in field_name: 
                response.append(f"'{request.args.get(field_name)}'")
            else:
                response.append(request.args.get(field_name))
        print(response)
        orchestrator.upload(values = response, table_name = table_name)
        return redirect(url_for('say_hello'))
    else:
        return render_template(f'upload_form/{table_name}.html')
    
@app.route('/query/quarters')
def get_employees_per_quarter():
    orchestrator.run_query('quarter')
    return render_template('results/quarter.html')

@app.route('/query/mean')
def get_more_hiring_depts():
    orchestrator.run_query('mean')
    return render_template('results/mean.html')