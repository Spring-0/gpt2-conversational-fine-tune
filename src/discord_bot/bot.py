import discord
from discord.ext import commands
from discord_bot.views import FeedbackButtonView
from discord_bot.commands import setup_commands
import os
from dotenv import load_dotenv

def run_discord_bot():
    load_dotenv()

    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    bot = commands.Bot(command_prefix="!", intents=intents, description="Chat with gebet.")

    @bot.event
    async def on_ready():
        print(f"{bot.user} ({bot.user.id}) started.")

    setup_commands(bot)

    bot.run(os.getenv("BOT_TOKEN"))
