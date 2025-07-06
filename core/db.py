import aiosqlite
import asyncio
import logging
from typing import Optional, List, Dict, Any

DB_PATH = "animebot.db"

CREATE_POSTED_TABLE = '''
CREATE TABLE IF NOT EXISTS posted (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT NOT NULL,
    item_id TEXT NOT NULL,
    channel_id TEXT NOT NULL,
    posted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
'''

CREATE_CHANNELS_TABLE = '''
CREATE TABLE IF NOT EXISTS channels (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT,
    enabled INTEGER DEFAULT 1
)
'''

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(CREATE_POSTED_TABLE)
        await db.execute(CREATE_CHANNELS_TABLE)
        await db.commit()
    logging.info("Database initialized with tables: posted, channels.")

def run_init_db():
    asyncio.run(init_db())

async def add_posted(source: str, item_id: str, channel_id: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO posted (source, item_id, channel_id) VALUES (?, ?, ?)",
            (source, item_id, channel_id)
        )
        await db.commit()

async def was_posted(source: str, item_id: str, channel_id: str) -> bool:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            "SELECT 1 FROM posted WHERE source=? AND item_id=? AND channel_id=?",
            (source, item_id, channel_id)
        ) as cursor:
            return await cursor.fetchone() is not None

async def get_recent_posts(limit: int = 20) -> List[Dict[str, Any]]:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            "SELECT * FROM posted ORDER BY posted_at DESC LIMIT ?", (limit,)
        ) as cursor:
            rows = await cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in rows]
