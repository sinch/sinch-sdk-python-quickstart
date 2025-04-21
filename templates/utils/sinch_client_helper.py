import os
import configparser
from pathlib import Path
from sinch import SinchClient


def load_config():
    """
    Load configuration from config.ini file in the root directory.
    Returns a dictionary of configuration values.
    """
    project_root = Path(__file__).resolve().parent.parent.parent
    env_file = project_root / 'config.ini'

    if not env_file.exists():
        raise FileNotFoundError(f"Could not find config.ini file in the root directory: {env_file}")

    config = configparser.ConfigParser()
    config.read(env_file)

    config_dict = {}
    for section in config.sections():
        for key, value in config.items(section):
            config_dict[key.upper()] = value

    return config_dict


def get_property(property_name: str) -> str:
    """
    Get a property from environment variables.

    Args:
        property_name: Name of the property to retrieve

    Returns:
        str: Property value or empty string if not found
    """
    return os.environ.get(property_name) or ''


def get_sinch_client(config) -> SinchClient:
    """
    Create and return a configured SinchClient instance.

    Returns:
        SinchClient: Configured Sinch client instance
    """
    project_id = config.get('SINCH_PROJECT_ID')
    key_id = config.get('SINCH_KEY_ID')
    key_secret = config.get('SINCH_KEY_SECRET')

    return SinchClient(
        project_id=project_id,
        key_id=key_id,
        key_secret=key_secret,
    )
