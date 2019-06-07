import pandas as pd
import numpy as np
import sqlite3

from flask import Flask, render_template, jsonify
from sqlalchemy.ext.automap import automap_base

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#################################################
# Database Setup
#################################################

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data/National_Obesity_By_State.sqlite"

db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# # reflect the tables
Base.prepare(db.engine, reflect=True)

# Save reference to the table
obesity_data = Base.classes.ob

@app.route('/')
def index():
   
    return render_template('index_new.html', states=states)

@app.route('/states')
def states():

    sel = [
            obesity_data.state,
            obesity_data.percent, 
            obesity_data.shape__Area,
            obesity_data.pe__length
        ]

    results = db.session.query(*sel).all()
    print(results)
        
    states_ob = {}

        # Loop through each result
    for result in results:
            # Create primaryzip code key
        states_ob[result[0]] = {
            "percent":result[1],
            "shape":result[2],
            "length":result[3]

            }

    print(states_ob)
    return jsonify(states_ob)

if __name__ == "__main__":
    app.run(debug=True)