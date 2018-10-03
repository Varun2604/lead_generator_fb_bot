
from event_parser import EventParser

class EventResponse(object):

    def __init__(self, input):
        self.entry = EventParser.parse_webhook_event(input)
        self.parsed_input = EventParser.parse_message_event(self.entry, True)

    def is_postback_event(self):
        return self.parsed_input['is_postback']

    def is_message_event(self):
        return not self.parsed_input['is_postback']

    def get_sender_id(self):
        return self.entry['sender']['id']

    def get_message_text(self):
        if 'message_text' in self.parsed_input:
            return self.parsed_input['message_text']
        return None

    def get_postback_payload(self):
        if 'postback_payload' in self.parsed_input:
            return self.parsed_input['postback_payload']
        return None