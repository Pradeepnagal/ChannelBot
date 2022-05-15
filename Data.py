from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

You can use me to manage channels with tons of features. Use below buttons to learn more !

By @king_pk
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ Hindi Hd Movie's  ✨", url="https://t.me/bkup_film")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ YouTube ♥", url="https://youtube.com/channel/UCoVZmEvmwlJTeHHps1fynjQ")],
        [InlineKeyboardButton("🔥 Instagram 🔥", url="https://instagram.com/pradeep___nagal")],
    ]

    # Help Message
    HELP = """
Everything is self explanatory after you add a channel.
To add a channel use keyboard button 'Add Channels' or alternatively for ease, use `/add` command

✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot

Alternative Commands
/channels - List added Channels
/add - Add a channel
/report - Report a Problem
    """

    # About Message
    ABOUT = """
**About This Bot** 

A telegram channel automation bot by @king_pk

Instagram : [Click Here](https://instagram.com/pradeep___nagal)

Movie's Channel : [Join Now](https://t.me/bkup_film)

YouTube : [Subscribe](https://youtube.com/channel/UCoVZmEvmwlJTeHHps1fynjQ)

Developer : @king_pk
    """
