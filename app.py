from flask import Flask, render_template, jsonify
from sqlalchemy import text
from database import engine


app = Flask(__name__)



def load_data_from_database():
  with engine.connect()  as conn:
    result = conn.execute(text("select * from Jobs;"))
    jobs = [dict(zip(result.keys(), row)) for row in result]
    return (jobs)
 
@app.route("/")
def hello():
  jobs = load_data_from_database()
  
  return render_template('home.html', jobs = jobs)

@app.route('/api/jobs')
def jobs():
  return jsonify(load_data_from_database())
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)