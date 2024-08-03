import logging

from flask import Blueprint, render_template, request, send_from_directory
from functions import load_posts, uploads_posts

UPLOAD_FOLDER = "uploads/images"

logging.basicConfig(encoding='utf-8', level=logging.INFO)

loader_blueprint = Blueprint('loader_blueprint',__name__, static_folder='static', url_prefix='/post')

@loader_blueprint.route("/form")
def form():
    return render_template('post_form.html')

@loader_blueprint.route("/upload", methods=['POST'])
def upload():
    try:
        file = request.files.get("picture")
        filename = file.filename
        content = request.values['content']
        posts = load_posts()
        posts.append({
            "pic":f"uploads/images/{filename}",
            "content":content
            })
        uploads_posts(posts)
        file.save(f"uploads/images/{filename}")
        if filename.split('.')[1] not in ['jpeg','png','jpg']:
            logging.info("Файл не той кадировки")
    except FileNotFoundError:
        logging.error("Ошибка загрузки файла")
        return "<h1> Файл не найден  </h1>"
    else:
        return render_template('post_uploaded.html', pic=f"uploads/images/{filename}", content=content)

@loader_blueprint.route(f"{UPLOAD_FOLDER}/<path:path>")
def static_dir(path):
    return send_from_directory(f"{UPLOAD_FOLDER}", path)
