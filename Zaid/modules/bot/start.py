from Zaid import app, API_ID, API_HASH
from config import ALIVE_PIC
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 

PHONE_NUMBER_TEXT = (
    " ⍟ ʜᴇʏ..! ᴍᴀsᴛᴇʀ..!!👋!\n\n✪ I'm Your Assistant?\n\n‣ I can help you to host Your Left Clients.\n\n‣ 𝐉ᴏɪɴ: @i_m_fighter \n\n‣ This specially for Buzzy People's(lazy)\n\n‣ Now /clone {send your PyroGram String Session}"
)

@app.on_message(filters.command("start"))
async def hello(client: app, message):
    buttons = [
           [
                InlineKeyboardButton("🌐🇴𝐖𝐍𝐄𝐑⚡", url="t.me/ll4st_MIND_GAMERII"),
            ],
            [
                InlineKeyboardButton("‌💘🇸𝐔𝐏𝐏𝐎𝐑𝐓💗", url="t.me/I_M_FIGHTER"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

# © By Itz-Zaid Your motherfucker if uh Don't gives credits.
@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n /clone session")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("💓ᴘʟᴢ ᴡᴀɪᴛ...💌")
                   # change this Directry according to ur repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="Zaid/modules"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f" 💘ᴜʀ ʀᴇᴀᴅʏ ᴛᴏ ғᴜᴄᴋ Successfully As {user.first_name} 💨.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
