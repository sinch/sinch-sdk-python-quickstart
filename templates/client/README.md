# Client Application Using the Sinch Python SDK

This directory provides a Python client application built with the
[Sinch Python SDK](https://github.com/sinch/sinch-sdk-python).  
It allows you to integrate Sinch APIs into  your Python applications easily.

## Prerequisites

Before you being, ensure you have:
 - [Python](https://www.python.org/) installed (versions 3.9 to 3.12 recommended).
 - A [Sinch account](https://dashboard.sinch.com/) with access to the APIs you want to use.

## Configuration

To configure the client application:

1. **Environment Variables**:  
   Edit the [config.ini](config.ini) file, adding your credentials from the Sinch dashboard under the Access Keys section.
   - To use [Numbers](https://developers.sinch.com/docs/numbers/) you need to fill the following variables with the values from your Sinch account:
     ``` 
       [CREDENTIALS]
       - SINCH_PROJECT_ID=Your Sinch Project ID
       - SINCH_KEY_ID=Your Sinch Access Key ID
       - SINCH_KEY_SECRET=Your Sinch Key Secret associated to your Sinch Access Key
     ```

2. **API Integration**:  
   The application demonstrates usage via modular snippets in `client/src/numbers_api/snippet.py`, which acts as the 
   main integration point for testing Sinch Numbers API endpoints. Replace the existing logic with your own, based on
   the desired API functionality.

   You can explore and adapt examples from [Python SDK snippets repository.](https://github.com/sinch/sinch-sdk-python-snippets) directly into the `execute(sinch_client)` function:
    - Choose a snippet
    - Copy only the functional logic, skipping the `SinchClient` initialization as 
      this is already set up in the project.
    - Paste it into the `execute(sinch_client)` function in `snippet.py`.


## Usage

1. Navigate to the project's root directory in your terminal.
 ```
   cd /path/to/sinch-sdk-python-quickstart
 ```
2. (Recommended) Create a virtual environment:
 ``` bash
   python -m venv venv
   source venv/bin/activate 
   # On Windows use `venv\Scripts\activate`
 ```
3. Install the project dependencies:
 ```
   pip install -e .
 ```
4. Ensure your `config.ini` file have been updated as described above.
5. Run the application:
  - `python app.py`  
  Or run it directly from your IDE.
