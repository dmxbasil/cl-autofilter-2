class script(object):
    START_TXT = """𝑯𝒆𝒍𝒍𝒐 {},
𝑴𝒚 𝒏𝒂𝒎𝒆 𝒊𝒔 <a href=https://t.me/{}>{}</a> 𝑰 𝒄𝒂𝒏 𝒑𝒓𝒐𝒗𝒊𝒅𝒆 𝒎𝒐𝒗𝒊𝒆𝒔 𝒊𝒏 𝒈𝒓𝒐𝒖𝒑, 𝑱𝒖𝒔𝒕 𝒂𝒅𝒅 𝒎𝒆 𝒕𝒐 𝒖𝒓 𝒈𝒓𝒐𝒖𝒑 𝒂𝒔 𝒂𝒅𝒎𝒊𝒏😍"""
    HELP_TXT = """𝑯𝒆𝒚 {}
𝑯𝒆𝒓𝒆 𝒊𝒔 𝒎𝒚 𝒉𝒆𝒍𝒑 𝒄𝒐𝒎𝒎𝒂𝒏𝒅𝒔."""
    ABOUT_TXT = """✯ ᴍʏ ɴᴀᴍᴇ » {}
✯ ᴄʀᴇᴀᴛᴏʀ » <a href=https://t.me/bibin_indian_rock>ʙɪʙɪɴ</a>
✯ ʟɪʙʀᴀʀʏ » <a href=https://docs.pyrogram.org/>ᴘʏʀᴏɢʀᴀᴍ</a>
✯ ʟᴀɴɢᴜᴀɢᴇ » <a href=https://www.python.org/>ᴘʏᴛʜᴏɴ</a>
✯ ᴠᴇʀsɪᴏɴ » 9
✯ ᴅᴀᴛᴀʙᴀsᴇ » <a href=https://www.mongodb.com>ᴍᴏɴɢᴏ ᴅʙ</a>
✯ sᴇʀᴠᴇʀ » <a href=https://signup.heroku.com/login>ʜᴇʀᴏᴋᴜ</a>
✯ ᴍʏ sᴛᴀᴛᴜs » v9.4.2 [ ᴏɴ ʙᴇᴛᴀ ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- 𝒓𝒆𝒂𝒍𝒍𝒚 𝒔𝒐𝒓𝒓𝒚 𝒊𝒂𝒎 𝒏𝒐𝒕 𝒓𝒆𝒂𝒅𝒚 𝒕𝒐 𝒈𝒊𝒗𝒆 𝒎𝒚 𝒔𝒐𝒖𝒄𝒓𝒆
- 𝑮𝒓𝒐𝒖𝒑 - https://t.me/mrlinkgrop

<b>ᴄʀᴇᴀᴛᴏʀs »</b>
- <a href=https://t.me/bibin_indian_rock>ʙɪʙɪɴ</a>"""
    MANUELFILTER_TXT = """ʜᴇʟᴘ » <b>Fɪʟᴛᴇʀs</b>

- 𝑴𝒂𝒏𝒖𝒍 𝑭𝒊𝒍𝒕𝒆𝒓 𝒊𝒔 𝒕𝒉𝒆 𝒇𝒆𝒂𝒕𝒖𝒓𝒆 𝒘𝒆𝒓𝒆 𝒖𝒔𝒆𝒓𝒔 𝒄𝒂𝒏 𝒔𝒆𝒕 𝒂𝒖𝒕𝒐 𝒓𝒆𝒑𝒍𝒊𝒆𝒔 𝒇𝒐𝒓 𝒑𝒂𝒓𝒕𝒊𝒄𝒖𝒍𝒂𝒓 𝒌𝒆𝒚𝒘𝒐𝒓𝒅𝒔 𝒂𝒏𝒅 𝒊 𝒘𝒊𝒍𝒍 𝒓𝒆𝒔𝒑𝒐𝒏𝒅 𝒘𝒉𝒆𝒏 𝒆𝒗𝒆𝒓 𝒕𝒉𝒂𝒕 𝒌𝒆𝒚𝒘𝒐𝒓𝒅 𝒇𝒐𝒖𝒏𝒅 𝒊𝒏 𝒚𝒐𝒖𝒓 𝒄𝒉𝒂𝒕..

<b>Nᴏᴛᴇ »</b>
1. 𝑰𝒂𝒎 𝒔𝒉𝒐𝒖𝒍𝒅 𝒃𝒆 𝒂 𝒂𝒅𝒎𝒊𝒏 𝒐𝒇 𝒚𝒐𝒖𝒓 𝒈𝒓𝒐𝒖𝒑
2. 𝑶𝒏𝒍𝒚 𝒂𝒅𝒎𝒊𝒏𝒔 𝒄𝒂𝒏 𝒇𝒊𝒍𝒕𝒆𝒓 𝒊𝒏 𝒎𝒚 𝒑𝒎
3. 𝑪𝒐𝒏𝒏𝒆𝒄𝒕 𝒈𝒓𝒐𝒖𝒑 𝒊𝒏 𝒎𝒚 𝒑𝒎 [𝒖𝒔𝒆 » `/connect - group id]\n𝒇𝒐𝒓 𝒆𝒙𝒂𝒎𝒑𝒍𝒆 `/connect -1234567890`
4. 𝑨𝒍𝒆𝒓𝒕 𝒃𝒖𝒕𝒕𝒐𝒏𝒔 𝒉𝒂𝒗𝒆 𝒍𝒊𝒎𝒊𝒕 64 𝒄𝒉𝒂𝒓𝒂𝒄𝒕𝒆𝒓𝒔

<b>Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ »</b>
• /filter ᴏʀ /add - <code>𝑨𝒅𝒅 𝑭𝒊𝒍𝒕𝒆𝒓 𝒊𝒏 𝑮𝒓𝒐𝒖𝒑/code>
• /filters ᴏʀ /viewfilters - <code>𝑳𝒊𝒔𝒕 𝒐𝒇 𝒂𝒍𝒍 𝑭𝒊𝒍𝒕𝒆𝒓𝒔 𝒊𝒏 𝒀𝒐𝒖𝒓 𝑮𝒓𝒐𝒖𝒑</code>
• /del - <code>𝑻𝒐 𝑫𝒆𝒍𝒆𝒕𝒆 𝒂 𝑭𝒊𝒍𝒕𝒆𝒓 𝒊𝒏 𝑮𝒓𝒐𝒖𝒑</code>
• /delall - <code>𝑫𝒆𝒍𝒆𝒕𝒆 𝑾𝒉𝒐𝒍𝒆 𝑭𝒊𝒍𝒕𝒆𝒓𝒔 𝒊𝒏 𝑮𝒓𝒐𝒖𝒑 (ᴀᴅᴍɪɴ ᴏɴʟʏ)</code>"""
    BUTTON_TXT = """ʜᴇʟᴘ:» <b>Buttons</b>

- ɪᴀᴍ sᴜᴘᴘᴏʀᴛᴇᴅ ᴏɴ ʙᴏᴛʜ ʙᴜᴛᴛᴏɴs (ᴜʀʟ , ᴀʟᴇʀᴛ)

<b>ɴᴏᴛᴇ »</b>
1. 𝑻𝒆𝒍𝒆𝒈𝒓𝒂𝒎 𝒘𝒊𝒍𝒍 𝒏𝒐𝒕 𝒂𝒍𝒍𝒐𝒘 𝒕𝒐 𝒔𝒆𝒏𝒅 𝒃𝒖𝒕𝒕𝒐𝒏 𝒘𝒊𝒕𝒉𝒐𝒖𝒕 𝒂𝒏𝒚 𝒄𝒐𝒏𝒕𝒆𝒏𝒕, 𝒔𝒐 𝒂𝒅𝒅 𝒂𝒏𝒚 𝒕𝒆𝒙𝒕 , 𝒑𝒉𝒐𝒕𝒐,𝒆𝒕𝒄𝒄 𝒐𝒏 𝒃𝒖𝒕𝒕𝒐𝒏 𝒇𝒊𝒍𝒕𝒆𝒓𝒊𝒏𝒈.
2. 𝑰 𝒔𝒖𝒑𝒑𝒐𝒓𝒕 𝒐𝒏 𝒂𝒏𝒚 𝒎𝒆𝒅𝒊𝒂 𝒕𝒉𝒂𝒕 𝒕𝒆𝒍𝒆𝒈𝒓𝒂𝒎 𝒔𝒖𝒑𝒑𝒐𝒓𝒕𝒔
3. 𝑩𝒖𝒕𝒕𝒐𝒏 𝒔𝒉𝒐𝒖𝒍𝒅 𝒃𝒆 𝒊𝒏 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒎𝒂𝒓𝒌𝒅𝒐𝒘𝒏 𝒇𝒐𝒓𝒎𝒂𝒕

<b>Uʀʟ ʙᴜᴛᴛᴏɴs »</b>
<code>[Button Text](buttonurl:https://t.me/dmx_chating)</code>

<b>Aʟᴇʀᴛ ʙᴜᴛᴛᴏɴs »</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """ʜᴇʟᴘ » <b>ᴀᴜᴛᴏ ғɪʟᴛᴇʀ</b>

