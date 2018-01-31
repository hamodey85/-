from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACe02dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token = "22c6abXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+61XXXXXXXXX",
    from_="+614XXXXXXXX",
    body="Hello from Python!")

print(message.sid)
