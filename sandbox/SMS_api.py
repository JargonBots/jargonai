# Property of JargonBots.
# Written by Armaan Kapoor on 12-22-2022.

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