<b>ɴᴏᴛᴇ ᴛᴏ ɪɴᴅᴇx »</b>

𝒀𝒐𝒖 𝒅𝒐𝒏𝒕 𝒕𝒉𝒊𝒏𝒌 𝒂𝒃𝒐𝒖𝒕 𝒊𝒕 𝒃𝒆𝒄𝒂𝒖𝒔𝒆 𝒊𝒂𝒎 𝒂𝒍𝒓𝒆𝒂𝒅𝒚 𝒂𝒅𝒅𝒆𝒅 𝒎𝒐𝒓𝒆 𝒕𝒉𝒂𝒏 2𝑴 𝒇𝒊𝒍𝒆𝒔 𝒊𝒏 𝒎𝒚 𝒅𝒂𝒕𝒂𝒃𝒂𝒔𝒆 𝒔𝒐 𝒚𝒐𝒖 𝒅𝒐𝒏𝒕 𝒏𝒆𝒆𝒅 𝒕𝒐 𝒂𝒅𝒅 𝒇𝒊𝒍𝒆𝒔 𝒂𝒏𝒚𝒎𝒐𝒓𝒆

1. 𝑴𝒂𝒌𝒆 𝒎𝒆 𝒂𝒔 𝒂𝒅𝒎𝒊𝒏 𝒊𝒇 𝒕𝒉𝒂𝒕 𝒄𝒉𝒂𝒏𝒏𝒆𝒍 𝒊𝒔 𝒑𝒓𝒊𝒗𝒂𝒕𝒆
2. 𝑴𝒂𝒌𝒆 𝒔𝒖𝒓𝒆 𝒕𝒉𝒂𝒕 𝒄𝒉𝒂𝒏𝒏𝒆𝒍 𝒅𝒐𝒆𝒔 𝒏𝒐𝒕 𝒄𝒐𝒏𝒕𝒂𝒊𝒏 𝒂𝒏𝒚 𝒑𝒓𝒐𝒏 𝒐𝒓 𝒂𝒏𝒚 𝒇𝒂𝒌𝒆 𝒇𝒊𝒍𝒆𝒔 ( ɪғ ɪ ғɪɴᴅ ʟɪᴋᴇ ᴛʜᴀᴛ ɪ ᴡɪʟʟ ʙᴀɴ ʏᴏᴜ ɪɴ ᴍʏ ᴅʙ ᴀɴᴅ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴍʏ ғᴇᴅ)
3. 𝑻𝒉𝒆𝒏 𝒇𝒐𝒓𝒘𝒂𝒓𝒅 𝒎𝒆 𝒕𝒉𝒆 𝒍𝒂𝒔𝒕 𝒎𝒆𝒔𝒔𝒂𝒈𝒆 𝒘𝒊𝒕𝒉 𝒇𝒐𝒓𝒘𝒂𝒓𝒅 𝒕𝒂𝒈𝒔 (ǫᴜᴏᴛᴇs)
 ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ғɪʟᴇs ᴛᴏ ᴍʏ ᴅʙ"""
    CONNECTION_TXT = """ʜᴇʟᴘ » <b>ᴄᴏɴɴᴇᴄᴛɪᴏɴs</b>

