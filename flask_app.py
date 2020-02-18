from flask import request, Flask
import Meraki_AWS_Script
import credentials

flask_app = Flask(__name__)


@flask_app.route("/detect-text", methods=["GET"])
def detect_text():
    Meraki_AWS_Script.snapshot_meraki_camera()
    detected_text = Meraki_AWS_Script.detect_text()
    return detected_text


if __name__ == "__main__":
    flask_app.run(host=credentials.FLASK["Flask_HOST"], port=credentials.FLASK["Flask_PORT"], debug=False)

