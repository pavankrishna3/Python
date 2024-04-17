import curses
from curses import wrapper
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the speed typing test")
    stdscr.addstr("\npress any key to continue")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, current ,target ,wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1,0,f"WPM : {wpm}")
    for i , char in enumerate(current):
        color = curses.color_pair(2)

        if char == target[i]:
            color = curses.color_pair(1)
        stdscr.addstr(0,i,char,color)

def wpm_test(stdscr):
    target_text = "This is the target text"
    current_text = []
    wpm = 0
    start_time = time.time()

    stdscr.nodelay(True)
    while True:
        elapsed_time = max(time.time( ) - start_time , 1)
        wpm =  round((len(current_text)/elapsed_time)*60/5)

        stdscr.clear()
        display_text(stdscr,current_text,target_text,wpm)
        stdscr.refresh()

        if "".join(current_text)==target_text:
            stdscr.nodelay(False)
            break


        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text)>0:
                current_text.pop()
        elif len(current_text)<len(target_text):
            current_text.append(key)


def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)

    start_screen(stdscr)

    while True:
        wpm_test(stdscr)

        stdscr.addstr(2,0,"you have completed the text. press any key to continue or  ESC to quit")
        key = stdscr.getkey()
        
        if ord(key) == 27:
            break

        

wrapper(main)