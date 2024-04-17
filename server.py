from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/learn_home')
def learn_home():
    return render_template('learn_home.html')

@app.route('/learn_patterns')
def learn_patterns():
    return render_template('learn_patterns.html')

@app.route('/learn_loops')
def learn_loops():
    return render_template('learn_loops.html')

@app.route('/learn_whorls')
def learn_whorls():
    return render_template('learn_whorls.html')

@app.route('/learn_arches')
def learn_arches():
    return render_template('learn_arches.html')

@app.route('/learn_minutiae')
def learn_minutiae():
    return render_template('learn_minutiae.html')

@app.route('/learn_bifurcation')
def learn_bifurcation():
    return render_template('learn_bifurcation.html')

@app.route('/learn_spur')
def learn_spur():
    return render_template('learn_spur.html')

@app.route('/learn_island')
def learn_island():
    return render_template('learn_island.html')

@app.route('/learn_ridge_ending')
def learn_ridge_ending():
    return render_template('learn_ridge_ending.html')

@app.route('/master_home')
def master_home():
    return render_template('master_home.html')

@app.route('/master_patterns_home')
def master_patterns_home():
    return render_template('master_patterns_home.html')


@app.route('/master_minutiae_home')
def master_minutiae_home():
    return render_template('master_minutiae_home.html')

@app.route('/solve_home')
def solve_home():
    return render_template('solve_home.html')



if __name__ == '__main__':
    app.run(debug=True)