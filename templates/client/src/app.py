import logging
from numbers_api.numbers_quickstart import NumbersQuickstart
from sinch_client_helper import get_sinch_client, load_config


def main():
    config = load_config()
    sinch_client = get_sinch_client(config)

    # Set up logging at the INFO level
    logging.basicConfig()
    sinch_client.configuration.logger.setLevel(logging.INFO)
    logger = sinch_client.configuration.logger

    try:
        NumbersQuickstart(sinch_client)
    except Exception as e:
        logger.error(f'Error: {e}')


if __name__ == '__main__':
    main()
