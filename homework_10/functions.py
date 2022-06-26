import json

filename = "candidates.json"

def load_data(filename) -> list[dict]:
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
        return data


def format_candidates(candidates: list[dict]) -> str:

    candidate = "<pre>"

    for candidate_ in candidates:
        candidate += f"{candidate_['name']}\n"
        candidate += f"{candidate_['position']}\n"
        candidate += f"{candidate_['skills']}\n\n"
    candidate += "</pre>"
    return candidate

def get_all_candidates() -> list[dict]:
    return load_data(filename)


def get_uid(uid: int) -> dict | None:
    candidates = get_all_candidates()

    for candidate in candidates:
        if candidate["id"] == uid:
            return candidate
    return None

def get_candidate_by_skill(skill: str) -> list[dict]:
    candidates = get_all_candidates()
    result = []
    for candidate in candidates:
        if skill in candidate["skills"].lower().split(", "):
            result.append(candidate)
    return result