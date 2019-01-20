from flask import request
from flask import Flask, jsonify
import datetime
app = Flask(__name__)

@app.route('/track/athome', methods=['POST'])
def athome():
    data = request.get_json(force=True)
    data["timestamp"]=str(datetime.datetime.now())
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
