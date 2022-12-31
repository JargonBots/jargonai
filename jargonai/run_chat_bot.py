# Property of JargonBots
# Written by Armaan Kapoor on 12-26-2022

from conversation import Conversation

# Chat useage examwannple:


Name = "Oprah"

cv = Conversation(
    starting_environment="The following is a conversation with {}.\n".format(Name),
    bot_name="{}: ".format(Name),
)

print("The following is a chat with {}".format(Name))
cv.tick()

# cv.user_append()
cv.store_environment("chat_history_log1.txt")
