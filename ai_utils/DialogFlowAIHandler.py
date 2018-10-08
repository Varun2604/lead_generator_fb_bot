from ai_utils.DefaultAIHandler import DefaultAIHandler
from config import Config
import dialogflow_v2 as dialogflow
from ai_utils.AIResponse import AIResponse

class DialogFlowAIHandler(DefaultAIHandler):

    def __init__(self):
        self.session_client = dialogflow.SessionsClient()
        self.project_id = Config.DIALOG_FLOW_PROJECT_ID
        self.session_id = 1         # increment the session id, do not keep it constant, as we do not want to maintain the session (users change)

    def fulfill_query(self, query_string):
        text_input = dialogflow.types.TextInput(text=query_string, language_code='en')
        query_input = dialogflow.types.QueryInput(text=text_input)
        sess = self.get_session(None)
        print(sess)
        response = self.session_client.detect_intent(session=sess, query_input=query_input)
        return AIResponse(response.query_result.fulfillment_text, response.query_result.intent.display_name)

    def get_session(self, session_id):
        if session_id is None:
            self.session_id += 1
            session_id = self.session_id
        return self.session_client.session_path(self.project_id, session_id)