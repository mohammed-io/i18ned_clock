import curses
import asyncio
from datetime import datetime
import pytz
import os
  

class Clock(object):
    def __init__(self, timezone):
        self.tz = pytz.timezone(timezone)

    def paint(self, frame):
        if frame >= 30:
            return datetime.now(tz=self.tz).strftime("%H %M %S (UTC%Z)")
        else:
            return datetime.now(tz=self.tz).strftime("%H:%M:%S (UTC%Z)")


async def init_screen(stdscr, clock, y=0, x=0):
    curses.curs_set(0) 

    frame = 0
    num = 0
    while True:
        try:
            stdscr.addstr(y, x, clock.paint(frame), curses.A_BOLD)
            await asyncio.sleep(1/60)
            stdscr.refresh()
            frame = (frame + 1) % 60
            num += 1
            if num == 240:
                break
        except:
            raise Exception('Window size is small.')
            

class Tiles(object):
    y = 0
    x = 0
    
    def __init__(self, stdscr):
        self.stdscr = stdscr
   
    async def row(self, clocklist):
        resultedCoroutines = []
        x = Tiles.x
        for c in clocklist:
            resultedCoroutines.append(init_screen(self.stdscr, c, y=Tiles.y, x=x))
            x += 30
        Tiles.y += 3
        return resultedCoroutines

    async def column(self, clocklist):
        resultedCoroutines = []
        y = Tiles.y
        for c in clocklist:
            resultedCoroutines.append(init_screen(self.stdscr, c, y=y, x=Tiles.x))
            y += 3
        Tiles.x += 30
        return resultedCoroutines


clock1 = Clock("Asia/Baghdad")
clock2 = Clock("Asia/Kabul")

async def main(stdscr):
    t = Tiles(stdscr) 

    row1 = await t.row([clock1, clock2, clock1, clock2, clock1])
    row2 = await t.row([clock1, clock1, clock1, clock1, clock1])
    col1 = await t.column([clock1, clock2, clock1])
    col2 = await t.column([clock1, clock2, clock1])
    row3 = await t.row([clock1, clock1, clock1, clock2, clock2])
    await asyncio.gather(*row1, *row2, *col1, *col2, *row3)  

curses.wrapper(lambda stdscr: asyncio.run(main(stdscr)))

