from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def info():
    slack_name = request.args.get('Slack name', default="Musa Parsanka", type=str)
    track = request.args.get('track', default="backend", type=str)

    current_day = datetime.datetime.utcnow().strftime('%A')
    utc_time = datetime.datetime.utcnow().isoformat()

    github_file_url = ""
    github_repo_url = ""

    # Create the JSON object to be returned
    info = {
        "slack_name": 'Musa Parsanka',
        "current_day": 'Friday',
        "utc_time": '9:00 am',
        "track": 'backend',
        "github_file_url": '',
        "github_repo_url": '',
        "status_code": 200
    }

    return jsonify(info)

if __name__ == "__main__":
    app.run(debug=True)
