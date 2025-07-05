import re
from pyrogram import Client, filters
from pyrogram.errors import MessageNotModified
from pyrogram.errors import *
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import *
import asyncio
from Script import text
from .db import tb
from .fsub import get_fsub

def parse_button_markup(text: str):
    lines = text.split("\n")
    buttons = []
    final_text_lines = []

    for line in lines:
        match = re.fullmatch(r"\[(.+?)\]\((https?://[^\s]+)\)", line.strip())
        if match:
            buttons.append([InlineKeyboardButton(match[1], url=match[2])])
        else:
            final_text_lines.append(line)

    return InlineKeyboardMarkup(buttons) if buttons else None, "\n".join(final_text_lines).strip()

@Client.on_message(filters.command("start"))
async def start_cmd(client, message):
    if await tb.get_user(message.from_user.id) is None:
        await tb.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(
            LOG_CHANNEL,
            text.LOG.format(message.from_user.mention, message.from_user.id)
        )

    # Check forced subscription
    if IS_FSUB and not await get_fsub(client, message):
        return

    await message.reply_text(
        text.START.format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⚡ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ⚡", url="http://t.me/UHD_Bots")],
            [
                InlineKeyboardButton("🤗 ʜᴇʟᴘ 🤗", callback_data="help"),
                InlineKeyboardButton("🤖 ᴀʙᴏᴜᴛ 🤖", callback_data="about")
            ],
            [InlineKeyboardButton("⚡ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ⚡", callback_data="generate")]
        ]),
        disable_web_page_preview=True
    )
    
