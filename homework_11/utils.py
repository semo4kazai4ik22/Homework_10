import json

__all__ = ['get_candidate',
          'get_candidates_by_name',
          'get_candidates_by_skill',
          'load_candidates_from_json'
          ]

def load_candidates_from_json(path) -> list[dict]:
    """возвращает список всех кандидатов"""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data


def get_candidate(candidate_id: int) -> dict:
    """возвращает одного кандидата по его id"""
    for candidate in load_candidates_from_json("candidates.json"):
        if candidate_id == candidate["id"]:
            return candidate


def get_candidates_by_name(candidate_name: str) -> dict:
    """возвращает кандидатов по имени"""
    candidates = []
    candidate_name = str(candidate_name.lower().strip())
    for candidate in load_candidates_from_json("candidates.json"):
        if candidate_name in candidate["name"].lower().strip():
            candidates.append(candidate)
    return candidates

def get_candidates_by_skill(skill_name: str) -> dict:
    """возвращает кандидатов по навыку"""
    candidates = []
    skill_name = str(skill_name.lower().strip())
    for candidate in load_candidates_from_json("candidates.json"):
        if skill_name in candidate["skills"].lower().strip():
            candidates.append(candidate)
    return candidates





