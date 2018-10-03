from app import app

from flask import request
import requests

from config import Config
from event_parser import EventParser,EventResponse
from ai_utils import AIResponse,get_ai_response

@app.route('/verify_webhook_subscription', methods=["GET"])
def verify_webhook_subscription():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == Config.SUBSCRIPTION_VERIFICATION_TOKEN:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200


@app.route('/', methods=["POST"])
def handle_incoming():
    data = request.json
    ev_res = EventResponse(data)
    ai_response = get_ai_response(ev_res)
    response = {
        'recipient': {'id': ev_res.get_sender_id()},
        'message': {'text': ai_response.get_message()}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + Config.FACEBOOK_ACCESS_TOKEN, json=response)
