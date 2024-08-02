from flask import Blueprint, render_template, request
from functions import load_posts
import logging

logging.basicConfig(encoding="utf-8", level=logging.INFO)

main_blueprint = Blueprint('main_blueprint',__name__)

@main_blueprint.route('/')
def main_page():
    return render_template('index.html')

@main_blueprint.route('/search')
def search_page():
    search_by = request.args['s']
    logging.info(f"Слово для поиска: {search_by}")
    posts = [x for x in load_posts() if search_by in x['content'].lower()]
    return render_template('post_list.html ',search_by=search_by, posts=posts)


