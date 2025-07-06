import discord
from discord import app_commands
from discord.ext import commands
from src.core.config_manager import check_config, backup_config, diff_config, restore_config
from src.core.xp_manager import add_xp, get_xp, get_rank, get_leaderboard

# This file should be imported and setup with the bot instance in bot.py

def setup_commands(bot: commands.Bot):
    @bot.tree.command(name="config_check", description="List missing or broken config keys")
    async def config_check_slash(interaction: discord.Interaction):
        result = check_config()
        if result['missing']:
            await interaction.response.send_message(f"Missing keys: {', '.join(result['missing'])}")
        else:
            await interaction.response.send_message("Config is valid.")

    @bot.tree.command(name="config_backup", description="Backup config to file")
    async def config_backup_slash(interaction: discord.Interaction):
        path = backup_config()
        await interaction.response.send_message(f"Config backed up to {path}")

    @bot.tree.command(name="config_diff", description="Show config changes since last backup")
    async def config_diff_slash(interaction: discord.Interaction):
        diff = diff_config()
        await interaction.response.send_message(f"Diff:\n```diff\n{diff}\n```" if diff else "No diff found.")

    @bot.tree.command(name="config_restore", description="Restore config from backup")
    @app_commands.describe(date="Date in YYYY-MM-DD format")
    async def config_restore_slash(interaction: discord.Interaction, date: str):
        result = restore_config(date)
        await interaction.response.send_message(result)

    @bot.tree.command(name="rank", description="Show your XP rank and progress")
    async def rank_slash(interaction: discord.Interaction):
        user_id = interaction.user.id
        xp = await get_xp(user_id)
        rank = await get_rank(user_id)
        await interaction.response.send_message(f"Your rank: {rank}\nXP: {xp}")

    @bot.tree.command(name="leaderboard", description="Show top 10 XP users")
    async def leaderboard_slash(interaction: discord.Interaction):
        lb = await get_leaderboard()
        msg = "Top 10 XP Users:\n"
        for i, (user_id, xp) in enumerate(lb, 1):
            msg += f"{i}. <@{user_id}> — {xp} XP\n"
        await interaction.response.send_message(msg)