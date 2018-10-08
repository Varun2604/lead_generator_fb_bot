from config import Config

class DefaultAIHandler(object):

    # def __init__(self):
        # self.access_url = Config.AI_ENGINE_FULFILLMENT_API
        # self.access_token = Config.AI_ENGINE_ACCESS_TOKEN

    def fulfill_query(self, query_string):
        raise NotImplementedError('need to implement method')



