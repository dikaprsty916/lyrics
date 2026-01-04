from rich import print
from time import sleep
import os

os.system('cls')

lines = [
    (0.8, "I'd let the world burn", 0.1),
    (0.8, "Let the world burn for you", 0.1),
    (0.8, "This is how it always had to end", 0.07),
    (0.8, "If I can't have you, then no one can", 0.07),
    (0.8, "I'd let it burn", 0.1),
    (1, "I'd let the world burn" , 0.087),
    (0.8, "Just to hear you calling out my name", 0.069),
    (0.8, "Watchin' it all go down in flames", 0.065),
]

symbols = ['@','#','$','%','&','/','!']
def printLyrics():
    for i, (lines_delay, line, char_delay) in enumerate(lines):
        for char in line:             
            for i in symbols:
                print(i, end='\x08', flush=True)
                sleep(char_delay/len(symbols)/2)      
            print(f"{char}",end='')           
        sleep(lines_delay)
        print()
printLyrics()
