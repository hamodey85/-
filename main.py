import webbrowser
import time

breaks = 3
sleep = 60*60*2
url = "https://www.youtube.com/watch?v=RvhU7Th9_OI&t="

while breaks !=0:
    time.sleep(sleep)
    webbrowser.open(url)
    breaks -=1