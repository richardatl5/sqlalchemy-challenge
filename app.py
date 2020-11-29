import numpy as np

import sqlalchemy

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

date = Base.classes.keys

hw = Flask(__name__)

@hw.route("/")
def welcome():
    """List all available api routes."""
    "/api/v1.0/precipitation" 
  
@hw.route("/api/v1.0/passengers")
def names():
    session = Session(engine)
    results = session.query(date.name).all()   
    all_names = list(np.ravel(results))

    return jsonify(all_names)

if __name__ == '__main__':
    hw.run(debug=True)