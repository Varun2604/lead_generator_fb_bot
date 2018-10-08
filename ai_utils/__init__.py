from config import Config
from ai_utils.AIResponse import AIResponse
from ai_utils.DialogFlowAIHandler import DialogFlowAIHandler

def get_ai_response(event_response):
    return fulfill_query(event_response.get_message_text())

def fulfill_query(query_string):
    h = DialogFlowAIHandler()
    return h.fulfill_query(query_string)
