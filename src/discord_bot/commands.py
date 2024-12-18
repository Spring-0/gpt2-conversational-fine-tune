from discord.ext import commands
from model.gpt_2_bot import GPT2Agent
from discord_bot.views import FeedbackButtonView
import os
from dotenv import load_dotenv

load_dotenv()

MY_USER_ID = int(os.getenv("ADMIN_USER_ID"))
MODEL_PATH = "/home/spring/Desktop/workspace/llm-discord/gpt2-conversational-fine-tune/final-save"

gpt_bot = GPT2Agent(model_path=MODEL_PATH)

def setup_commands(bot):
    @bot.command(name="geb")
    async def prompt_gpt_2(ctx):
        try:
            prompt = ctx.message.content.split("!geb ")[1].strip()
        except IndexError:
            pass
        
        print(f"Prompt: {prompt}")
        bot_response = gpt_bot.generate_response(prompt)

        await ctx.send(
            bot_response,
            view=FeedbackButtonView(MY_USER_ID, prompt, bot_response)
        )
