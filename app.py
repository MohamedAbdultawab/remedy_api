from flask import Flask, request, jsonify
from .model import get_predictor
from .constants import *


app = Flask(__name__)


@app.route('/remedy', methods=['POST'])
def hello_world():

    question_text = request.json.get('question', None) if request.json else None
    if question_text:
        predictor = get_predictor()
        number_results_to_return = request.json.get('topK', TOP_K)
        returned_results = predictor.predict(question_text,
                                             search_by=SEARCH_SIMILARITY_BY, topk=number_results_to_return, answer_only=ANSWERS_ONLY)
        return jsonify({"question": question_text,
                "answers": returned_results,
                })
    return jsonify({"question": None,
            "answers": [],
            })
