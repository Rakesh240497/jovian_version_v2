from flask import Flask, render_template, jsonify
from sqlalchemy import text
from database import engine, load_data_from_database, load_job_data_from_database


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
  
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)