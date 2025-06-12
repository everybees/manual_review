categories = {
        "Functional Requirements Analysis": [
            ("Ideal response does not fulfill all listed functional requirements.", 2.5),
            ("Only partially fulfills the requirements.", 1.5),
            ("Minor incompleteness but most covered.", 0.5)
        ],
        "Physics/Math Realism Analysis": [
            ("Incorrect or unrealistic physics/math implementation.", 1.5),
            ("Minor errors in constants or formulas.", 1.0),
            ("Mostly realistic, small inconsistencies.", 0.5)
        ],
        "Visual Quality Analysis": [
            ("Object shapes/colors incorrect or inconsistent with prompt.", 2.0),
            ("Minor issues with rendering accuracy.", 1.0),
            ("Mostly consistent visuals with small gaps.", 0.5)
        ],
        "Edge Cases & Potential Bugs": [
            ("Major unhandled edge cases or instability.", 1.5),
            ("Some known edge cases not addressed.", 1.0),
            ("Minor potential bugs or rare issues.", 0.5)
        ],
        "Feedback Incorporation": [
            ("Trainer feedback not addressed.", 1.5),
            ("Partially addressed trainer feedback.", 1.0),
            ("Minor omissions in feedback incorporation.", 0.5)
        ],
        "Code Quality Analysis": [
            ("Unorganized, undocumented, poor naming.", 1.5),
            ("Some inconsistent naming or lack of comments.", 1.0),
            ("Minor style or structure issues.", 0.5)
        ],
        "Language Issues": [
            ("Major grammar/spelling issues.", 1.5),
            ("Some language clarity or grammar errors.", 1.0),
            ("Minor typos or awkward phrasing.", 0.5)
        ],
        "Basic Checks": [
            ("Missing intro, outro, or restart simulation; wrong format.", 2.0),
            ("Some elements missing or improperly formatted.", 1.0),
            ("Minor format deviation.", 0.5)
        ]
    }