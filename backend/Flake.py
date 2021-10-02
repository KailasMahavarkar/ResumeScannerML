import random
import re
from flask import Flask, json, render_template, request, redirect, jsonify
from flask_cors import CORS, cross_origin
import Model
import inspect
import Miner
import Rank
import env
from string import ascii_letters
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

            if xfile.content_type == "application/pdf":
                newFileName = env.jp(env.CACHE_PATH, Cleaner.NameGenerator())
                xfile.save(newFileName)
                cleaned_resume = Cleaner.CleanResume(Miner.MinePDF(newFileName))
                
                return jsonify({
                    "msg": cleaned_resume,
                    "result": Model.ProcessData(text=cleaned_resume)
                })
            return jsonify({})
    except Exception as e:
        return jsonify({})



@app.route('/read', methods=['POST'])
def readResume():

    try:
        xdata = request.get_json()
        return jsonify({"result": Rank.singleResume(int(xdata['id']))})  
    except Exception as e:
        return jsonify({"error": "error"})


if __name__ == '__main__':

    app.config['CORS_HEADERS'] = 'Content-Type'
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port, debug=True)
