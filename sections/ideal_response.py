categories = {
    "Metadata Adherence": [
        ("Subtopic and Use Case are mismatched, or prompt is generalized and not scenario-specific.", 1.5),
        ("Subtopic or Use Case are partially addressed, or use case is interpreted ambiguously.", 1.0),
        ("Minor naming mismatch or vague connection to the subtopic/use case.", 0.5),
    ],
    "Technical Constraint Adherence": [
        ("Language/library or dimension is completely wrong.", 1.5),
        ("Missing explicit mention of required libraries, or language is assumed but not stated.", 1.0),
        ("Slight format inconsistency.", 0.5),
    ],
    "Interactivity Clarity": [
        ("Interactivity is required but not present (or vice versa).", 1.5),
        ("Interactivity is vaguely described.", 1.0),
        ("Controls or UI elements not clearly explained but hinted.", 0.5),
    ],
    "Prompt Clarity & Structure": [
        ("Prompt is poorly written, grammatically incorrect, or confusing to interpret.", 1.5),
        ("Prompt has some clarity issues or informal wording.", 1.0),
        ("Minor issues (capitalization, passive voice, etc.)", 0.5),
    ],
    "Over-Engineering": [
        ("Includes unrelated physics components/mechanics.", 1.5),
        ("Adds unnecessary extras like animation/audio.", 1.0),
        ("Slightly over-complicated wording.", 0.5),
    ],
    "LLM-Generated Signatures": [
        ("Prompt is copy-pasted, templated or formatted with long dashes.", 1.5),
        ("Heavily templated but partially original.", 1.0),
        ("Some LLM-generated signs but minor.", 0.5),
    ]
}