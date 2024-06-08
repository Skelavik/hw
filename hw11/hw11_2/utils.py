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
    for id,info in load_candidates_from_json().items():
        if candidate_name == info["name"]:
            return info
    return "Кандидата нет"

def get_candidates_by_skill(skill_name):
    candidates_by_skills = []
    for id,info in load_candidates_from_json().items():
        set_skills = info["skills"].split(", ")
        if skill_name in set_skills:
            candidates_by_skills.append({id:info})
    return candidates_by_skills



