from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.veez import user
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""𖤐 **اهـــلا {message.from_user.mention()} 𖤐**\n
𖤐 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **هذا بوت تشغيل الموسيقى والفيديو في مجموعات من خلال محادثات الفيديو الجديدة في التلجيرام!**

𖤐 **اكتشف جميع أوامر الروبوت وكيفية عملها من خلال النقر على زر الأوامر𖤐!**

𖤐 **لمعرفة كيفية استخدام هذا الروبوت ، الرجاء النقر فوق الزر »❓ الدليل الأساسي!**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ضـــيــف البـــوت لمـــمجوعــتك ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton(" 𖤐دلــيـل الاســاســي𖤐", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("𖤐الاومر𖤐", callback_data="cbcmds"),
                    InlineKeyboardButton("𖤐الـــمــطــور𖤐", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "𖤐جــروب التــــواصل𖤐", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "𖤐قنـــاه التـــحـديثات𖤐", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "𝙀𝙇 𝙂8𝘼𝙕𝘼𝙇 🦌⁽♔₎┋𝐆8★", url="https://t.me/U_Y_H"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("𖤐جــــروب الــــتواصــل𖤐", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "𖤐قــنــاه التحـديــثات𖤐", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**نـــورت {message.from_user.mention()}, انـــا {BOT_NAME}**\n\n𖤐 يـــعـــمــل الــبـــوت بــشـــكـــل طـــبــيــعــي\nاســـتــاذ: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n𖤐 نسخه البوت: `v{__version__}`\n𖤐 نــســخــه بــوتـــجــرم: `{pyrover}`\n𖤐نسسخه بايثون: `{__python_version__}`\n🍀 بــوت ممتاذ: `{pytover.__version__}`\n✨ حالهة البوت: `{uptime}`\n\n**شكرًا لإضافتي هنا ، لتشغيل الفيديو والموسيقى على دردشة الفيديو الخاصة بمجموعتك** ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("𖤐 `قـــيــد آلتـــشـغيل`\n" f"𖤐 `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 حــآلــه آلـــبــؤت:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                "𖤐 **شكرا لإضافتي إلى المجموعة !𖤐**\n\n"
          "انـنا بــوت لتــشــغـيل الموسيقي والفديوهات في المحادثه الصواتية لانضمام الحساب المساعد قم بكتابه /userbotjoin وسسوف ينضم تلقائي قناه السورس @U_Y_H.\n\n"
                "**Once done, type** /reload",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("𖤐قـــنــاه الــبـوت𖤐", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            InlineKeyboardButton("𖤐جــروب الــدععم𖤐", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton("𖤐الــحــســاب الـــمـــســاعــد𖤐", url=f"https://t.me/{ass_uname}")
                        ]
                    ]
                )
            )
