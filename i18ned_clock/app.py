
import time
import curses
from threading import Thread
import asyncio


class TimeZone(object):
    def __init__(self, timezone):
        self.timezone = timezone
    
    def calculate_current_time(self, colons):
        localTime = time.localtime()

        if colons == False:
            colons = " "
        else:
            colons = ":"
        currentTime = time.strftime("%H{0}%M{0}%S (GMT+{1})".format(colons, self.timezone), localTime)
        return currentTime

        


class Clock(object):
    def __init__(self, timezone):
        self.timezone = timezone
        self.timezoneObj = TimeZone(self.timezone)

    def paint(self, frame):
        localTime = time.localtime()

        if frame >= 30:
            return time.strftime("%H:%M:%S (GMT+{1})".format(self.timezone), localTime)
        else:
            return time.strftime("%H %M %S (GMT+{1})".format(self.timezone), localTime)


    def __str__(self, colons=True):
        return self.timezoneObj.calculate_current_time(colons)



async def init_screen(stdscr, clock, pos_y, pos_x):
    curses.curs_set(0) 
    
    if pos_y >= 15 or pos_x >= 150:
            y_limit = 15; x_limit = 150
            raise Exception(f"You can only set positions smaller than {y_limit} for y, and {x_limit} for x")


    frame = 0

    while True:
        clock.paint()
        stdscr.addstr(pos_y, pos_x, clock.__str__(), curses.A_BOLD)
        # await asyncio.sleep(0.5)
        # await asyncio.sleep(1/60)

        frame = (frame + 1) % 60
        # ..... clock.paint()

        stdscr.refresh()
        stdscr.addstr(pos_y,pos_x, clock.__str__(colons=False), curses.A_BOLD)
        await asyncio.sleep(0.5)
        stdscr.refresh()

    

clock1 = Clock(3)
clock2 = Clock(4)

async def main(stdscr):

    await asyncio.gather(
        asyncio.create_task(init_screen(stdscr, clock1, 0, 10)),
        asyncio.create_task(init_screen(stdscr, clock1, 0, 40)),
        asyncio.create_task(init_screen(stdscr, clock1, 0, 70))
    )




curses.wrapper(lambda stdscr: asyncio.run(main(stdscr)))



