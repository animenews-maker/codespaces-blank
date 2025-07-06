import discord
import os
import logging
from discord.ext import commands
from dotenv import load_dotenv
from typing import Any, Dict

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix=os.getenv("BOT_PREFIX", "!"), intents=discord.Intents.all())

# Example: Supported sources for !post_now and other commands
SUPPORTED_SOURCES = [
    "ANN", "Crunchyroll-News", "MyAnimeList-News", "LiveChart-News", "ComicNatalie", "Reddit-Anime",
    "AniList-Airings", "LiveChart-Airings", "LiveChart-Upcoming", "MyAnimeList-Ratings", "ANN-Anime",
    "AniList-Upcoming", "MangaDex-News", "ComicNatalie-Upcoming", "YouTube-Trailers", "AniTrendz-Trailers",
    "MangaDex-API", "LiveChart-Schedule", "MyAnimeList-Manga", "AniList-Ratings", "MAL-Trending",
    "AnimeChan-Quote", "Reddit-Manga", "YouTube-Reviews", "Twitter-Anime", "Instagram-Anime",
    "Threads-Anime", "Telegram-Anime", "AniTrendz-News", "AnimeNewsPlus", "AnimeCorner-News",
    "AnimeHype", "AnimeUKNews", "OtakuUSA", "AnimePlanet-News", "AnimeTrending", "Anime-YouTube-Shorts",
    "MangaUpdates", "Anime-Discord-News", "Anime-Subreddit-News", "Anime-Official-Twitter", "Anime-Official-Instagram",
    "AnimeJapan-News", "AnimeTV", "Anime-YouTube-Reviews", "Anime-YouTube-Interviews", "Anime-YouTube-Events",
    "MangaPlus-News", "MangaPlus-Chapters", "MangaTimeKirara", "Anime-Official-Facebook", "Anime-Official-Threads"
]

SOURCE_DESCRIPTIONS = {
    "ANN": "Anime News Network - Official anime news and articles.",
    "Crunchyroll-News": "Crunchyroll's official news feed.",
    "MyAnimeList-News": "MAL's anime and manga news.",
    "LiveChart-News": "LiveChart's anime news and updates.",
    "ComicNatalie": "Japanese comic and manga news.",
    "Reddit-Anime": "Top posts from r/anime.",
    "AniList-Airings": "AniList's airing anime info.",
    "LiveChart-Airings": "LiveChart's airing schedule.",
    "LiveChart-Upcoming": "Upcoming anime from LiveChart.",
    "MyAnimeList-Ratings": "Latest ratings from MAL.",
    "ANN-Anime": "Anime-specific news from ANN.",
    "AniList-Upcoming": "Upcoming anime from AniList.",
    "MangaDex-News": "MangaDex manga news.",
    "ComicNatalie-Upcoming": "Upcoming manga from ComicNatalie.",
    "YouTube-Trailers": "Latest anime trailers on YouTube.",
    "AniTrendz-Trailers": "Anime trailers from AniTrendz.",
    "MangaDex-API": "MangaDex API for chapters.",
    "LiveChart-Schedule": "Weekly anime release schedule.",
    "MyAnimeList-Manga": "MAL manga news.",
    "AniList-Ratings": "AniList ratings updates.",
    "MAL-Trending": "Trending anime on MAL.",
    "AnimeChan-Quote": "Random anime quotes.",
    "Reddit-Manga": "Top posts from r/manga.",
    "YouTube-Reviews": "Anime reviews on YouTube.",
    "Twitter-Anime": "Anime Twitter news.",
    "Instagram-Anime": "Anime Instagram posts.",
    "Threads-Anime": "Anime Threads posts.",
    "Telegram-Anime": "Anime Telegram channels.",
    "AniTrendz-News": "Anime news from AniTrendz.",
    "AnimeNewsPlus": "Anime News Plus feed.",
    "AnimeCorner-News": "Anime Corner news.",
    "AnimeHype": "Anime Hype news.",
    "AnimeUKNews": "UK anime news.",
    "OtakuUSA": "Otaku USA magazine news.",
    "AnimePlanet-News": "Anime Planet news.",
    "AnimeTrending": "Anime Trending news.",
    "Anime-YouTube-Shorts": "Anime YouTube Shorts.",
    "MangaUpdates": "MangaUpdates manga news.",
    "Anime-Discord-News": "Anime Discord server news.",
    "Anime-Subreddit-News": "News from anime subreddits.",
    "Anime-Official-Twitter": "Official anime Twitter accounts.",
    "Anime-Official-Instagram": "Official anime Instagram accounts.",
    "AnimeJapan-News": "AnimeJapan event news.",
    "AnimeTV": "Anime TV news and updates.",
    "Anime-YouTube-Reviews": "Anime review videos on YouTube.",
    "Anime-YouTube-Interviews": "Anime interviews on YouTube.",
    "Anime-YouTube-Events": "Anime event streams on YouTube.",
    "MangaPlus-News": "MangaPlus manga news.",
    "MangaPlus-Chapters": "MangaPlus chapter releases.",
    "MangaTimeKirara": "Manga Time Kirara magazine news.",
    "Anime-Official-Facebook": "Official anime Facebook pages.",
    "Anime-Official-Threads": "Official anime Threads accounts."
}

@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user} (ID: {bot.user.id})")
    activity = discord.Game(name="Anime News | !help")
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.event
async def on_command_error(ctx, error):
    if hasattr(ctx, 'send'):
        await ctx.send(f"❌ Error: {str(error)}")
    logging.error(f"Command error: {error}")

@bot.command()
async def sources(ctx):
    """List all supported sources."""
    await ctx.send("**Supported sources:**\n" + ", ".join(SUPPORTED_SOURCES))

@bot.command()
async def sourceinfo(ctx, *, source: str):
    """Get info about a specific source."""
    if source in SOURCE_DESCRIPTIONS:
        await ctx.send(f"✅ **{source}**: {SOURCE_DESCRIPTIONS[source]}")
    elif source in SUPPORTED_SOURCES:
        await ctx.send(f"✅ **{source}** is supported, but no description available.")
    else:
        await ctx.send(f"❌ Source '{source}' is not recognized.")

# Add all new sources to the config.json channels as well for full integration
# This is a placeholder for how you would add them in your config.json:
# "sources": SUPPORTED_SOURCES
#
# If you want to enable all sources for a specific channel, you can do so in config.json like:
# "sources": ["ANN", "Crunchyroll-News", ..., "Anime-Official-Threads"]
#
# For dynamic use, you can also reference SUPPORTED_SOURCES in your command logic, e.g.:
#
# @bot.command()
# async def post_now(ctx, source: str):
#     if source not in SUPPORTED_SOURCES:
#         await ctx.send(f"❌ Source '{source}' is not supported.")
#         return
#     # ...fetch and post logic...
#
# This ensures all new sources are available for commands and config-driven posting.

def start_discord_bot(config: Dict[str, Any]):
    bot.run(TOKEN)
