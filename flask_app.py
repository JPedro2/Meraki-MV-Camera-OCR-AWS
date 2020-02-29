from flask import request, Flask
import Meraki_AWS_Script
import credentials
import coffee_demo

flask_app = Flask(__name__)


@flask_app.route("/detect-text", methods=["GET"])
def detect_text():
    Meraki_AWS_Script.snapshot_meraki_camera()
    detected_text = Meraki_AWS_Script.detect_text()
    return detected_text

@flask_app.route("/brew-coffee", methods=["GET"])
def brew_coffee_demo():
    fatigue = coffee_demo.get_fatigue_result()
    coffee_strength = coffee_demo.strength_calc(fatigue)
    make_coffee = coffee_demo.IFTTT_make_coffee(coffee_strength)
    return make_coffee


if __name__ == "__main__":
    flask_app.run(host=credentials.FLASK["Flask_HOST"], port=credentials.FLASK["Flask_PORT"], debug=False)

