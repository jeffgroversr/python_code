# Download the helper library from https://www.twilio.com/docs/python/install

import twilio
import twilio.rest
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = "AC2564d0891912e61db3dd7209d102a8a9"
auth_token = "821824b04684af0d4b28459e25103b1b"
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body="Posted louisville Right of Way Permits",
                              from_="+15023738207",
                              to="+12703128077"
                          )

print(message.sid)