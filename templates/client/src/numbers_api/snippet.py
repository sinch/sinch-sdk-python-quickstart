# Replace the code below with any snippet from:
# https://github.com/sinch/sinch-sdk-python-snippets
def execute(sinch_client):
    print("Snippet execution: Numbers service")


# Example usage:
# Let's say you're using the snippet from  snippets/available_regions/list/snippet.py:
#
# from sinch import SinchClient
#
# sinch_client = SinchClient(
#     project_id="YOUR_PROJECT_ID",
#     key_id="KEY_ID",
#     key_secret="KEY_SECRET"
# )
#
# available_regions = sinch_client.numbers.regions.list(
#     number_types=["MOBILE"]
# )
#
# print("Available regions:\n")
# for region in available_regions.iterator():
#     print(region)

# You extract the logic and place it inside the `execute` function like so:
#
# def execute(sinch_client):
#    available_regions = sinch_client.numbers.regions.list(
#        number_types=["MOBILE"]
#    )
#
#    print("Available regions:\n")
#    for region in available_regions.iterator():
#        print(region)
