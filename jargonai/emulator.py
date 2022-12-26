from api_request_handler import openai_request


class emulator:
    def __init__(self, starting_environment):
        self.environment = str(starting_environment)

    def get_environment(self):
        return str(self.environment)

    def user_append(self):
        user_text = str(input("You: "))
        self.environment += "\nMe: " + str(user_text)

    def bot_append(self):
        injection = self.environment + "\n" + self.bot_name
        req = openai_request(injection)
        self.toks = req.return_tokens(1.1, 100, 0.0, ["Me:", self.bot_name])
        self.environment = injection + self.toks

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
            # self.bot_append()
