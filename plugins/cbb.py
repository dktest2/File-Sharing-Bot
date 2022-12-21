#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>╭━━━━━━━━━━━━━━━➣\n┣⪼ Creator : <a href='https://telegram.dog/R_KOHLI'>𝚁𝙰𝚅𝙸 𝙺𝙾𝙷𝙻𝙸</a>\n┣⪼ Language : Python3\n┣⪼ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n┣⪼ Source Code : <a href='https://github.com/Dkmovie/DK-Files-Store-Bot'>DK-File Store Bot</a>\n┣⪼ CHANNL : <a href='https://t.me/movie_a1'>𝙳𝙺_𝙼𝙾𝚅𝙸𝙴</a>\n┣⪼ GROUP : <a href='https://t.me/movie_on1'>𝙼𝙾𝚅𝙸𝙴 𝙶𝚁𝙾𝚄𝙿</a>\n╰━━━━━━━━━━━━━━━➣</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
