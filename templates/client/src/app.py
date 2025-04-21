from templates.client.src.numbers_api.numbers_quickstart import NumbersQuickstart
from templates.utils import get_sinch_client, load_config


def main():
    config = load_config()
    sinch_client = get_sinch_client(config)

    try:
        NumbersQuickstart(sinch_client)
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()
