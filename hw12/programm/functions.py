import json
POST_PATH = "posts.json"

def load_posts():
    with open(POST_PATH,'r',encoding='UTF8') as file:
        posts = json.loads(file)
    return posts
