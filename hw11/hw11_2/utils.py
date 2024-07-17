import json

def load_candidates_from_json():
    with open("candidates.json", "r", encoding='UTF8') as file:
        candidates = json.load(file)
        candidates_ = {}
        for i in candidates:
            candidates_[i['id']] = i
    return candidates_

def get_candidate(candidate_id):
    data = load_candidates_from_json()
    return data[candidate_id]

def get_candidate_by_name(candidate_name):
    data_by_name = []
    fio_in_request = candidate_name.split(" ")
    """Сначало имя, потом фамилия"""
    for id,info in load_candidates_from_json().items():
        fio_in_data = info["name"].split(" ")
        if fio_in_request[0] == fio_in_data[0]:
            data_by_name.append((id,info["name"]))
    if len(data_by_name) == 0:
        return "Кандидата нет"
    else:
        return data_by_name

def get_candidates_by_skill(skill_name):
    candidates_by_skills = []
    for id,info in load_candidates_from_json().items():
        set_skills = info["skills"].split(", ")
        if skill_name in set_skills:
            candidates_by_skills.append((id,info["name"]))
    return candidates_by_skills



