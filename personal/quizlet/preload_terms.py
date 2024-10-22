"""Preset sets of terms to come back to"""

org_terms: dict[str, str] = {
    "mushroom": "fungi",
    "dog": "animal",
    "tree": "plant",
    "Bleep-Blorp: Devourer of World": "alien",
}

astr_terms: dict[str, str] = {
    "Earth": "planet",
    "Venus": "hot planet",
    "Jupiter": "big planet",
    "Mercury": "tiny planet",
    "Pluto": "not a planet :(",
}

# if you add more preload terms sets, add if statements in find_preload_set in main
# also update set_name_catalog
# I KNOW this system is imperfect but it's what I've got for now

set_name_catalog: list[str] = ["org_terms", "astr_terms"]
