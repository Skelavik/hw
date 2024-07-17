from flask import Flask,render_template
import utils

app = Flask(__name__)

@app.route("/<int:x>")
def page_index(x):
    data = utils.get_candidate(x)
    return render_template("card.html",name_candidate=data["name"],positional_candidate=data["position"],skills_candidate=data["skills"],foto_candidate=data["picture"])

@app.route("/")
def show_all_candidate():
    items = utils.load_candidates_from_json()
    return render_template("list.html",items=items)



app.run()