
class AIResponse(object):

    def __init__(self, message, intend):
        self.message = message
        self.intend = intend

    def get_message(self):
        return self.message

    def get_intend(self):
        return self.intend
