import sys
from rich import print
from time import sleep

def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def printLyrics():
    lines = [
        ("We gonna party like it's 3012 tonight", 0.07),
        ("I wanna show you all the finer things in life", 0.07),
        ("So just forget about the world, we young tonight", 0.07),
        ("I'm coming for ya, I'm coming for ya", 0.07),
        ("Cause all...", 0.15),
        ("I need", 0.15),
        ("Is a beauty and a beat", 0.13),
        ("Who can make my life complete", 0.13),
        ("It's all...", 0.15),
        ("'bout you ", 0.15),
        ("When the music makes you move", 0.11),
        ("Baby, do it like you do", 0.11)
    ]

    delays = [0.6, 0.6, 0.4, 0.4, 1.5, 0.6, 0.6, 1.5, 2, 0.6, 0.6]

    hide_cursor()
    try:
        for i, (line, char_delay) in enumerate(lines):
            for char in line:
                print(f"[bold white]{char}[/bold white]", end="")
                sys.stdout.flush()
                sleep(char_delay)
            print()
            if i < len(delays):
                sleep(delays[i])
    finally:
        sleep(3)
        show_cursor()

printLyrics()

