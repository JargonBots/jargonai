import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACe28e047e148974ee302aa476f2107d63'
auth_token = 'b27762321b6ba6d2f8b9fa9e8e669cdd'

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is Futura:',
         from_='+12076871838',
         to='+19736092074'
     )

print(message.sid)