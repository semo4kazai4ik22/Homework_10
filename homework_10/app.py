from functions import load_data, format_candidates, get_uid, get_all_candidates, get_candidate_by_skill

from flask import Flask

app = Flask(__name__)

filename = "candidates.json"

@app.route('/')
def main_page():
    """Вывод кандидатов на главную"""
    candidates: list[dict] = get_all_candidates()
    result: str = format_candidates(candidates)
    return result


@app.route('/candidates/<int:uid>')
def profile_page(uid):
    """Поиск кандидата по id"""
    candidate: dict = get_uid(uid)
    result = f'<img src="{candidate["picture"]}">'
    result += format_candidates([candidate])
    return result


@app.route('/skills/<skill>')
def skills_page(skill):
    """Поиск кандидата по навыку"""
    candidates: list[dict] = get_candidate_by_skill(skill)
    result = format_candidates(candidates)
    return result



if __name__ == "__main__":
    app.run()






