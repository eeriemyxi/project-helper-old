from discord_webhook import DiscordWebhook
import requests
import urllib3
from extras.color_format import Colors as col
def command():
    print('Thanks for your time! Please enter the suggestion below. You should include an email if you\'re comfortable with it.')
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/874346590234615848/xBYVKyNxziJzrsnhzY1zW5OCgQR_0vmNEhQ8SKsuHDKZSbW3vwZVILw2NgcJoEyq_J3D', content=input('Suggestion: ')+'\n<@858247195009482772>')
    col.cprint('cyan','Sending...')
    try:
        webhook.execute()
        col.cprint('green','Sent.')
        print('Thanks, I\'ll check it out when I get time.')
        return
    except (requests.exceptions.ConnectionError, urllib3.exceptions.NewConnectionError, urllib3.exceptions.MaxRetryError):
        col.p_error('No internet connection.')