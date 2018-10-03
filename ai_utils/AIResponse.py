
class AIResponse(object):

    def __init__(self, message, entity):
        self.message = message
        self.entity = entity

    def get_message(self):
        return self.message

    def get_entity(self):
        return self.entity
