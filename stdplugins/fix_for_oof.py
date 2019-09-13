# oof.py and fix_for_oof.py both are required for this fix to function.

from telethon import events
import asyncio
from collections import deque


@borg.on(events.NewMessage(pattern=r"\.oof", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list(";_;"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
		await event.edit(";_;")
    
