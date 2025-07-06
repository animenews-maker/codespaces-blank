import aiosqlite
import os
from typing import Optional

DB_PATH = os.path.join(os.path.dirname(__file__), '../../logs/xp.db')

XP_RANKS = [
    (0, "Anime Newbie"),
    (100, "Otaku Scout"),
    (500, "S-Class Weeb"),
    (1000, "Supreme Hokage")
]

async def add_xp(user_id: int, amount: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('CREATE TABLE IF NOT EXISTS xp (user_id INTEGER PRIMARY KEY, xp INTEGER DEFAULT 0)')
        await db.execute('INSERT OR IGNORE INTO xp (user_id, xp) VALUES (?, 0)', (user_id,))
        await db.execute('UPDATE xp SET xp = xp + ? WHERE user_id = ?', (amount, user_id))
        await db.commit()

async def get_xp(user_id: int) -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('CREATE TABLE IF NOT EXISTS xp (user_id INTEGER PRIMARY KEY, xp INTEGER DEFAULT 0)')
        async with db.execute('SELECT xp FROM xp WHERE user_id = ?', (user_id,)) as cursor:
            row = await cursor.fetchone()
            return row[0] if row else 0

async def get_rank(user_id: int) -> str:
    xp = await get_xp(user_id)
    for threshold, rank in reversed(XP_RANKS):
        if xp >= threshold:
            return rank
    return XP_RANKS[0][1]

async def get_leaderboard(limit: int = 10):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('CREATE TABLE IF NOT EXISTS xp (user_id INTEGER PRIMARY KEY, xp INTEGER DEFAULT 0)')
        async with db.execute('SELECT user_id, xp FROM xp ORDER BY xp DESC LIMIT ?', (limit,)) as cursor:
            return await cursor.fetchall()
