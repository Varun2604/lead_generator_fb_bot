from app import app
from flask import request
from config import Config


# @app.route('/')
# @app.route('/index')
# def index():
#     return "Hello, World!"

@app.route('/verify_webhook_subscription', methods=["GET"])
def verify_webhook_subscription():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == Config.SUBSCRIPTION_VERIFICATION_TOKEN:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200