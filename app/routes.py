import traceback

import requests
from flask import request, render_template, send_from_directory, abort, jsonify

from ai_utils import get_ai_response
from app import app
from config import Config
from db_utils import register_sender, register_lead_query
from event_parser.EventResponse import EventResponse
from rest_administer.api_handler import handle_api_call, ApiException


@app.route('/verify_webhook_subscription', methods=["GET"])
def verify_webhook_subscription():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == Config.SUBSCRIPTION_VERIFICATION_TOKEN:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200


@app.route('/handle_event', methods=["POST"])
def handle_event():
    data = request.json
    ev_res = EventResponse(data)
    register_sender(ev_res.get_sender_id())
    ai_response = get_ai_response(ev_res)
    register_lead_query(ai_response, ev_res)
    response = {
        'recipient': {'id': ev_res.get_sender_id()},
        'message': {'text': ai_response.get_message()}
    }
    print(response)
    # resp = requests.post(Config.FACEBOOK_MESSAGE_API+"?access_token=" + Config.FACEBOOK_ACCESS_TOKEN, json=response)


@app.route('/console', methods=['GET'])
def handle_console():
    return render_template("console.html")

@app.route('/js/<path:path>')
def send_js(path):
    try:
        ind = path.index('.js')
        return send_from_directory('templates', path)
    except:
        abort(404)

@app.route('/api/<path:entity>/<path:id>', methods=['GET','PUT','DELETE'])
def api_handlers(entity, id):
    try:
        return jsonify(handle_api_call(entity, id, request.method, request.data)), 200
    except ApiException as error:
        return jsonify({'error':error.__str__()}), 400
    except BaseException as e:
        traceback.print_exc()
        return jsonify({'error': 'internal error'}), 400


@app.route('/api/<path:entity>', methods=['POST', 'GET'])
def api_handlers_with_id(entity):
    try:
        return jsonify(handle_api_call(entity, None, request.method, request.data)), 200
    except ApiException as error:
        return jsonify({'error': error.__str__()}), 400
    except BaseException as e:
        traceback.print_exc()
        return jsonify({'error': 'internal error'}), 400

@app.route('/push_notify', methods=['POST'])
def push_notify():
    data = request.json
    notification = data['message']
    v = {'messages' : [{'text' : notification}]}
    resp = requests.post("https://graph.facebook.com/v2.6/me/message_creatives?access_token=" + 'access-token', json=v)
    res = resp.json()
    print('creative message response:')
    print(res)
    msg_id = res['message_creative_id']
    v2 = {'message_creative_id' : msg_id}
    resp1 = requests.post("https://graph.facebook.com/v2.6/me/broadcast_messages?access_token=" + 'access-token', json=v2)
    print('posting a broadcast message:')
    print(resp1.content)
    return 'ok'