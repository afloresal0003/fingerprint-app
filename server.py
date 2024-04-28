from flask import Flask, render_template

app = Flask(__name__)

# Define routes and their corresponding flags to track user traffic 
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

#Page Content Datasets
homepage_card_info = [
    {
        "href": "/learn_home",
        "card_image": "https://static.thenounproject.com/png/4365546-200.png",
        "card_title": "LEARN",
        "card_description": "Learn about fingerprint patterns and minutiae!",
        "card_context": ""
    },
    {
        "href": "/master_home",
        "card_image": "https://static.thenounproject.com/png/3241393-200.png",
        "card_title": "MASTER",
        "card_description": "Test your knowledge!",
        "card_context": "Perfect scores = concept mastery!"
    },
    {
        "href": "/solve_home",
        "card_image": "https://cdn.icon-icons.com/icons2/3079/PNG/512/detective_crime_man_persona_vatar_icon_191245.png",
        "card_title": "SOLVE",
        "card_description": "Use what you learned to crack the case!",
        "card_context": "Unlocks after perfect scores in MASTER"
    }
]

learn_loops_info = {
   "pattern_title": "LOOPS",
   "type_description": "There are 2 special kinds of loops we'll focus on. Move onto the next pattern when you feel you can tell the difference between each kind of loop.",
   "subtypes_info": [{
         "subtype_title": "Plain Loop",
         "subtype_images": ["https://www.forensicsciencesimplified.org/prints/img/Loop.png", 
                     "https://assets-global.website-files.com/61845f7929f5aa517ebab941/64081c4d2c0f29619291c5b6_5)%20Ulnar%20loop.jpg", 
                     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-d81eUjxEjDoOf6jwv_nbf4FRYKi5vCDdrkScdiS7Tg&s"],
         "subtype_description": "A plain loop pattern typically features ridges that enter from one side of the impression, curve around, and exit from the same side."
      },
      {
         "subtype_title": "Double Loop",
         "subtype_images": ["https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/finger-print-double-loop-whorl-vcnw.jpg", 
                     "https://assets-global.website-files.com/61845f7929f5aa517ebab941/64081cef3ef911d8f8d87126_7)%20Double%20loop.jpg", 
                     "https://i.pinimg.com/originals/89/96/50/899650117c470b303c2efcd5f0cd2325.gif"],
         "subtype_description": "A double loop, in contrast, exhibits two separate loop formations within the fingerprint, often with ridges curving in opposite directions."
      }],
   "next_subtype": "ARCHES",
   "prev_href": "/learn_patterns",
   "next_href": "/learn_arches"
}

learn_arches_info = {
   "pattern_title": "ARCHES",
   "type_description": "There are 2 special kinds of arches we'll focus on. Move onto the next pattern when you feel you can tell the difference between each kind of arch.",
   "subtypes_info": [{
         "subtype_title": "Plain Arch",
         "subtype_images": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQN6L1pb2UDedQGf4_-lN92N75fi_fcPlx1N3lcSuWCQVR1f8bufbFU6McX6QqpsTZ3o_g&usqp=CAU", 
                     "https://www.forensicsciencesimplified.org/prints/img/PlainArch.png", 
                     "https://getsmarteye.com/wp-content/uploads/2022/01/arch.jpg"],
         "subtype_description": "Plain arches exhibit a simple, rounded ridge flow from one side to the other."
      },
      {
         "subtype_title": "Tented Arch",
         "subtype_images": ["https://assets-global.website-files.com/61845f7929f5aa517ebab941/64081d9a9c2db7518dc2a6e6_10)%20Tented%20arch.jpg", 
                     "https://www.researchgate.net/publication/224087067/figure/fig6/AS:668490264506368@1536391907009/The-Arches-a-Tented-Arch-TA-and-b-Plain-Arch-PA.ppm", 
                     "https://o.quizlet.com/i/E7zUFbcC75G6IGk7y3slzQ.jpg"],
         "subtype_description": "Tented arches feature a more pronounced and sharper peak in the center of the pattern, resembling the peak of a tent."
      }],
   "next_subtype": "WHORLS",
   "prev_href": "/learn_patterns",
   "next_href": "/learn_whorls"
}

