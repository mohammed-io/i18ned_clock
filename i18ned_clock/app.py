
import time
import curses
from threading import Thread



class TimeZone(object):
    def __init__(self, timezone):
        self.timezone = timezone
    
    def calculateCurrentTime(self, colons):
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

    def __str__(self, colons=True):
        return self.timezoneObj.calculateCurrentTime(colons)




def initScreen(stdscr, clock, pos_y, pos_x):
    curses.curs_set(0) 
    
    if pos_y >= 15 or pos_x >= 150:
            y_limit = 15; x_limit = 150
            raise Exception(f"You can only set positions smaller than {y_limit} for y, and {x_limit} for x")


    num = 0
    while True:
        stdscr.addstr(pos_y, pos_x, clock.__str__(), curses.A_BOLD)
        time.sleep(0.5)
        stdscr.refresh()
        stdscr.addstr(pos_y,pos_x, clock.__str__(colons=False), curses.A_BOLD)
        time.sleep(0.5)
        stdscr.refresh()

        num += 1
        if num >= 10:
            break
    

clock1 = Clock(3)
clock2 = Clock(4)

def main(stdscr):
    Thread(target=initScreen, args=(stdscr, clock1, 0, 10)).start()
    Thread(target=initScreen, args=(stdscr, clock1, 0, 40)).start()
    Thread(target=initScreen, args=(stdscr, clock2, 0, 70)).start()



curses.wrapper(main)



