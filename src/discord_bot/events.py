from discord.ext import commands
import logging

async def setup(bot):
    @bot.event
    async def on_message(message):
        if message.author.bot:
            return
        await bot.process_commands(message)

    @bot.event
    async def on_command_error(ctx, error):
        logging.error(f"Command error: {error}")
        await ctx.send(f"Error: {error}")
