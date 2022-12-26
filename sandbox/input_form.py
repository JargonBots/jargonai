import os
import traceback

import discord
from discord import app_commands

# The guild in which this slash command will be registered.
# It is recommended to have a test guild to separate from your "production" bot
TEST_GUILD = discord.Object(os.getenv("DISCORD_GUILD_ID"))


class MyClient(discord.Client):
    def __init__(self) -> None:
        # Just default intents and a `discord.Client` instance
        # We don't need a `commands.Bot` instance because we are not
        # creating text-based commands.
        intents = discord.Intents.default()
        super().__init__(intents=intents)

        # We need an `discord.app_commands.CommandTree` instance
        # to register application commands (slash commands in this case)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")

    async def setup_hook(self) -> None:
        # Sync the application command with Discord.
        await self.tree.sync(guild=TEST_GUILD)


class TextGeneratorForm(discord.ui.Modal, title="Text Generator"):
    # Our modal classes MUST subclass `discord.ui.Modal`,

    # This is a longer, paragraph style input, where user can submit feedback
    # Unlike the name, it is not required. If filled out, however, it will
    # only accept a maximum of 300 characters, as denoted by the
    # `max_length=300` kwarg.
    feedback = discord.ui.TextInput(
        label="Description",
        style=discord.TextStyle.paragraph,
        placeholder="Write me a poem about ducks",
        required=True,
        max_length=300,
    )
    input_args = discord.ui.TextInput(
        label="Input Arguments",
        style=discord.TextStyle.paragraph,
        placeholder="ex: an array of integers length N and a target integer (none: leave blank)",
        required=False,
        max_length=300,
    )
    output_args = discord.ui.TextInput(
        label="Output Arguments",
        style=discord.TextStyle.paragraph,
        placeholder="ex. the position of the indices of two integers from the array (none: leave blank)",
        required=False,
        max_length=300,
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Thanks for your submission! {self.feedback.value}", ephemeral=True)

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message("Oops! Something went wrong.", ephemeral=True)

        # Make sure we know what the error actually is
        traceback.print_tb(error.__traceback__)


client = MyClient()


@client.tree.command(guild=TEST_GUILD, description="Generate some text based on input.")
async def feedback(interaction: discord.Interaction):
    # Send the modal with an instance of our `Feedback` class
    # Since modals require an interaction, they cannot be done as a response to a text command.
    # They can only be done as a response to either an application command or a button press.
    await interaction.response.send_modal(TextGeneratorForm())


BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
client.run(BOT_TOKEN)
