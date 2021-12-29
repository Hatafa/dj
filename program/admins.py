from cache.admins import admins
from driver.veez import call_py
from pyrogram import Client, filters
from driver.decorators import authorized_users_only
from driver.filters import command, other_filters
from driver.queues import QUEUE, clear_queue
from driver.utils import skip_current_song, skip_item
from config import BOT_USERNAME, GROUP_SUPPORT, IMG_3, UPDATES_CHANNEL
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


bttn = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 رجوع", callback_data="cbmenu")]]
)


bcl = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🗑 الغاء", callback_data="cls")]]
)


@Client.on_message(command(["reload", "تحديث", f"reload@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(
        "𖤐 بـــوت **تــم اعــادة تــشــغــلــيــها بـــنــجــاح 𖤐!**\n𖤐 **تـــم تحـــديــث** قـــائمة **الادمن !**"
    )


@Client.on_message(command(["skip", "كمل" f"skip@{BOT_USERNAME}", "vskip"]) & other_filters)
@authorized_users_only
async def skip(client, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="• لتحكم في الموسقي", callback_data="cbmenu"
                ),
                InlineKeyboardButton(
                    text="• الغاء", callback_data="cls"
                ),
            ]
        ]
    )

    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("𖤐لا يـــوجد شــيئ لـــتــشــغــيل𖤐")
        elif op == 1:
            await m.reply("𖤐 __تــم__ **تــخــطــي.**\n\n**الاغـــنــيــة بـــنــجــاح𖤐**")
        elif op == 2:
            await m.reply("🗑️ **مسح قائمه الانتظار**\n\n**• userbot leaving voice chat**")
        else:
            await m.reply_photo(
                photo=f"{IMG_3}",
                caption=f"⏭ **تــم تخطي الموسقي.**\n\n🏷 **الاسم:** [{op[0]}]({op[1]})\n💭 **المجموعه:** `{chat_id}`\n💡 **الحاله:** `يعمل`\n🎧 **مطلوبه من:** {m.from_user.mention()}",
                reply_markup=keyboard,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "🗑 **تمت إزالة الأغنية من قائمة الانتظار:**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(
    command(["stop", f"stop@{BOT_USERNAME}", "end", "اسكت", f"end@{BOT_USERNAME}", "vstop", "اسكت",])
    & other_filters
)
@authorized_users_only
async def stop(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("𖤐 **تــم ايــقــاف الــبــوت.𖤐**")
        except Exception as e:
            await m.reply(f"🚫 **خطا:**\n\n`{e}`")
    else:
        await m.reply(" **هسكت ازاي ومفيش حاجة شغالة اصل😏ا**")


@Client.on_message(
    command(["pause", f"pause@{BOT_USERNAME}", "vpause"]) & other_filters
)
@authorized_users_only
async def pause(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                "⏸ **تم ايقاف الموسقي موقتا.**\n\n• **To resume the stream, use the**\n» /resume command."
            )
        except Exception as e:
            await m.reply(f"🚫 **خطا:**\n\n`{e}`")
    else:
        await m.reply("❌ **ليس في شئ شغال**")


@Client.on_message(
    command(["resume", f"resume@{BOT_USERNAME}", "vresume"]) & other_filters
)
@authorized_users_only
async def resume(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                "▶️ **بدا التشغيل.**\n\n• **To pause the stream, use the**\n» /pause command."
            )
        except Exception as e:
            await m.reply(f"🚫 **خطا:**\n\n`{e}`")
    else:
        await m.reply("❌ **لم يوجد شيئ للتشغيل**")


@Client.on_message(
    command(["mute", f"mute@{BOT_USERNAME}", "vmute"]) & other_filters
)
@authorized_users_only
async def mute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await m.reply(
                "🔇 **تم كتم البوت.**\n\n• **To unmute the userbot, use the**\n» /unmute command."
            )
        except Exception as e:
            await m.reply(f"🚫 **خطا:**\n\n`{e}`")
    else:
        await m.reply("❌ **لا يوجد شىئ مشغل**")


@Client.on_message(
    command(["unmute", f"unmute@{BOT_USERNAME}", "vunmute"]) & other_filters
)
@authorized_users_only
async def unmute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await m.reply(
                "🔊 **تم فك كتم البوت.**\n\n• **To mute the userbot, use the**\n» /mute command."
            )
        except Exception as e:
            await m.reply(f"🚫 **خطا:**\n\n`{e}`")
    else:
        await m.reply("❌ **لا يوجد شيئ مشغل**")


@Client.on_callback_query(filters.regex("cbpause"))
async def cbpause(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answe("المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await query.edit_message_text(
                "⏸ تم ايقاف البوت موقتا", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **خطا:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("بسسلعب يحبيبي بق🙂", show_alert=True)


@Client.on_callback_query(filters.regex("cbresume"))
async def cbresume(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("𖤐المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر𖤐 !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await query.edit_message_text(
                "▶️ تم استئناف البوت", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **خطا:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("ازاي ومفيش حاجهة شغالهة اقنعني😡", show_alert=True)


@Client.on_callback_query(filters.regex("cbstop"))
async def cbstop(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("𖤐المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر𖤐 !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await query.edit_message_text(" **𖤐تم ايقاف التشغيل𖤐**", reply_markup=bcl)
        except Exception as e:
            await query.edit_message_text(f"🚫 **خطا:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("مفيش حاجهةة متزفته شغتله🙂", show_alert=True)


@Client.on_callback_query(filters.regex("cbmute"))
async def cbmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await query.edit_message_text(
                "🔇 تم كتم البوت بنجاح", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **خطا:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("مفيش حاجهة شغالهةة يبرو☹️", show_alert=True)


@Client.on_callback_query(filters.regex("cbunmute"))
async def cbunmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await query.edit_message_text(
                "🔊تم الغاء كتم بنجاح", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **خطا:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("مفيش حاجهةة شغالهةة😏", show_alert=True)


@Client.on_message(
    command(["volume", f"volume@{BOT_USERNAME}", "vol"]) & other_filters
)
@authorized_users_only
async def change_volume(client, m: Message):
    range = m.command[1]
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.change_volume_call(chat_id, volume=int(range))
            await m.reply(
                f"✅ **ظبط الصوت علي** `{range}`%"
            )
        except Exception as e:
            await m.reply(f"🚫 **خطا:**\n\n`{e}`")
    else:
        await m.reply(" **مفيش حاجهةة شغالهةة يستا☹️**")
