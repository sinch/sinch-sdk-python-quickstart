from flask import request, Response


class NumbersController:
    def __init__(self, sinch_client, webhooks_secret):
        self.sinch_client = sinch_client
        self.webhooks_secret = webhooks_secret
        self.logger = self.sinch_client.configuration.logger

    def numbers_event(self):
        headers = dict(request.headers)
        body_str = request.raw_body.decode('utf-8') if request.raw_body else ''

        webhooks_service = self.sinch_client.numbers.webhooks(self.webhooks_secret)

        valid_auth = webhooks_service.validate_authentication_header(
            headers=headers,
            json_payload=body_str
        )

        if not valid_auth:
            self.logger.warning('Invalid authentication header')
            return Response(status=401)
        else:
            self.logger.info('Valid authentication header')

        event = webhooks_service.parse_event(body_str)

        self.logger.info(f'Received event: {event}')

        return Response(status=200)
