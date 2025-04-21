from templates.client.src.numbers_api.snippet import execute


class NumbersQuickstart:
    def __init__(self, sinch_client):
        self.sinch_client = sinch_client
        execute(self.sinch_client)
