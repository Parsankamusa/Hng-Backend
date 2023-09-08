from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def info():
    slack_name = request.args.get('Slack name', default="Musa Parsanka", type=str)
    track = request.args.get('track', default="backend", type=str)

    current_day = datetime.datetime.utcnow().strftime('%A')
    utc_time = datetime.datetime.utcnow().isoformat()

    github_file_url = "https://github.com/Parsankamusa/ZURI-INTERNSHIP/blob/main/STAGE%201/Main.py"
    github_repo_url = "https://github.com/Parsankamusa/ZURI-INTERNSHIP/tree/main"

    # Create the JSON object to be returned
    info = {
        "slack_name": 'Musa Parsanka',
        "current_day": 'Friday',
        "utc_time": '2023-09-08T15:11:00Z',
        "track": 'backend',
        "github_file_url": 'https://github.com/Parsankamusa/ZURI-INTERNSHIP/blob/main/STAGE%201/Main.py',
        "github_repo_url": 'https://github.com/Parsankamusa/ZURI-INTERNSHIP/tree/main',
        "status_code": 200
    }

    return jsonify(info)

if __name__ == "__main__":
    app.run(debug=True)
