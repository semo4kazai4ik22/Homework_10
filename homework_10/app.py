from functions import load_data

from flask import Flask

app = Flask(__name__)

filename = "candidates.json"

@app.route('/')
def main_page():
    candidates: list[dict] = load_data(filename)
    candidate = "<pre>"

    for candidate_ in candidates:
        candidate += f"{candidate_['name']}\n{candidate_['position']}\n{candidate_['skills']}"
    candidate += "</pre>"
    return candidate
# <pre>
#   Имя кандидата -
#   Позиция кандидата
#   Навыки через запятую
#
#   Имя кандидата -
#   Позиция кандидата
#   Навыки через запятую
#
#   Имя кандидата -
#   Позиция кандидата
#   Навыки через запятую
# <pre>

if __name__ == "__main__":
    app.run()