- 𝑼𝒔𝒆𝒅 𝑻𝒐 𝑪𝒐𝒏𝒏𝒆𝒄𝒕 𝑷𝑴 𝒊𝒏 𝑮𝒓𝒐𝒖𝒑
- ɪᴛ ʜᴇʟᴘs ᴛᴏ ᴘʀᴇᴠᴇɴᴛ ᴛʜᴇ ᴏᴠᴇʀ sᴘᴀᴍᴍɪɴɢ ᴏғ ɢʀᴏᴜᴘ

<b>ɴᴏᴛᴇ »</b>
1. 𝑶𝒏𝒍𝒚 𝒂𝒅𝒎𝒊𝒏𝒔 𝒄𝒂𝒏 𝒂𝒅𝒅 𝒂 𝒄𝒐𝒏𝒏𝒆𝒄𝒕𝒊𝒐𝒏 𝒕𝒐 𝒚𝒐𝒖𝒓 𝒈𝒓𝒐𝒖𝒑
3. 𝑴𝒂𝒌𝒆 𝒔𝒖𝒓𝒆 𝒕𝒉𝒂𝒕 𝑰𝒂𝒎 𝒂𝒅𝒎𝒊𝒏 𝒕𝒉𝒆𝒓𝒆
2. 𝑺𝒆𝒏𝒅 <code>/connect (ɢʀᴏᴜᴘ ɪᴅ)</code> 𝑻𝒐 𝑪𝒐𝒏𝒏𝒆𝒄𝒕

