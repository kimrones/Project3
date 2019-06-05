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

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///National_Obesity_By_State.sqlite"

db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# # reflect the tables
Base.prepare(db.engine, reflect=True)

# Save reference to the table
obesity_data = Base.classes.ob

@app.route('/')
def index():
   
    return render_template('index.html', states=states)

@app.route('/states')
def states():

    sel = [
            obesity_data.state,
            obesity_data.percent, 
            obesity_data.shape__Area,
            obesity_data.pe__length
        ]

    results = db.session.query(*sel).order_by(obesity_data.percent.desc()).limit(10).all()

    states_ob = []

        # Loop through each result
    # for result in results:
    #         # Create primaryzip code key
    #     states_ob[result[0]] = {
    #         "percent":result[1],
    #         "shape":result[2],
    #         "length":result[3]

    #         }

    for result in results:
                # Create primaryzip code key
            states = states_ob.append( {
                "state": result[0],
                "percent":result[1]

                })

    
    # return jsonify(states_ob)
    # for index in range(len(results)):
    #     data = states_ob[index]
    state = [result[0] for result in results]
    percent = [int(result[1]) for result in results]

    print(state)
    #return jsonify(state)
    
   
    trace = {
        "x": state,
        "y": percent,
        "type": "bar"
    }
    
    # print(trace)
    return jsonify(trace)

if __name__ == "__main__":
    app.run(debug=True)