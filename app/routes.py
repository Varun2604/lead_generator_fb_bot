from app import app

from flask import request, render_template
import requests

from config import Config
from event_parser import EventParser,EventResponse
from ai_utils import AIResponse,get_ai_response
from db_utils import register_sender

@app.route('/verify_webhook_subscription', methods=["GET"])
def verify_webhook_subscription():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == Config.SUBSCRIPTION_VERIFICATION_TOKEN:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200


@app.route('/handle_event', methods=["POST"])
def handle_event():
    #TODO verify the facebook event response with reciepient id (check if it the id will come in while getting subscription)
    data = request.json
    ev_res = EventResponse.EventResponse(data)
    register_sender(ev_res.get_sender_id())
    ai_response = get_ai_response(ev_res)
    response = {
        'recipient': {'id': ev_res.get_sender_id()},
        'message': {'text': ai_response.get_message()}
    }
    # print(response)
    resp = requests.post(Config.FACEBOOK_MESSAGE_API+"?access_token=" + Config.FACEBOOK_ACCESS_TOKEN, json=response)


@app.route('/console', methods=['GET'])
def handle_console():
    return render_template("console.html")