<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ »</b>
• /connect  - <code>𝑪𝒐𝒏𝒏𝒆𝒄𝒕 𝒂 𝒑𝒂𝒓𝒕𝒊𝒄𝒖𝒍𝒂𝒓 𝒄𝒉𝒂𝒕 𝒕𝒐 𝒎𝒚 𝑷𝑴</code>
• /disconnect  - <code>𝑫𝒊𝒔𝒄𝒐𝒏𝒏𝒆𝒄𝒕 𝒂 𝑪𝒉𝒂𝒕</code>
• /connections - <code>𝑳𝒊𝒔𝒕 𝒂𝒍𝒍 𝒚𝒐𝒖𝒓 𝑪𝒐𝒏𝒏𝒆𝒄𝒕𝒊𝒐𝒏</code>"""
    EXTRAMOD_TXT = """ʜᴇʟᴘ »<b>ᴇxᴛʀᴀ ᴍᴏᴅs</b>

<b>ɴᴏᴛᴇ »</b>
𝑻𝒉𝒆𝒓𝒆 𝒂𝒓𝒆 𝑺𝒐𝒎𝒆 𝑬𝒙𝒕𝒓𝒂 𝑴𝒐𝒅𝒔 𝑻𝒉𝒂𝒕 𝑰 𝑯𝒂𝒗𝒆

