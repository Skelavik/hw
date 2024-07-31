from flask import Blueprint, render_template


loader_blueprint = Blueprint('loader_blueprint',__name__, static_folder='static', url_prefix='/post')

@loader_blueprint.route("/form")
def form():
    return render_template('post_form.html')
