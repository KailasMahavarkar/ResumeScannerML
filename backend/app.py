import random
import re
from flask import Flask,  request, jsonify
from flask_cors import CORS
import Model
import Miner
import Rank
import env
import Cleaner
import os


app = Flask(__name__)
cors = CORS(app)


@app.route('/req', methods=['POST'])
def runAPI():
    text_string = request.get_json()
    try:
        if text_string['text'] is not None:
            result = Rank.RankResume(text=text_string['text'])
            return jsonify({"result": result})
        return jsonify({})
    except Exception as e:
        return jsonify({})


@app.route('/scan', methods=['POST'])
def runREQ():
    try:
        if request.files.to_dict(flat=False)['file']:
            xfile = request.files['file']
            minerResult = Miner.MinePDF(xfile)

            if xfile.content_type == "application/pdf":
                if (minerResult is not False):
                    cleaned_resume = Cleaner.CleanResume(minerResult)
                    return jsonify({
                        "msg": cleaned_resume,
                        "success": "success",
                        "result": Model.ProcessData(text=cleaned_resume)
                    })
            return jsonify({
                "msg": "resume is incorrect or corrupt",
                "success": "failed",
                "error": "Client Error"
            })
    except Exception as e:
        print(e)
        return jsonify({
            "msg": "could not scan resume",
            "success": "failed",
            "error": "Server Error"
        })


@app.route('/read', methods=['POST'])
def readResume():
    try:
        xdata = request.get_json()
        return jsonify({"result": Rank.singleResume(int(xdata['id']))})
    except Exception as e:
        return jsonify({"error": "error"})


@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "msg": "Welcome to ResumeRanker API",
        "success": "success"
    })


@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def allroutes(u_path):
    return jsonify({
        "msg": "bad request",
        "success": "failed",
        "error": "404 | url not found",
    })


if __name__ == '__main__':
    app.config['CORS_HEADERS'] = 'Content-Type'
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port, debug=True)