learn_whorls_info = {
   "pattern_title": "WHORLS",
   "type_description": "There are 3 special kinds of whorls we'll focus on. Carry on when you feel you can tell the difference between each kind of whorl.",
   "subtypes_info": [{
         "subtype_title": "Plain Whorl",
         "subtype_images": ["https://www.forensicsciencesimplified.org/prints/img/Whorl.png", 
                     "https://getsmarteye.com/wp-content/uploads/2022/01/whorl.jpg", 
                     "https://media.istockphoto.com/id/487256965/vector/fingerprint.jpg?s=612x612&w=0&k=20&c=F-ZOjn8CbKXIELkOQPUzOutEuUHppzeY8KJa88mVxdU="],
         "subtype_description": "A plain whorl is characterized by circular or spiral ridges that encircle a central point."
      },
      {
         "subtype_title": "Accidental Whorl",
         "subtype_images": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVP2cDQrpkPbfA949FAYWtqPZQaDVrf6w5gvr2tFtoCw&s", 
                     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLlVUTNqmOMOUQYbqJo1GWDUZ3_QbxLONQIPBFiItxtvOJUDYgYOxc2oemnQEnRLrz-uw&usqp=CAU", 
                     "https://c8.alamy.com/zooms/9/78953e77b5d5430994361135852ec309/rhk610.jpg"],
         "subtype_description": "An accidental whorl displays irregular patterns with often no discernible central point."
      },
      {
         "subtype_title": "Central Pocket Whorl",
         "subtype_images": ["https://upload.wikimedia.org/wikipedia/commons/a/a8/Central_Pocket_Loop_Whorl_in_a_right_little_finger.jpg", 
                     "https://tholath.files.wordpress.com/2009/10/central-pocket-loop.jpg?w=584", 
                     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBjiTsc7FYX6Gzi7Ura6c9hOXziYeOYEXIpKAEK-Rfw_GOybbC6VHRUoKCvPKTux8lnOA&usqp=CAU"],
         "subtype_description": "A central pocket whorl is distinguished by a noticeable indentation or pocket at its center."
      }],
   "next_subtype": "LOOPS",
   "prev_href": "/learn_patterns",
   "next_href": "/learn_loops"
}

learn_bifurcation_info = {
    "minutiae_title": "BIFURCATION",
    "minutiae_images": ["https://www.researchgate.net/publication/342419519/figure/fig1/AS:908189398749185@1593540634677/Typical-Fingerprint-Features-Termination-and-Bifurcation-points.jpg", "https://www.mdpi.com/sensors/sensors-24-00664/article_deploy/html/images/sensors-24-00664-g002-550.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFDcmVBrwLtA-yB-Zh_20h62LiwBbLqKo-nMyxnr_i3wcB47ZbhmJR_B8SFV7S4VUfnUY&usqp=CAU"],
    "minutiae_description": "A fingerprint bifurcation is characterized by a single ridge dividing into two separate ridges, resembling a Y-shaped split within the fingerprint pattern.",
    "next_minutiae": "SPUR",
    "prev_href": "/learn_minutiae",
    "next_href": "/learn_spur"
}

learn_spur_info = {
    "minutiae_title": "SPUR",
    "minutiae_images": ["https://accessdl.state.al.us/AventaCourses/access_courses/forensic_sci_ua_v22/03_unit/03-05/images/spur_oldcourse.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlSWfpqiV6qVA52AXHEpRdy0B51DD1JYi7-y7iolLTdA&s", "https://image.slidesharecdn.com/fingerprintsandridgecharacteristics-160307185226/85/fingerprints-and-ridge-characteristics-21-320.jpg"],
    "minutiae_description": "A fingerprint spur is characterized by a ridge that branches off from the main ridge and reconnects or ends after a short distance, resembling a small protrusion or spur along the ridge pattern.",
    "next_minutiae": "ISLAND",
    "prev_href": "/learn_minutiae",
    "next_href": "/learn_island"
}

