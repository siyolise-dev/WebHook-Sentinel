# WebHook-Sentinel

A lightweight Python service that intercepts incoming webhooks and logs them to a structured CSV file.

## Features
- **Async Handling:** Built with Flask for efficient request handling.
- **Data Logging:** Automatically timestamps and stores incoming JSON data.
- **Easy Integration:** Ready to deploy for notification logging.

## Usage
1. Install requirements: `pip install flask pandas`
2. Run the script: `python webhook_handler.py`
3. Send POST requests to `http://localhost:5000/webhook`.

## License
Distributed under the MIT License.

