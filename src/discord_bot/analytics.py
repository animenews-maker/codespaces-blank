from src.utils.analytics import get_post_stats
from discord.ext import commands

async def setup(bot):
    @bot.command()
    async def stats(ctx, channel: str):
        stats = await get_post_stats(channel)
        await ctx.send(f"Posts: {stats['count']}, Latest: {stats['latest']}")
