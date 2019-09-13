import asyncio
import datetime
from telethon import events
from telethon.tl import functions, types
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="print ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 16)
    input_str = event.pattern_match.group(1)
    if input_str == "repo":
        await event.edit("Click [here](https://github.com/Priyam005/TelegramUserBot/) to goto the custom github repo.")
    elif input_str == "deploy":
        await event.edit("Click [here](https://dashboard.heroku.com/apps/userbot-telegram/deploy/github) to goto the heroku deploy page.")
    elif input_str == "mf":
        await event.edit("""
......................................../´¯/) 
......................................,/¯../ 
...................................../..../ 
..................................../´.¯/
..................................../´¯/
..................................,/¯../ 
................................../..../ 
................................./´¯./
................................/´¯./
..............................,/¯../ 
............................./..../ 
............................/´¯/
........................../´¯./
........................,/¯../ 
......................./..../ 
....................../´¯/
....................,/¯../ 
.................../..../ 
............./´¯/'...'/´¯¯·¸ 
........../'/.../..../......./¨¯\ 
........('(...´...´.... ¯~/'...') 
.........\.................'...../ 
..........''...\.......... _.·´ 
............\..............( 
..............\.............\...`
    """)
    elif input_str == "yee":
        await event.edit("""
ツ
""")
    elif input_str == "happy":
        await event.edit("""
(ʘ‿ʘ)
""")
    elif input_str == "happy2":
        await event.edit("""
=͟͟͞͞٩(๑☉ᴗ☉)੭ु⁾⁾
""")
    elif input_str == "happy3":
        await event.edit("""
ヾ(o✪‿✪o)ｼ
""")
    elif input_str == "crying":
        await event.edit("""
༎ຶ‿༎ຶ
""")
    elif input_str == "dicc":
        await event.edit("""
╰U╯☜(◉ɷ◉ )
""")
    elif input_str == "fek":
        await event.edit("""
╰U╯\n\n(‿ˠ‿)
""")
    elif input_str == "ded":
        await event.edit("""
✖‿✖
""")
    elif input_str == "sad":
        await event.edit("""
⊙︿⊙
""")
    elif input_str == "lenny":
        await event.edit("""
( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)
""")
    elif input_str == "packs":
        await event.edit("""
Your 1st sticker pack can be found [here](https://t.me/addstickers/Uniborg_Pack_843901469)\n\nYour 2nd sticker pack can be found [here](https://t.me/addstickers/Uniborg_Pack2_843901469)\n\nYour 3rd sticker pack can be found [here](https://t.me/addstickers/Uniborg_Pack3_843901469)\n\nYour animated sticker pack can be found [here](https://t.me/addstickers/Uni_Borgpack_843901469_as)\n\nYour 2nd animated sticker pack can be found [here](https://t.me/addstickers/Uni_Borg_Pack2_843901469_as)
""")
    else:
        await event.edit("variable not defined.")
