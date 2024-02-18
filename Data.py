# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    GETHELP = """
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

"""

    close = [
        [InlineKeyboardButton("close", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("close", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("about me", callback_data="about"),
            InlineKeyboardButton("close", callback_data="close")
        ],
    ]

    ABOUT = """
<b>┏• Creator : <a href='tg://settings'>yours truly</a>\n┣• Channel : <a href='https://t.me/AnimeXWrld'>Anime Wrld</a>\n┗• Support Group : <a href='https://t.me/AnimeXWrld_Chat'>Anime Wrld Chat</a></b>
"""
