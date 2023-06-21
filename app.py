from flask import Flask, render_template, jsonify

app = Flask(__name__)

Jobs = [
    {
    'id': 1,
    'Title': 'FrontEnd Engineer',
    'Location': 'Bangalore, India',
    'Salary': 80000
    },
    {
    'id': 2,
    'Title': 'BackEnd Engineer',
    'Location': 'Newyork, USA',
    'Salary': 100000
    },
    {
    'id': 3,
    'Title': 'Data Engineer',
    'Location': 'Atlanta, Georgia',
    'Salary': 120000
    }, 
    {
    'id': 4,
    'Title': 'Cloud Engineer',
    'Location': 'Delhi, India',
    'Salary': 150000
    }
  ]

@app.route("/")
def hello():
  jobs = None
  return render_template('home.html', jobs = Jobs)

@app.route('api/jobs')
def jobs():
  return jsonify(Jobs)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)