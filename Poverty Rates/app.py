from flask import Flask, jsonify, render_template
import sqlalchemy
from sqlalchemy import create_engine

db = create_engine("mysql://root:baseball1@localhost:3306/Poverty")

app = Flask(__name__)
person ={
    "name":"Nick",
    "age": "27"
}
@app.route("/poverty")
def test():
    return jsonify(person)

@app.route("/api/all")
def all_data():
    poverty_data = {}
    poverty_data["state"]=[]
    poverty_data["county"]=[]
    poverty_data["poverty"]=[]
    poverty_data["above_poverty"]=[]

    poverty= db.execute("SELECT * FROM ob_pv_county;")
    for data in poverty:
        print(data)
        poverty_data["state"].append(data[0])
        poverty_data["county"].append(data[1])
        poverty_data["poverty"].append(data[2])
        poverty_data["above_poverty"].append(data[3])
    return jsonify(poverty_data)

@app.route("/")
def home():
    return render_template("index.html",data=person)



if __name__ =="__main__" :
    app.run(debug=True)

