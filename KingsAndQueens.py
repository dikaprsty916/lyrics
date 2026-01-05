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
    title = "== KINGS AND QUEENS =="

    lines = [
        ("I can feel my body shake", 0.062),
        ("there's only so much I can take", 0.052),
        ("I'll show you how a real queen behaves", 0.052),
        ("oh...", 0.062),
        ("No damsel in distress", 0.072),
        ("don't need to save me", 0.052),
        ("Once I start breathing fire", 0.072),
        ("you can't tame me", 0.052),
        ("And you might think I'm weak without a sword", 0.072),
        ("But if I had one, it'd be bigger than yours", 0.072),
        ("If all of the kings had their queens on the throne", 0.062),
        ("We would pop champagne and raise a toast", 0.062),
        ("To all of the queens who are fighting alone", 0.062),
        ("Baby, you're not dancin' on your own", 0.062),
    ]

    delays = [0.3, 0.3, 0.4, 1, 0.2, 1, 0.2, 0.4, 0.4, 0.7, 0.4, 0.4, 0.4, 0.4]

    hide_cursor()
    try:
        print(f"\n[bold #FFD700]{title}[/bold #FFD700]\n")

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