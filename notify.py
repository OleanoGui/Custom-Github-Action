import os
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

client = WebClient(token=os.environ["SLACK_API_TOKEN"])

def find_conversation(name):
    try:
        result = client.conversations_list()
        channels = result["channels"]
        channel = next((ch for ch in channels if ch["name"] == name), None)
        if channel:
            return channel["id"]
        else:
            logger.error(f"Channel '{name}' not found.")
            return None
    except SlackApiError as e:
        logger.error(f"Error fetching conversations: {e.response['error']}")
        return None

def publish_message(message):
    try:
        result = client.chat_postMessage(
            channel=message["channel"],
            text="New Pull Request!",
            blocks=message["blocks"]
        )
        logger.info(result)
    except SlackApiError as e:
        logger.error(f"Error publishing message: {e.response['error']}")

message_title_by_state = {
    "opened": "*🚀 New Pull Request!*",
    "closed": "*🚨 Pull Request Closed!*",
    "approved": "*👍 Pull Request Approved!*",
    "rejected": "*👎 Pull Request Rejected!*",
}

def notify_slack():
    pull_request_data = {
        "id": os.environ.get("PULL_REQUEST_ID"),
        "title": os.environ.get("PULL_REQUEST_TITLE"),
        "url": os.environ.get("PULL_REQUEST_URL"),
        "author": os.environ.get("PULL_REQUEST_AUTHOR"),
        "state": os.environ.get("PULL_REQUEST_STATE"),
    }

    logger.info(pull_request_data)
    if not all(pull_request_data.values()):
        logger.error("Missing pull request data. Exiting.")
        return
    channel_id = find_conversation("custom-github-action")
    if not channel_id:
        logger.error("Channel not found. Exiting.")
        return

    message = {
        "channel": channel_id,
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": message_title_by_state.get(pull_request_data["state"], "*Pull Request Update*")
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Id:*\n{pull_request_data['id']}\n*Title:*\n{pull_request_data['title']}\n*Author:*\n{pull_request_data['author']}\n*State:*\n{pull_request_data['state']}\n*URL:*\n<{pull_request_data['url']}>"
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://api.slack.com/img/blocks/bkb_template_images/approvalsNewDevice.png",
                    "alt_text": "computer thumbnail"
                }
            }
        ]
    }

    publish_message(message)

if __name__ == "__main__":
    notify_slack()