from flask import request
from flask import Flask, jsonify
import datetime
app = Flask(__name__)

@app.route('/track/athome', methods=['POST'])
def athome():
    data = request.get_json(force=True)
    data["timestamp"]=str(datetime.datetime.now())
    return jsonify(data)

@app.route('/localstack/v0.1/user/profile/get-token', methods=['GET'])
def getToken():

    return jsonify({'Data': jsongen (desc, result)})
if __name__ == '__main__':
    app.run(debug=True)
