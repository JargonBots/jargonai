# Property of JargonBots.
# Written by Erik (Dan) Karlsson on 12-25-2022.

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values['Body']

    # use the incoming message to generate the response here

    r = MessagingResponse()
    r.message('this is the response')
    return str(r)
