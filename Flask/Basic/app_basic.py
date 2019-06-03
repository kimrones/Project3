from flask import Flask, render_template
from obesity import OBESITY


app = Flask(__name__)


def get_states(source):
    states = []
    for row in source:
        state = row["State"]
        states.append(state)
    return sorted(states)    

def get_percent(source, state):
    for row in source:
        if state == row["State"]:
            # decode handles accented characters
            percent = row["Percent"]
    return state, percent

@app.route('/')
def index():
    states = get_states(OBESITY)
    # return '<h1>Go to /awards/</h1>'
    return render_template('index_basic.html', states=states)
    # return ('/awards/')

@app.route('/awards/')
def awards():
    states = get_states(OBESITY)
    # pass the sorted list of titles to the template
    return render_template('index_new.html', states=states)


if __name__ == "__main__":
    app.run()