import discord
from discord.ext import commands
from discord import app_commands
import logging
import os
from src.core.config import load_config
from src.utils.poster_generator import generate_poster

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
def on_ready():
    logging.info(f"Logged in as {bot.user}")
    try:
        import asyncio
        asyncio.create_task(bot.tree.sync())
        logging.info("Slash commands synced.")
    except Exception as e:
        logging.error(f"Failed to sync slash commands: {e}")

@bot.command()
async def help(ctx):
    await ctx.send("Use /poster preview, /post now [source], /toggle <channel>, /recommend <anime>, /next_episode <show>, /poll <question>, /search trailer, /debug")

@bot.command()
async def poster_preview(ctx):
    poster_path = generate_poster(title="Poster Preview", description="This is a preview.")
    await ctx.send(file=discord.File(poster_path))

# Register slash commands
@bot.tree.command(name="poster_preview", description="Show a preview of the next poster")
async def poster_preview_slash(interaction: discord.Interaction):
    poster_path = generate_poster(title="Poster Preview", description="This is a preview.")
    await interaction.response.send_message(file=discord.File(poster_path))

@bot.tree.command(name="post_now", description="Manual post trigger for a source")
@app_commands.describe(source="The source to post from (e.g. anilist, reddit)")
async def post_now_slash(interaction: discord.Interaction, source: str):
    await interaction.response.send_message(f"Manual post triggered for {source}")

@bot.tree.command(name="toggle", description="Enable or disable updates for a channel")
@app_commands.describe(channel="The channel to toggle")
async def toggle_slash(interaction: discord.Interaction, channel: str):
    await interaction.response.send_message(f"Toggled updates for {channel}")

@bot.tree.command(name="recommend", description="Suggest similar anime titles")
@app_commands.describe(anime="Anime to get recommendations for")
async def recommend_slash(interaction: discord.Interaction, anime: str):
    await interaction.response.send_message(f"Recommendations for {anime} coming soon!")

@bot.tree.command(name="next_episode", description="Show countdown and info for next episode")
@app_commands.describe(show="Show to get next episode info for")
async def next_episode_slash(interaction: discord.Interaction, show: str):
    await interaction.response.send_message(f"Next episode info for {show} coming soon!")

@bot.tree.command(name="poll", description="Create an anime poll")
@app_commands.describe(question="Poll question")
async def poll_slash(interaction: discord.Interaction, question: str):
    await interaction.response.send_message(f"Poll: {question}")

@bot.tree.command(name="search", description="Search for trailers, manga, etc.")
@app_commands.describe(query="Search query")
async def search_slash(interaction: discord.Interaction, query: str):
    await interaction.response.send_message(f"Search results for {query} coming soon!")

@bot.tree.command(name="debug", description="Developer: test a module")
async def debug_slash(interaction: discord.Interaction):
    await interaction.response.send_message("Debug info coming soon!")

@bot.tree.command(name="stats", description="Show analytics for a channel")
@app_commands.describe(channel="Channel to show stats for")
async def stats_slash(interaction: discord.Interaction, channel: str):
    # Placeholder for analytics
    await interaction.response.send_message(f"Stats for {channel} coming soon!")

async def post_to_channels(config):
    # Placeholder: implement per-channel posting logic
    pass

def run_discord_bot(config):
    token = os.getenv("DISCORD_TOKEN")
    bot.run(token)
