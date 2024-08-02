from flask import Flask, request, render_template, send_from_directory
from functions import load_posts
from main.main import main_blueprint
from loader.loader import loader_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

@app.route(f"/{UPLOAD_FOLDER}/<path:path>")
def static_dir(path):
    return send_from_directory(f"{UPLOAD_FOLDER}", path)


app.run(debug=True)

