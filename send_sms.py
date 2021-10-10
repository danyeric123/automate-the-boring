
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACc1e22f3d717d9aa1f37567b11dee5e15"
# Your Auth Token from twilio.com/console
auth_token  = "d215c41cb160e8675a7e388fa4afd747"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16466258268", 
    from_="+19175355452",
    body="""
    Hello from my Python script!
    Love David
    """)

print(message.sid)