<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ »</b>
• /id - <code>𝑮𝒆𝒕 𝑰𝑫 𝒐𝒇 𝒂 𝒔𝒑𝒆𝒄𝒊𝒇𝒊𝒆𝒅 𝑼𝑺𝑬𝑹</code>
• /info  - <code>𝑮𝒆𝒕 𝒊𝒏𝒇𝒐 𝒂𝒃𝒐𝒖𝒕 𝑨 𝑼𝑺𝑬𝑹</code>
• /imdb  - <code>𝑮𝒆𝒕 𝒇𝒊𝒍𝒎 𝒊𝒏𝒇𝒐 𝒊𝒏 𝑰𝑴𝑫𝑩 𝑺𝑶𝑼𝑹𝑪𝑬</code>
• /search  - <code>𝑮𝒆𝒕 𝒕𝒉𝒆 𝒇𝒊𝒍𝒎 𝒊𝒏𝒇𝒐 𝒊𝒏 𝑽𝒂𝒓𝒊𝒐𝒖𝒔 𝑺𝑶𝑼𝑹𝑪𝑬 </code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>ɴᴏᴛᴇ »</b>
𝑻𝒉𝒊𝒔 𝒎𝒐𝒅𝒖𝒍𝒆 𝒐𝒏𝒍𝒚 𝒘𝒐𝒓𝒌𝒔 𝒇𝒐𝒓 𝒎𝒚 𝑨𝒅𝒎𝒊𝒏𝒔

<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ »</b>
• /logs - <code>𝑻𝒐 𝒈𝒆𝒕 𝒕𝒉𝒆 𝒓𝒆𝒔𝒄𝒆𝒏𝒕 𝒆𝒓𝒓𝒐𝒓𝒔</code>
• /stats - <code>𝑻ᴏ 𝒈𝒆𝒕 𝒔𝒕𝒂𝒕𝒖𝒔 𝒐𝒇 𝒇𝒊𝒍𝒆𝒔 𝒊𝒏 𝑫𝑩.</code>
• /delete - <code>𝑻𝒐 𝒅𝒆𝒍𝒆𝒕𝒆 𝒂 𝒔𝒑𝒆𝒄𝒊𝒇𝒊𝒄 𝒇𝒊𝒍𝒆 𝒇𝒓𝒐𝒎 𝑫𝑩.</code>
• /users - <code>𝑻𝒐 𝒈𝒆𝒕 𝒍𝒊𝒔𝒕 𝒐𝒇 𝒎𝒚 𝒖𝒔𝒆𝒓𝒔 𝒂𝒏𝒅 𝑰𝑫𝑺.</code>
• /chats - <code>𝑻𝒐 𝒈𝒆𝒕 𝒍𝒊𝒔𝒕 𝒐𝒇 𝒕𝒉𝒆 𝒎𝒚 𝒄𝒉𝒂𝒕𝒔 𝒂𝒏𝒅 𝑰𝑫𝑺 </code>
• /leave  - <code>𝑻𝒐 𝒍𝒆𝒂𝒗𝒆 𝒇𝒓𝒐𝒎 𝒂 𝒄𝒉𝒂𝒕.</code>
• /disable  -  <code>𝑫𝒐 𝒅𝒊𝒔𝒂𝒃𝒍𝒆 𝒂 𝒄𝒉𝒂𝒕.</code>
• /ban  - <code>𝑻𝒐 𝒃𝒂𝒏 𝒂 𝒖𝒔𝒆𝒓.</code>
• /unban  - <code>𝑻𝒐 𝒖𝒏𝒃𝒂𝒏 𝒂 𝒖𝒔𝒆𝒓.</code>
• /channel - <code>𝑻𝒐 𝒈𝒆𝒕 𝒍𝒊𝒔𝒕 𝒐𝒇 𝒕𝒐𝒕𝒂𝒍 𝒄𝒐𝒏𝒏𝒆𝒄𝒕𝒊𝒐𝒏 𝒄𝒉𝒂𝒏𝒏𝒆𝒍𝒔</code>
• /broadcast - <code>𝑻𝒐 𝒃𝒓𝒐𝒂𝒅𝒄𝒂𝒔𝒕 𝒂 𝒎𝒆𝒔𝒔𝒂𝒈𝒆 𝒕𝒐 𝒂𝒍𝒍 𝒖𝒔𝒆𝒓𝒔</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ʙᴏᴛ = #cl af 2
ID - <code>{}</code>
Name - {}
"""
