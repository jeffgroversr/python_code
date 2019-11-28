# Download the helper library from https://www.twilio.com/docs/python/install

import twilio
import twilio.rest
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = "USEYOURTWILIOSINHERE"
auth_token = "USEYOURTWILIOTOKENHERE"
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body="Pulling louisville Right of Way Permits",
                              from_="+15023738207",
                              to="+12703128077"
                          )

print(message.sid)
