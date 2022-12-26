# Property of JargonBots
# Written by Armaan Kapoor on 12-26-2022

from api_request_handler import openai_request


class conversation:
    def __init__(self, starting_environment, bot_name):
        self.bot_name = bot_name
        self.environment = str(starting_environment)

    def get_environment(self):
        return str(self.environment)

    def user_append(self):
        print("\n")
        user_text = str(input("You: "))
        if "-n " in user_text:
            self.narrator_appends(user_text[2::])
        if "-a " in user_text:
            # FIXME: Not sure what goes here
            pass
        else:
            self.environment += "\nMe: " + str(user_text)

    def bot_append(self):
        injection = self.environment + "\n" + self.bot_name
        req = openai_request(injection)
        self.toks = req.return_tokens(1.0, 200, 0.0, ["Me:", self.bot_name])
        print("\n")
        self.environment = injection + self.toks

    # def third_party_append(self, third_party_name, third_party_text):
    #     self.environment += "\n" + third_party_name + ": " + third_party_text

    def narrator_appends(self, narrator_text):
        self.environment += "\nNarrator (makes statements that change the environment): " + narrator_text

    def add_context(self, narrator_text):
        self.environment += "\nNarrator (makes statements that change the environment): " + narrator_text

    def add_to_environment(self, injection):
        self.environment += str(injection)

    def clear_environment(self):
        self.environment = ""

    def display(self):
        print(self.environment)

    def tick(self, ticks):

        for tick in range(ticks):
            self.user_append()
            self.bot_append()
            print(self.bot_name + self.toks)
            # say it out loud mac os
            # system('say -v Fred ' + str(self.toks))
            # self.bot_append()
