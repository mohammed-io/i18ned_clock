import curses
import asyncio
from datetime import datetime
import pytz

  

class Clock(object):
    def __init__(self, timezone):
        self.timezone = timezone
        self.tz = pytz.timezone(self.timezone)

    def paint(self, frame):
        if frame >= 30:
            return datetime.now(tz=self.tz).strftime("%H %M %S (UTC%Z)")
        else:
            return datetime.now(tz=self.tz).strftime("%H:%M:%S (UTC%Z)")



async def init_screen(stdscr, clock, pos_y, pos_x):
    curses.curs_set(0) 
    
    if pos_y >= 15 or pos_x >= 150:
            y_limit = 15; x_limit = 150
            raise Exception(f"You can only set positions smaller than {y_limit} for y, and {x_limit} for x")

    frame = 0
    while True:
        stdscr.addstr(pos_y, pos_x, clock.paint(frame), curses.A_BOLD)
        await asyncio.sleep(1/60)
        stdscr.refresh()

        frame = (frame + 1) % 60
        


clock1 = Clock("Asia/Baghdad")
clock2 = Clock("Asia/Kabul")

async def main(stdscr):
    await asyncio.gather(init_screen(stdscr, clock1, 0, 10), init_screen(stdscr, clock2, 0, 40))
    

curses.wrapper(lambda stdscr: asyncio.run(main(stdscr)))



