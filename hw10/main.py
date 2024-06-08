from flask import Flask

import utils
candidates = utils.load_candidates()

app = Flask(__name__)

@app.route("/")
def page_index():

    str_candidates = "<pre>"
    for candidate in candidates.values():
        str_candidates += f"{candidate["name"]} \n{candidate["position"]} \n{candidate["skills"]} \n\n"
    str_candidates += "</pre>"

    return str_candidates

@app.route("/candidate/<int:x>")
def candidate(x):

    foto_candidate = ""
    str_candidate = "<pre>\n"

    candidate = candidates[x]

    foto_candidate = f"<img src = {candidate["picture"]}> </img>"
    str_candidate += f"{candidate["name"]} \n{candidate["position"]} \n{candidate["skills"]} \n\n"
    str_candidate += "<pre>"

    #for key,value in candidates.items():
    #    if int(x) == key:
    #       str_candidate += f"{value["name"]} \n{value["position"]} \n{value["skills"]} \n\n"
    #      foto_candidate = f"<img src = {value["picture"]}>"

    return f"{foto_candidate} \n {str_candidate}"



@app.route("/skills/<skills>")
def skills_(skills):
    str_skills_candidate = "<pre>"
    for key,value in candidates.items():
        set_skills = value["skills"].split(", ")
        if skills in set_skills:
            str_skills_candidate += f"{value["name"]} <br>{value["position"]} <br>{value["skills"]}<br> <br>"
    str_skills_candidate += "<pre>"
    return str_skills_candidate

app.run()
