
import utils
candidates = utils.load_candidates()

def skills_(skills):
    str_skills_candidate = ("<pre>")
    for key,value in candidates.items():
        set_skills = value["skills"].split(", ")
        if skills in set_skills:
            str_skills_candidate += f"{value["name"]} <br> {value["position"]} <br> {value["skills"]} <br> <br>"
    str_skills_candidate += ("/pre")
    return str_skills_candidate

print(skills_(input()))
