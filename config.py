import os, time, re
id_pattern = re.compile(r'^.\d+$')



class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "28786884")
    API_HASH  = os.environ.get("API_HASH", "e45e49071c6f1ce834201a5611e75b81")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6864648554:AAH0VtehZo8wD4_6keIXsgvyYxu0ZXbaG7o") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","mongodb+srv://vishnu:vishnu@cluster0.yolrhee.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")     
    DB_URL  = os.environ.get("DB_URL","Cluster0")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/23ded828669a39e39fa85-1e564467f4f56e0523.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5807740619').split()]

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "-1001996186113") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002052274277"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """Hello {} 👋 

➻ This Is An Advanced And Yet Powerful Rename Bot.

➻ Using This Bot You Can Rename And Change Thumbnail Of Your Files.

➻ You Can Also Convert Video To File And File To Video.

➻ This Bot Also Supports Custom Thumbnail And Custom Caption.

<b>Bot Is Made By :</b> @TGCinemaworld"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 My Nᴀᴍᴇ : {}
├👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/Vishnudhfm14>Vɪsʜɴᴜ MB🤍</a>
├☃️ Fᴏᴜɴᴅᴇʀ Oꜰ : <a href=https://t.me/TGCinemaworld>Jᴏɪɴ Hᴇʀᴇ</a>
├📕 Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
├✏️ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pyᴛʜᴏɴ 3</a>
├💾 Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>
├🌀 Mʏ Sᴇʀᴠᴇʀ : <a href=https://dashboard.render.com>Rᴇɴᴅᴇʀ</a>
╰───────────────⍟ </b>"""

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail.
➪ /view_thumb - Use This Command To View Your Current Thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption
➪ Example - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

✏️ <b><u>How To Rename A File</u></b>

➪ Send Any File And Type New File Name And Select The Format [ Document, Video, Audio ].           

𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/MadflixOfficials>Developer</a>
"""

    PROGRESS_BAR = """\n
 <b>🔗 Size :</b> {1} | {2}
️ <b>⏳️ Done :</b> {0}%
 <b>🚀 Speed :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.

<b>🛍 UPI ID:</b> `wishvishnu179-1@okaxis`
"""


    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

<b>☞ Fᴏʀ Exᴀᴍᴘʟᴇ :-</b>

◦ <code><b> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="𝙑𝙄𝙎𝙃𝙉𝙐👽@𝐓𝐆𝐂𝐢𝐧𝐞𝐦𝐚𝐰𝐨𝐫𝐥𝐝" -metadata author="𝙑𝙄𝙎𝙃𝙉𝙐👽@𝐓𝐆𝐂𝐢𝐧𝐞𝐦𝐚𝐰𝐨𝐫𝐥𝐝" -metadata:s:s title="Subs By :-𝐕𝐢𝐬𝐡𝐧𝐮 𝐌𝐁🤍" -metadata:s:a title="𝙑𝙄𝙎𝙃𝙉𝙐👽@𝐓𝐆𝐂𝐢𝐧𝐞𝐦𝐚𝐰𝐨𝐫𝐥𝐝" -metadata:s:v title="𝙑𝙄𝙎𝙃𝙉𝙐👽@𝐓𝐆𝐂𝐢𝐧𝐞𝐦𝐚𝐰𝐨𝐫𝐥𝐝" </code>

<b><i>📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @Vishnudhfm14</b></i>
"""








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper
