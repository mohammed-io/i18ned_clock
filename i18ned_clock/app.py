import curses
import asyncio
from datetime import datetime
import pytz


class Clock:
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


    async def init_screen(stdscr, clock, y=y, x=x):
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


class Column:
    def __init__(self, children):
        self.children = children

    def paint(self, frame):
        return "\n".join([c.paint(frame) for c in self.children])


class Row:
    def __init__(self, children):
        self.children = children

    def paint(self, frame):
        return "\t".join([c.paint(frame) for c in self.children])


clock1 = Clock("Asia/Baghdad")
clock2 = Clock("Asia/Kabul")


async def main(stdscr):
    await asyncio.gather(init_screen(stdscr, Column(children=[clock1, clock2, clock1]), 0, 0), init_screen(stdscr, Row(children=[clock1, clock1]), 5, 0),  init_screen(stdscr, Row(children=[clock1, clock1, clock1, clock1]), 8, 20))

curses.wrapper(lambda stdscr: asyncio.run(main(stdscr)))