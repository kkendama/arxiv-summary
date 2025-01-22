import requests
import os

class DiscordPoster:
    def __init__(self):
        self.webhook_url = os.getenv('DISCORD_WEBHOOK_URL')
    
    def post(self, content):
        payload = {
            'content': content
        }
        requests.post(self.webhook_url, json=payload) 