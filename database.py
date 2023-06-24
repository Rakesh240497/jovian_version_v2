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
