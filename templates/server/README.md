# Backend application built using Sinch Python SDK for Webhook Handling

This directory contains a server application built with [Sinch Python SDK](https://github.com/sinch/sinch-sdk-python)
to process incoming webhooks.

## Requirements

- [Python 3.9+](https://www.python.org/)
- [Flask]()
- [Sinch account](https://dashboard.sinch.com/)
- [ngrok](https://ngrok.com/docs)

## Configuration

1. **Environment Variables**:  
   Edit the [.env](.env) file, adding your credentials from the Sinch dashboard under the Access Keys section.
   - To use [Numbers](https://developers.sinch.com/docs/numbers/) you need to fill the following variables 
   with the values from your Sinch account:
   ``` 
     - SINCH_PROJECT_ID=Your Sinch Project ID
     - SINCH_KEY_ID=Your Sinch Access Key ID
     - SINCH_KEY_SECRET=Your Sinch Key Secret associated to your Sinch Access Key
   ```
   - Server Port
   Define the port your server will listen on (default: 3001):
   ```
     - SERVER_PORT=3001
   ```
    - Controller Settings
      - Numbers controller: Set the webhook secret, which you can retrieve from the [Numbers API](https://developers.sinch.com/docs/numbers/api-reference/numbers/tag/Numbers-Callbacks/), 
        using the `/callbackConfiguration` endpoint:
   ```
     - NUMBERS_WEBHOOK_SECRET=Your Sinch Webhook Secret
   ```


## Usage

### Running the server


1. Navigate to the project's root directory in your terminal.
 ```
   cd /path/to/sinch-sdk-python-quickstart
 ```
2. (Recommended) Create a virtual environment:
 ``` bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
 ```
3. Install the project dependencies:
 ``` bash
   pip install -e .
 ```
4. Update the `.env` file with your configuration (see above).
5. Start the server:
  - `python server.py`  
Or run it directly from your IDE.

### Endpoints

When the server is up and running, the declared controllers will listen and respond to the following endpoints:

| Service      | Endpoint           |
|--------------|--------------------|
| Numbers      | /NumbersEvent      |


## Using ngrok to expose your local server

To test your webhook locally, you can tunnel requests to your local server using ngrok.

*Note: The default port is `3001`, but this can be changed (see [Server port](#Server port) section)*

```bash
  ngrok http 3001
```

You'll see output similar to this:
```
ngrok                                                                           (Ctrl+C to quit)
...
Forwarding                    https://adbd-79-148-170-158.ngrok-free.app -> http://localhost:3001
```
Use the `https` forwaring URL in your callback configuration. For example:
 - Numbers: https://adbd-79-148-170-158.ngrok-free.app/NumbersEvent

Use this value to configure the callback URLs:
 - **Numbers**: Set the `callbackUrl` parameter when renting ou updating a number via the API
