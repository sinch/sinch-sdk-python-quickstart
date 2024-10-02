from sinch.domains.voice.models.svaml.actions import HangupAction
from sinch.domains.voice.models.svaml.instructions import SayInstruction
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def result():
    incoming_call = request.get_json()
    print(incoming_call)

    if (incoming_call['event'] == 'ice'):
        svaml_response = {
            "instructions": [
                SayInstruction(text="Thank you for calling. This call will now end.").as_dict()
            ],
            "action": HangupAction().as_dict()
        }

        return svaml_response, 200

    else:
        return "OK", 200