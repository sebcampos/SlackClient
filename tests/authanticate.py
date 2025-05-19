from src.slackclient.client import SlackClient
# https://api.slack.com/quickstart

def test_authenticate():
    client = SlackClient()
    client.