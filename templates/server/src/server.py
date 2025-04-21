from flask import Flask, request
from templates.server.src.numbers_api.controller import NumbersController
from templates.utils import get_sinch_client, load_config

app = Flask(__name__)

config = load_config()
port = int(config.get("SERVER_PORT") or 3001)
webhooks_secret = config.get("NUMBERS_WEBHOOKS_SECRET")
sinch_client = get_sinch_client(config)

numbers_controller = NumbersController(sinch_client, webhooks_secret)


# Middleware to capture raw body
@app.before_request
def before_request():
    request.raw_body = request.get_data()


app.add_url_rule('/NumbersEvent', methods=['POST'], view_func=numbers_controller.numbers_event)

if __name__ == '__main__':
    app.run(port=port)
