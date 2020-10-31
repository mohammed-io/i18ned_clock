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


class Screen:
    y = 0
    x = 0
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


resultedCoroutines = []


class Row(Screen):
    def __init__(self, stdscr, clocks):
        self.clocks = clocks
        self.stdscr = stdscr

    async def paint(self):
        for clock in self.clocks:
            resultedCoroutines.append(Screen.init_screen(self.stdscr, clock, Screen.y, Screen.x))
            Screen.x += 30
        Screen.x = 0
        Screen.y += 4   


class Column(Screen):
    def __init__(self, stdscr, clocks):
        self.clocks = clocks
        self.stdscr = stdscr

    async def paint(self):
        for clock in self.clocks:
            resultedCoroutines.append(Screen.init_screen(self.stdscr, clock, Screen.y, Screen.x))
            Screen.y += 3
        Screen.x = 0
        Screen.y += 1


clock1 = Clock("Asia/Baghdad")
clock2 = Clock("Asia/Kabul")


async def main(stdscr):
    Column(stdscr, clocks=[Row(stdscr, clocks=[await Column(stdscr, clocks=[clock1, clock2, clock1, clock1]).paint()]), await Row(stdscr, clocks=[clock1, clock2, clock1]).paint(), await Column(stdscr, clocks=[clock1, clock2, clock1]).paint(), await Row(stdscr, clocks=[clock1, clock2, clock1, clock1]).paint()])
    await asyncio.gather(*resultedCoroutines) 

curses.wrapper(lambda stdscr: asyncio.run(main(stdscr)))