
from twilio.rest import Client
import dotenv
import os

dotenv.load_dotenv()

# Your Account SID from twilio.com/console
account_sid = os.environ.get('ACCOUNT_SID')
# Your Auth Token from twilio.com/console
auth_token  = os.environ.get('AUTH_TOKEN')

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16466258268", 
    from_="+19175355452",
    body="""
    Hello from my Python script!
    Love David
    """)

print(message.sid)