learn_island_info = {
    "minutiae_title": "ISLAND",
    "minutiae_images": ["https://accessdl.state.al.us/AventaCourses/access_courses/forensic_sci_ua_v22/03_unit/03-05/images/shortridge_oldcourse.jpg", "https://image.slidesharecdn.com/fingerprintsandridgecharacteristics-160307185226/85/fingerprints-and-ridge-characteristics-18-320.jpg", "https://cdn.imgbin.com/18/4/11/imgbin-automated-fingerprint-identification-minutiae-biometrics-ridge-island-finger-touch-MZaPQp0ShZs2Bm7H1upbSJmK8.jpg"],
    "minutiae_description": "A fingerprint island is characterized by a small area within the fingerprint where the ridge structure is surrounded by two or more diverging ridges, resembling an isolated island amidst the surrounding ridges.",
    "next_minutiae": "RIDGE ENDING",
    "prev_href": "/learn_minutiae",
    "next_href": "/learn_ridge_ending"
}

learn_ridge_ending_info = {
    "minutiae_title": "RIDGE ENDING",
    "minutiae_images": ["https://accessdl.state.al.us/AventaCourses/access_courses/forensic_sci_ua_v22/03_unit/03-05/images/endingridge_oldcourse.jpg", "https://image.slidesharecdn.com/fingerprintsandridgecharacteristics-160307185226/85/fingerprints-and-ridge-characteristics-16-320.jpg", "https://file.techscience.com/files/iasc/2023/TSP_IASC-36-2/TSP_IASC_31692/TSP_IASC_31692/Images/IASC_31692-fig-1.png/mobile_webp"],
    "minutiae_description": "A fingerprint ridge ending is marked by a ridge that abruptly terminates without branching",
    "next_minutiae": "BIFURCATION",
    "prev_href": "/learn_minutiae",
    "next_href": "/learn_bifurcation"
}

learn_homepage_info = {
    "module_title": "LEARN",
    "module_description": "What would you like to learn about today?",
    "card_info": [
        {
            "href": "/learn_patterns",
            "card_image": "https://pngimg.com/d/fingerprint_PNG85.png",
            "card_title": "Patterns",
        },
        {
            "href": "/learn_minutiae",
            "card_image": "https://cdn2.iconfinder.com/data/icons/crime-law-and-justice-2-1/85/fingerprint_fingerprints_analysis_evidence_identification_investigation-512.png",
            "card_title": "Minutiae",
        }
    ]
}

master_homepage_info = {
    "module_title": "MASTER",
    "module_description": "What would you like to master today?",
    "card_info": [
        {
            "href": "/master_patterns_home",
            "card_image": "https://pngimg.com/d/fingerprint_PNG85.png",
            "card_title": "Patterns",
        },
        {
            "href": "/master_minutiae_home",
            "card_image": "https://cdn2.iconfinder.com/data/icons/crime-law-and-justice-2-1/85/fingerprint_fingerprints_analysis_evidence_identification_investigation-512.png",
            "card_title": "Minutiae",
        }
    ]
}

master_patterns_transition_info = {
    "quiz_title": "MASTER: PATTERNS",
    "quiz_description": "Get ready! Each question is timed. Make sure to get a perfect score for mastery on this concept.",
    "go_href": "/master_patterns/<int:question_id>"
}

master_minutiae_transition_info = {
    "quiz_title": "MASTER: MINUTIAE",
    "quiz_description": "Get ready! Each question is timed. Make sure to get a perfect score for mastery on this concept.",
    "go_href": "/master_minutiae/<int:question_id>"
}

pattern_questions = {

    "1": {
        "id": "1",
        "image": "https://www.google.com",
        "question": "What pattern is this?",
        "options": ["Plain Whorl", "Tented Arch", "Central Pocket Whorl"]
    },
    "2": {
        "id": "2",
        "image": "https://www.google.com",
        "question": "What pattern is this?",
        "options": ["Plain Arch", "Tented Arch", "Plain Loop"]
    },
    "3": {
        "id": "3",
        "image": "https://www.google.com",
        "question": "What pattern is this?",
        "options": ["Accidental Whorl", "Double Loop", "Central Pocket Whorl"]
    },
    "4": {
        "id": "4",
        "image": "https://www.google.com",
        "question": "What pattern is this?",
        "options": ["Plain Whorl", "Central Pocket Whorl", "Accidental Whorl"]
    },
    "5": {
        "id": "5",
        "image": "https://www.google.com",
        "question": "What pattern is this?",
        "options": ["Plain Arch", "Plain Loop", "Plain Whorl"]
    },
    "6": {
        "id": "6",
        "image": "https://www.google.com",
        "question": "What pattern is this?",
        "options": ["Plain Whorl", "Central Pocket Whorl", "Double Loop"]
    },
    "7": {
        "id": "7",
        "image": "https://www.google.com",
        "question": "What pattern is this?",
        "options": ["Plain Whorl", "Plain Loop", "Central Pocket Whorl"]
    }

}

