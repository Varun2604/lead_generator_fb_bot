

class EventParser(object):

    # {
    #     "object": "page",
    #     "entry": [
    #         {
    #             "id": "<PAGE_ID>",
    #             "time": 1458692752478,
    #             "messaging": [
    #               ...
    #             ]
    #         }
    #     ]
    # }
    def parse_webhook_event(fb_input):
        messaging_obj = fb_input['entry'][0]['messaging']
        if len(messaging_obj) == 0:
            raise Exception('Invalid Input')

        return messaging_obj[0]

    # {
    #     "sender": {
    #         "id": "<PSID>"
    #     },
    #     "recipient": {
    #         "id": "<PAGE_ID>"
    #     },
    #     "timestamp": 1458692752478,
    #     "message": {
    #         "mid": "mid.1457764197618:41d102a3e1ae206a38",
    #         "text": "hello, world!",
    #         "quick_reply": {
    #             "payload": "<DEVELOPER_DEFINED_PAYLOAD>"
    #         }
    #     }
    # }
    def parse_message_event(fb_input, is_webhook_event_parsed=False):
        entry = fb_input
        if not is_webhook_event_parsed:
            entry = EventParser.parse_webhook_event(fb_input)

        sender_id = entry['sender']['id']
        if 'message' in entry:
            return {'sender_id' : sender_id, 'message_text' : entry['message']['text'], 'is_postback' : True}
        elif 'postback' in entry :
            return EventParser.parse_postback_event(entry, True)

    # {
    #     "sender": {
    #         "id": "<PSID>"
    #     },
    #     "recipient": {
    #         "id": "<PAGE_ID>"
    #     },
    #     "timestamp": 1458692752478,
    #     "postback": {
    #         "title": "<TITLE_FOR_THE_CTA>",
    #         "payload": "<USER_DEFINED_PAYLOAD>",
    #         "referral": {
    #             "ref": "<USER_DEFINED_REFERRAL_PARAM>",
    #             "source": "<SHORTLINK>",
    #             "type": "OPEN_THREAD",
    #         }
    #     }
    # }
    def parse_postback_event(fb_input, is_webhook_event_parsed=False):
        entry = fb_input
        if not is_webhook_event_parsed:
            entry = EventParser.parse_webhook_event(fb_input)

        return {'sender_id': entry['sender']['id'], 'postback_payload': entry['postback']['payload'], 'is_postback': True}