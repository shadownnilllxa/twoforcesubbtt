# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Commands for BOT Users
 ├ /start - Starts the Bot
 ├ /about - About this Bot
 ├ /help - Help this Bot Command
 ├ /ping - To check live bots
 └ /uptime - To see bot status
 
 ❏ Commands For BOT Admins
 ├ /logs - To view bot logs
 ├ /setvar - To set var with dibot command
 ├ /delvar - To remove var with dibot command
 ├ /getvar - To see one of the var with dibot command
 ├ /users - To view bot user statistics
 ├ /batch - To link more than one file
 ├ /speedtest - To test the bot server speed
 └ /broadcast - To send a broadcast message to the bot user

👨‍💻 Develoved by </b><a href='https://t.me/Its_Oreki_Hotarou'>Hōᴛᴀʀō Oʀᴇᴋɪ</a>
"""

    close = [
        [InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about"),
            InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")
        ],
    ]

    ABOUT = """
<b>Hi there this is a file store bot which is convert any file to link...
then you can access this file through a specific link...!

 • Creator: <a href='https://t.me/Its_Oreki_Hotarou'>Hōᴛᴀʀō Oʀᴇᴋɪ</a>
 • My Channel: <a href='https://t.me/Anime_X_Hunters'>Aɴɪᴍᴇ x Hᴜɴᴛᴇʀꜱ</a>
 • Source Code: <a href='https://github.com/Sahil0976'>Nᴏᴢᴇʟ Sɪʟᴠᴀ</a>

👨‍💻 Develoved by </b><a href='https://t.me/Lunatic0de/101'>@Lunatic0de</a>
"""
