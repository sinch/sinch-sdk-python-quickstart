import os
from sinch import SinchClient


sinch_client = SinchClient(
    key_id=os.getenv("KEY_ID"),
    key_secret=os.getenv("KEY_SECRET"),
    project_id=os.getenv("PROJECT_ID")
)
