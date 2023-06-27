from flask import Flask, render_template, jsonify, request
from sqlalchemy import text
from database import engine, load_data_from_database, load_job_data_from_database, jobapplications


app = Flask(__name__)

 
@app.route("/")
def hello():
  jobs = load_data_from_database()
  return render_template('home.html', jobs = jobs)

@app.route('/api/jobs')
def jobs():
  return jsonify(load_data_from_database())

@app.route('/job/<id>')
def get_job_data(id):
  job = load_job_data_from_database(id)
  if not job:
    return "Not Found", 404
  return render_template('jobdetails.html', job = job)


@app.route('/applicationform', methods=['GET'])
def application_form():
    job_id = request.args.get('id')
    # Fetch job data based on the job ID from the database or any other source
    job = load_job_data_from_database(job_id)
    return render_template('application_form.html', job=job)

@app.route('/success', methods=['GET','POST'])
def success():
  application_details = {}
  # job_id = request.args.get('id')
  application_details['name'] = request.form['name']
  application_details['email'] = request.form['email']
  application_details['linkedin'] = request.form['linkedin']
  application_details['education'] = request.form['education']
  application_details['experience'] = request.form['experience']
  application_details['jobid'] = request.form['jobid']
  application_details['resume'] = request.form['resume']
  jobapplications(application_details)
  return jsonify(application_details)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)