from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.regex(r'^Report a Problem$') | filters.command('report'))
async def _manage(_, msg):
    how = '**Report a Problem** \n\n'
    how += "If something **unexpected** happens, you can report it to us.\n\n"
    how += '**Steps** \n'
    how += '1) Try whatever you did again. If it shows the same unexpected thing, move to step 2 \n'
    how += '2) Visit @king_pk and define your problem **completely**, i.e, what you expected and what happened instead.'
    how += "If you don't get a reply within 2 days msg me again, "
    await msg.reply(
        how,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton('Support Group', url='https://t.me/king_pk')]
        ]),
        quote=True
    )
