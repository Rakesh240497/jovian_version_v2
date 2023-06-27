from sqlalchemy import create_engine, text
import os
# connectstring = os.environ['DBCONNECTION']
my_secret = os.environ['DBCONNECTION']

engine = create_engine(my_secret, 
                       connect_args= {'ssl': {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }
                    })
# result_dict = None

def load_data_from_database():
  with engine.connect()  as conn:
    result = conn.execute(text("select * from Jobs;"))
    jobs = [dict(zip(result.keys(), row)) for row in result]
    return (jobs)



def load_job_data_from_database(id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from Jobs where id = :id"), {"id": id})
        jobs = [dict(zip(result.keys(), row)) for row in result]
        if not jobs:
          return False
        else: 
          return jobs[0]
        
def jobapplications(application):
  with engine.connect() as conn:
    try:
      query = conn.execute(text("INSERT INTO applications (jobid, fullname, email, linkedin, education, experience, resumelink) "
                          "VALUES (:jobid, :fullname, :email, :linkedin, :education, :experience, :resumelink)"),
                     {
                         "jobid": application['jobid'],
                         "fullname": application['name'],
                         "email": application['email'],
                         "linkedin": application['linkedin'],
                         "education": application['education'],
                         "experience": application['experience'],
                         "resumelink": application['resume']
                     })
    except Exception as e:
      print(f"Error occurred during query execution: {e}")
      
    
    