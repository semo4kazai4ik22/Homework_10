from utils import *
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def page_index():
    candidates = load_candidates_from_json("candidates.json")
    return render_template("list.html", candidates=candidates)


@app.route('/candidate/<int:uid>')
def page_card(uid):
    candidate = get_candidate(uid)
    return render_template("card.html", candidate=candidate)


@app.route('/search/<candidate_name>')
def page_search(candidate_name):
    candidates: list = get_candidates_by_name(candidate_name)

    return render_template("search.html", candidates=candidates)


@app.route('/skill/<skill_name>')
def page_skill(skill_name):
    candidates: list = get_candidates_by_skill(skill_name)
    skill_name = skill_name

    return render_template("skill.html", candidates=candidates, skill_name=skill_name)

if __name__ == "__main__":
    app.run()

