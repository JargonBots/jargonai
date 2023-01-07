# Property of JargonBots.
# Written by Armaan Kapoor on 12-22-2022

import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='',
         from_='',
         to=''
     )

print(message.sid)
