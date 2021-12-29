# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""𖤐 **اهـــلا [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
𖤐 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) هذا بوت تشغيل الموسيقى والفيديو في مجموعات من خلال محادثات الفيديو الجديدة في التلجيرام!**

𖤐 **هذا بوت تشغيل الموسيقى والفيديو في مجموعات من خلال محادثات الفيديو الجديدة في التلجيرام!**

𖤐 **لمعرفة كيفية استخدام هذا الروبوت ، الرجاء النقر فوق الزر  الدليل الأساسي!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ضـــيـــف الـــبوت لـــجــروبك ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton(" 𖤐الاوامـــر الاساسيه 𖤐", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("𖤐الاومـر𖤐", callback_data="cbcmds"),
                    InlineKeyboardButton("𖤐الـــمـــطـــور𖤐", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "𖤐جــــروب الـــدعــم𖤐", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "𖤐قـــنـــاة الـــتــحــديـــثــات𖤐", url=f"https://t.me/{UPDATES_CHANNEL}"
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


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""𖤐 **الدليل الأساسي لاستخدام هذا الروبوت𖤐:**

1.) **أولا ، أضفني إلى مجموعتك.**
2.) **بعد ذلك ، قم بترقيتي كمسؤول ومنح جميع الأذونات باستثناء المسؤول المجهول.**
3.) **بعد ترقيتي ، اكتب /reload في مجموعة لتحديث بيانات المسؤول.**
3.) **قم اضافه @{ASSISTANT_NAME} لمجموعتك أو اكتب /userbotjoin لدعوت المساعد.**
4.) **قم بتشغيل محادثة الفيديو أولاً قبل البدء في تشغيل الفيديو / الموسيقى.**
5.) **في بعض الأحيان ، يتم إعادة تحميل الروبوت باستخدام /reload يمكن أن يساعدك الأمر في حل بعض المشكلات.**

𖤐 **𖤐 ** إذا لم ينضم المستخدم الروبوت إلى محادثة الفيديو ، فتأكد من تشغيل دردشة الفيديو بالفعل أو اكتبها /userbotleave ثم اكتب /userbotjoin تكرار.**
𖤐 **إذا كانت لديك أسئلة متابعة حول هذا الروبوت ، فيمكنك إخباره من خلال دردشة الدعم الخاصة بي هنا: @{GROUP_SUPPORT}**

𖤐 __مشغل بواسطة {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("𖤐رجـوع𖤐", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""𖤐 **اهــلا [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **نـــورت اخـي قـــائمــه الاومـــر تـــابع فـي الاسفل !**

⚡ __مـــدعـــوم مــن {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𖤐القائمه الاولي من الاوامر𖤐", callback_data="cbadmin"),
                    InlineKeyboardButton("𖤐القائمه التانيه من الاومر𖤐", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("𖤐القائمه التاله من الاوامر𖤐", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("𖤐رجوع𖤐", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""𖤐 هـــنــا قـــائمــه الاومـــر الـــاســـاسيــه𖤐:

𖤐 /mplay (لنك او اسم) تشغيل الموسيقى على دردشة المكلمات𖤐
طرق أخري للتشغيل (.شغل ؛ .غزال) جنبهم اسم الاغنيه أو الرابط
𖤐 /stream قم بعمل اعاده توجيه علي الموسيقي واكتب هذه الامر𖤐
𖤐 /vplay  (لتشغيل فديو في المحادثه الصوتيه (اسم𖤐
𖤐 /vstream قم بي اعادة توجيه علي فديو لتقوم بتشغيلو𖤐
𖤐 /playlist تظهر لك قائمة التشغيل𖤐
𖤐 /video (اسم) تحميل الفديو من اليوتيوب𖤐
𖤐 /song (اسم) تحميل اغنية من اليوتيوب𖤐
𖤐 /lyric (اسم) قص الأغنية الغنائية𖤐
𖤐 /search (لنك) البحث عن فديو عن طريق لنك𖤐

𖤐 /ping معرفه سرعه البوت𖤐
𖤐 /uptime عرض مده تشغيل البوت𖤐
𖤐 /alive معرفه اذكان البوت يعمل𖤐

⚡️ __مــدعـــوم مــن {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("𖤐رجـــوع𖤐", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""𖤐 هـــنــا قـــائمــه الاومـــر الـــاســـاسيــه𖤐:

𖤐 /pause ايقاف التشغيل موقتا𖤐
𖤐 /resume استكمال تشغيل الموسقي𖤐
𖤐 /skip تخطي الاغنيه الشغاله𖤐
𖤐 /stop لايقاف الاغنيه𖤐
𖤐 /vmute لكتم البوت في المحادثه الصواتيه𖤐
𖤐 /vunmute لفك كتم لبوت في المحادثه الصواتيه𖤐
𖤐 /volume `1-200` لتحكم في صوت البوت (لازم البوت المساعد يكون مشرف)𖤐
𖤐 /reload تحديث البوت وتحديث قائمه الادمنيه𖤐
𖤐 /userbotjoin لدعوه الحساب المساعد𖤐
𖤐 /userbotleave لخروج الحساب المساعد من الجروب𖤐

𖤐 __مدعوم من {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("𖤐رجـــوع𖤐", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""𖤐 هـــنــا قـــائمــه الاومـــر الـــاســـاسيــه𖤐:

𖤐 /rmw لحذف جميع الملفات𖤐
𖤐 /rmd لحذف جميع الملفات المحمله𖤐
𖤐 /sysinfo لمعرفهةة معلومات السرفير𖤐
𖤐 /update لتحديث بوت لاخر اصدار𖤐
𖤐 /restart لتحديث البوت𖤐
𖤐 /leaveall لخروج البوت من جميع الجروبات𖤐

⚡ __مدعوم من {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("𖤐رجـــوع𖤐", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("𖤐انتا مسؤال مجهول !\n\n» العودة إلى حساب المستخدم من حقوق المسؤول.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **الاعدادت** {query.message.chat.title}\n\n⏸ : ايقاف الموسيقي\n▶️ : اعاده تشغيل الموسيقي\n🔇 : لكتم البوت\n🔊 : فك كتم البوت\n⏹ : اياف الاغنيه",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 الغاء", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("𖤐لم يوجد شيئ مشغل𖤐", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    await query.message.delete()
