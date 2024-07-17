from flask import Flask,render_template
import utils

app = Flask(__name__)

@app.route("/")
def show_all_candidate():
    name_candidate = []
    items = utils.load_candidates_from_json()
    for item, item_name in items.items():
        name_candidate.append((item_name["id"],item_name["name"]))
    return render_template("list.html",items=name_candidate)

@app.route("/candidate/<int:x>")
def page_index(x):
    data = utils.get_candidate(x)
    return render_template("card.html",name_candidate=data["name"],
                           positional_candidate=data["position"],
                           skills_candidate=data["skills"],
                           foto_candidate=data["picture"])


@app.route("/search/<candidate_name>")
def search_candidate_name(candidate_name):
    name_candidate = []
    data = utils.get_candidate_by_name(candidate_name)
    count = len(data)
    return render_template("search.html",items=data,count=count)




app.run()