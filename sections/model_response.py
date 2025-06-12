categories = {
    "Runtime Errors": [
        ("Complete failure to execute (e.g., crash on load, syntax errors).", 3.0),
        ("Crash/freeze during core functionality (e.g., due to undefined function).", 2.0),
        ("Recoverable errors in non-critical features.", 1.0),
        ("Minor cosmetic or edge-case warnings.", 0.5),
    ],
    "Performance Issues": [
        ("Simulation unusable: extreme lag or browser crash.", 3.0),
        ("Severe degradation: persistent lag or slowdowns.", 2.0),
        ("Occasional stutter or short delays.", 1.0),
        ("Imperceptible lag or short delays during peak loads.", 0.5),
    ],
    "Visual Specification Issues": [
        ("Key elements missing or incorrect, simulation incomprehensible.", 3.0),
        ("Essential visual flaws hindering understanding.", 2.0),
        ("Visible deviations affecting aesthetics.", 1.0),
        ("Subtle imperfections requiring close inspection.", 0.5),
    ],
    "Simulation Logic Issues": [
        ("Core physics broken, no collision detection.", 3.0),
        ("Frequent unrealistic behavior affecting objectives.", 2.0),
        ("Occasional physics inaccuracies.", 1.0),
        ("Minor deviations from ideal behavior.", 0.5),
    ]
}