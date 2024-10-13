import json

def post_data_load():
    """Загрузка постов"""
    with open("data/posts.json", "r", encoding='utf-8')as file:
        data = json.load(file)
    return data

def comments_data_load():
    """Загрузка коментариев постов"""
    with open("data/comments.json", "r", encoding='utf-8')as file:
        data = json.load(file)
    return data


def get_post_all():
    return post_data_load()

def get_posts_by_user(user_name):
    """Возращает посты опрделенного пользователя"""
    post_by_user = []
    data = post_data_load()
    for user in data:
        if user["poster_name"] == user_name:
            post_by_user.append(user)
    return post_by_user

def get_comments_by_post_id(post_id):
    """Возращает комментарии определнного поста"""
    comments_by_post_id = []
    data = comments_data_load()
    for comments in data:
        if comments["post_id"] == post_id:
            comments_by_post_id.append(comments)
    return comments_by_post_id

def search_for_post(query):
    """Ищет посты по ключевому слову"""
    pk_posts = []
    data = post_data_load()
    for querys in data:
        content = querys["content"]
        if query in content:
            pk_posts.append(querys["pk"])
    return pk_posts

def get_post_by_pk(pk):
    """Ищем пост по его индефикатуру pk"""
    data = post_data_load()
    for pk_posts in data:
        if pk_posts["pk"] == pk:
            return pk_posts

print(get_post_by_pk(1))


