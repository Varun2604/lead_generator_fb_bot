from ai_utils.AIResponse import AIResponse

def get_ai_response(event_response):
    return AIResponse(event_response.get_message_text(), None)
