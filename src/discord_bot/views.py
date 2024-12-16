import discord
from discord.ui import Button, View
from logger import Logger

class FeedbackButtonView(View):
    def __init__(self, admin, prompt, response):
        super().__init__()
        self.admin = admin
        self.prompt = prompt
        self.response = response
        self.logger = Logger()

    async def disable_buttons(self, interaction):
        for button in self.children:
            button.disabled = True

        await interaction.message.edit(view=self)

    @discord.ui.button(label="👍 Good", style=discord.ButtonStyle.green, custom_id="good_button")
    async def good_button(self, interaction, button):
        if interaction.user.id != self.admin:
            await interaction.response.send_message("Unauthorized Action.", ephemeral=True)
            return

        await self.disable_buttons(interaction)
        await interaction.response.send_message(f"{interaction.user.mention} upvoted the response.")

        await self.log_interaction(True)

    @discord.ui.button(label="👎 Bad", style=discord.ButtonStyle.red, custom_id="bad_button")
    async def bad_button(self, interaction, button):
        if interaction.user.id != self.admin:
            await interaction.response.send_message("Unauthorized Action.", ephemeral=True)
            return

        await self.disable_buttons(interaction)
        await interaction.response.send_message(f"{interaction.user.mention} downvotes the response.")

        await self.log_interaction(False)

    async def log_interaction(self, isGood):
        self.logger.log_interaction(self.prompt, self.response, isGood)
