from discord.ext import commands
from src.utils.poster_generator import generate_poster

async def setup(bot):
    @bot.command()
    async def poster_preview(ctx):
        poster_path = generate_poster(title="Poster Preview", description="This is a preview.")
        await ctx.send(file=discord.File(poster_path))

    @bot.command()
    async def post_now(ctx, source: str):
        await ctx.send(f"Manual post triggered for {source}")

    @bot.command()
    async def toggle(ctx, channel: str):
        await ctx.send(f"Toggled updates for {channel}")

    @bot.command()
    async def recommend(ctx, anime: str):
        await ctx.send(f"Recommendations for {anime} coming soon!")

    @bot.command()
    async def next_episode(ctx, show: str):
        await ctx.send(f"Next episode info for {show} coming soon!")

    @bot.command()
    async def poll(ctx, *, question: str):
        await ctx.send(f"Poll: {question}")

    @bot.command()
    async def search(ctx, *, query: str):
        await ctx.send(f"Search results for {query} coming soon!")

    @bot.command()
    async def debug(ctx):
        await ctx.send("Debug info coming soon!")