minutiae_questions = {

    "1": {
        "id": "1",
        "image": "https://www.google.com",
        "question": "How many bifurcations are in the bottom right quadrant of this fingerprint?",
        "options": ["2", "5", "3"]
    },
    "2": {
        "id": "2",
        "image": "https://www.google.com",
        "question": "Name all minutiae present in top left corner of this fingerprint.",
        "answers": ["Bifurcation", "Ridge Ending", "Island"]
    },
    "3": {
        "id": "3",
        "image": "https://www.google.com",
        "question": "Label all letters with the appropriate minutiae.",
        "A": "Ridge Ending",
        "B": "Island",
        "C": "Spur",
        "D": "Bifurcation",
        "E": "Island",
        "F": "Bifurcation",
        "G": "Spur"
    },
    "4": {
        "id": "4",
        "image": "https://www.google.com",
        "question": "What pattern is this?",
        "single_answer": "spur"
    }

}

pattern_answers = [0, 0, 0, 0, 0, 0, 0] # 0 = incorrect, 1 = correct

minutiae_answers = [0, 0, 0, 0] # 0 = incorrect, 1 = correct

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
    return render_template('module_home.html', data=learn_homepage_info, patterns_green=patterns_green, minutiae_green=minutiae_green)

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
    return render_template('learn_pattern_layout.html', data=learn_loops_info)

@app.route('/learn_whorls')
def learn_whorls():
    visited_routes['learn_whorls'] = True
    return render_template('learn_pattern_layout.html', data=learn_whorls_info)

@app.route('/learn_arches')
def learn_arches():
    visited_routes['learn_arches'] = True
    return render_template('learn_pattern_layout.html', data=learn_arches_info)

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
    return render_template('learn_minutiae_layout.html', data=learn_bifurcation_info)

@app.route('/learn_spur')
def learn_spur():
    visited_routes['learn_spur'] = True
    return render_template('learn_minutiae_layout.html', data=learn_spur_info)

@app.route('/learn_island')
def learn_island():
    visited_routes['learn_island'] = True
    return render_template('learn_minutiae_layout.html', data=learn_island_info)

@app.route('/learn_ridge_ending')
def learn_ridge_ending():
    visited_routes['learn_ridge_ending'] = True
    return render_template('learn_minutiae_layout.html', data=learn_ridge_ending_info)

@app.route('/master_home')
def master_home():
    return render_template('module_home.html', data=master_homepage_info)

@app.route('/master_patterns_home')
def master_patterns_home():
    return render_template('master_transition_screen.html', data=master_patterns_transition_info)

@app.route('/master_minutiae_home')
def master_minutiae_home():
    return render_template('master_transition_screen.html', data=master_minutiae_transition_info)

@app.route('/solve_home')
def solve_home():
    return render_template('solve_home.html')

@app.route('/quiz_pattern/<question_num>')
def quiz_pattern(question_num):
    pattern_question = pattern_questions[str(question_num)]
    return render_template('quiz_pattern.html', quiz_question=pattern_question)

#ADD POST INFORMATION TO RECEIVE WHETHER THE ANSWER IS CORRECT OR NOT

@app.route('/quiz_minutiae/<question_num>')
def quiz_minutiae(question_num):
    minutiae_question = minutiae_questions[str(question_num)]
    return render_template('quiz_minutiae.html', quiz_question=minutiae_question)

@app.route('/quiz_pattern/results')
def quiz_results():
    quiz_results = sum(pattern_answers)
    return render_template('quiz_results.html', quiz_results=quiz_results)



if __name__ == '__main__':
    app.run(debug=True)