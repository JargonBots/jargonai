# Property of JargonBots
# Written by Armaan Kapoor on 12-26-2022

from api_request_handler import openai_request


class Conversation:
    def __init__(self, starting_environment, bot_name):
        self.bot_name = bot_name
        self.environment = str(starting_environment)

    def get_environment(self):
        return str(self.environment)

    # def voice_append(self):
    #     print("You: ")
    #     voice_to_text = ListenSpeech()
    #     self.environment += "\nMe: " + str(voice_to_text)

    def user_append(self):
        print("\n")
        user_text = str(input("You: "))
        if "-n " in user_text:
            self.narrator_appends(user_text[2::])
        else:
            self.add_to_environment(user_text)
        return user_text

    def bot_append(self):
        injection = self.environment + "\n" + self.bot_name
        req = openai_request(injection)
        self.toks = req.return_tokens(0.5, 1000, 0.0, ["Me:", self.bot_name + ":"])
        print("\n")
        self.environment = injection + self.toks

    def narrator_appends(self, narrator_text):
        self.environment += (
            "\nNarrator (makes statements that change the environment): "
            + narrator_text
        )

    def add_to_environment(self, injection):
        self.environment += "\nMe: " + str(injection)

    def clear_environment(self):
        self.environment = ""

    def display_response(self):
        print(self.bot_name + self.toks)

    def store_environment(self, file_name):
        rate = input("\nRate the conversation on a scale of 1-10: ")
        with open(file_name, "w") as f:
            f.write(self.environment)
            f.write("\n\nRating: " + rate)

    def tick(self):

        user_text = self.user_append()

        while user_text != "exit":
            self.bot_append()
            self.display_response()
            user_text = self.user_append()

        print("\nExiting Chat With {}...".format(self.bot_name[:-2:]))
