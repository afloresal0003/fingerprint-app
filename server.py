from flask import Flask, render_template, session

app = Flask(__name__)

# Define routes and their corresponding flags
visited_routes = {
    'learn_patterns': False,
    'learn_minutiae': False,
    'learn_loops': False,
    'learn_arches': False,
    'learn_whorls': False,
    'learn_bifurcation': False,
    'learn_spur': False,
    'learn_island': False,
    'learn_ridge_ending': False
}

mastered_concepts = {
    'patterns': False,
    'minutiae': False
}

#Media Datasets
homepage_card_info = [
    {
        "href": "/learn_home",
        "card_image": "https://static.thenounproject.com/png/4365546-200.png",
        "card_title": "LEARN",
        "card_description": "Learn about fingerprint patterns and minutiae!"
    },
    {
        "href": "/master_home",
        "card_image": "https://static.thenounproject.com/png/3241393-200.png",
        "card_title": "MASTER",
        "card_description": "Test your knowledge! Mastery quizzes unlocked after learning a concept"
    },
    {
        "href": "/solve_home",
        "card_image": "https://cdn.icon-icons.com/icons2/3079/PNG/512/detective_crime_man_persona_vatar_icon_191245.png",
        "card_title": "SOLVE",
        "card_description": "Use what you learned to crack the case! Unlocks after perfect scores in MASTER"
    }
]

@app.route('/')
def index():
    master_clickable = (visited_routes['learn_loops'] and visited_routes['learn_arches'] and visited_routes['learn_whorls']) or (visited_routes['learn_bifurcation'] and visited_routes['learn_spur'] and visited_routes['learn_island'] and visited_routes['learn_ridge_ending'])
    learn_green = visited_routes['learn_loops'] and visited_routes['learn_arches'] and visited_routes['learn_whorls'] and visited_routes['learn_bifurcation'] and visited_routes['learn_spur'] and visited_routes['learn_island'] and visited_routes['learn_ridge_ending']
    solve_clickable = mastered_concepts['patterns'] and mastered_concepts['minutiae']
    return render_template('index.html', homepage_card_info=homepage_card_info, master_clickable=master_clickable, learn_green=learn_green, solve_clickable=solve_clickable)

@app.route('/learn_home')
def learn_home():
    patterns_green = visited_routes['learn_loops'] and visited_routes['learn_arches'] and visited_routes['learn_whorls']
    minutiae_green = visited_routes['learn_bifurcation'] and visited_routes['learn_spur'] and visited_routes['learn_island'] and visited_routes['learn_ridge_ending']
    return render_template('learn_home.html', patterns_green=patterns_green, minutiae_green=minutiae_green)

@app.route('/learn_patterns')
def learn_patterns():
    visited_routes['learn_patterns'] = True
    loops_green = visited_routes['learn_loops']
    arches_green = visited_routes['learn_arches']
    whorls_green = visited_routes['learn_whorls']
    return render_template('learn_patterns.html', loops_green=loops_green, arches_green=arches_green, whorls_green=whorls_green)

@app.route('/learn_loops')
def learn_loops():
    visited_routes['learn_loops'] = True
    return render_template('learn_loops.html')

@app.route('/learn_whorls')
def learn_whorls():
    visited_routes['learn_whorls'] = True
    return render_template('learn_whorls.html')

@app.route('/learn_arches')
def learn_arches():
    visited_routes['learn_arches'] = True
    return render_template('learn_arches.html')

@app.route('/learn_minutiae')
def learn_minutiae():
    visited_routes['learn_minutiae'] = True
    bifurcation_green = visited_routes['learn_bifurcation']
    spur_green = visited_routes['learn_spur']
    island_green = visited_routes['learn_island']
    ending_green = visited_routes['learn_ridge_ending']
    return render_template('learn_minutiae.html', bifurcation_green=bifurcation_green, spur_green=spur_green, island_green=island_green, ending_green=ending_green)

@app.route('/learn_bifurcation')
def learn_bifurcation():
    visited_routes['learn_bifurcation'] = True
    return render_template('learn_bifurcation.html')

@app.route('/learn_spur')
def learn_spur():
    visited_routes['learn_spur'] = True
    return render_template('learn_spur.html')

@app.route('/learn_island')
def learn_island():
    visited_routes['learn_island'] = True
    return render_template('learn_island.html')

@app.route('/learn_ridge_ending')
def learn_ridge_ending():
    visited_routes['learn_ridge_ending'] = True
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